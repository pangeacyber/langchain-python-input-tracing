from __future__ import annotations

from pathlib import Path
from typing import Any, override

import click
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from pydantic import SecretStr

from langchain_input_tracing.tracers import PangeaAuditCallbackHandler

PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "human",
            """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {input}
Context: {context}
Answer:""",
        ),
    ]
)

docs_loader = DirectoryLoader(
    str(Path(__file__).parent.joinpath("data").resolve(strict=True)), glob="**/*.md", show_progress=True
)
docs = docs_loader.load()
text_splitter = CharacterTextSplitter(chunk_size=3500, chunk_overlap=50)
docs_split = text_splitter.split_documents(docs)


class SecretStrParamType(click.ParamType):
    name = "secret"

    @override
    def convert(self, value: Any, param: click.Parameter | None = None, ctx: click.Context | None = None) -> SecretStr:
        if isinstance(value, SecretStr):
            return value

        return SecretStr(value)


SECRET_STR = SecretStrParamType()


@click.command()
@click.option("--model", default="gpt-4o-mini", show_default=True, required=True, help="OpenAI model.")
@click.option(
    "--audit-token",
    envvar="PANGEA_AUDIT_TOKEN",
    type=SECRET_STR,
    required=True,
    help="Pangea Secure Audit Log API token. May also be set via the `PANGEA_AUDIT_TOKEN` environment variable.",
)
@click.option(
    "--audit-config-id",
    help="Pangea Secure Audit Log configuration ID.",
)
@click.option(
    "--pangea-domain",
    envvar="PANGEA_DOMAIN",
    default="aws.us.pangea.cloud",
    show_default=True,
    required=True,
    help="Pangea API domain. May also be set via the `PANGEA_DOMAIN` environment variable.",
)
@click.option(
    "--openai-api-key",
    envvar="OPENAI_API_KEY",
    type=SECRET_STR,
    required=True,
    help="OpenAI API key. May also be set via the `OPENAI_API_KEY` environment variable.",
)
@click.argument("prompt")
def main(
    *,
    prompt: str,
    audit_token: SecretStr,
    audit_config_id: str | None = None,
    pangea_domain: str,
    model: str,
    openai_api_key: SecretStr,
) -> None:
    embeddings_model = OpenAIEmbeddings(api_key=openai_api_key)
    vectorstore = FAISS.from_documents(documents=docs_split, embedding=embeddings_model)
    retriever = vectorstore.as_retriever()

    llm = ChatOpenAI(model=model, api_key=openai_api_key)
    qa_chain = create_stuff_documents_chain(llm, PROMPT)

    rag_chain: Runnable = create_retrieval_chain(retriever, qa_chain)

    audit_callback = PangeaAuditCallbackHandler(token=audit_token, domain=pangea_domain, config_id=audit_config_id)
    click.echo(rag_chain.invoke({"input": prompt}, config={"callbacks": [audit_callback]})["answer"])


if __name__ == "__main__":
    main()
