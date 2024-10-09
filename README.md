# Input Tracing for LangChain in Python

An example CLI tool in Python that demonstrates integrating Pangea's
[Secure Audit Log][] service into a LangChain app to maintain an audit log of context and
prompts being sent to LLMs.

In this case, our topic context consists of articles about authentication from our 
[Secure by Design Hub][] included in  `langchain_input_tracing/data`.

## Prerequisites

- Python v3.12 or greater.
- pip v24.2 or [uv][] v0.4.5.
- A [Pangea account][Pangea signup] with Secure Audit Log enabled.
- An [OpenAI API key][OpenAI API keys].
- libmagic

## Setup

```shell
git clone https://github.com/pangeacyber/langchain-python-input-tracing.git
cd langchain-python-input-tracing
```

### Install libmagic

This is included in Windows via the python-magic-bin package

On macOS, you can install via this shell command:

```shell
brew install libmagic
```

If using pip:

```shell
python -m venv .venv
source .venv/bin/activate
pip install .
```

Or, if using uv:

```shell
uv sync
source .venv/bin/activate
```

The sample can then be executed with:

```shell
python -m langchain_input_tracing "What do you know about OAuth?"
```

*Note:* Because our context is limited to the authentication articles mentioned above, if you ask a question outside that context, you will get some variation of "I don't know."


## Usage

```
Usage: python -m langchain_input_tracing [OPTIONS] PROMPT

Options:
  --model TEXT             OpenAI model.  [default: gpt-4o-mini; required]
  --audit-token SECRET     Pangea Secure Audit Log API token. May also be set
                           via the `PANGEA_AUDIT_TOKEN` environment variable.
                           [required]
  --audit-config-id TEXT   Pangea Secure Audit Log configuration ID.
  --pangea-domain TEXT     Pangea API domain. May also be set via the
                           `PANGEA_DOMAIN` environment variable.  [default:
                           aws.us.pangea.cloud; required]
  --openai-api-key SECRET  OpenAI API key. May also be set via the
                           `OPENAI_API_KEY` environment variable.  [required]
  --help                   Show this message and exit.
```

### Example Input

```shell
python -m langchain_input_tracing "What do you know about OAuth?"
```

### Sample Output

To secure your web app, embrace transparency in your security efforts and adopt Secure by Design principles, which focus on integrating security throughout the software development lifecycle. Implement application security hardening, robust user authentication, and secure default settings to enhance overall security. Additionally, consider using multi-factor authentication (MFA) and regularly educate users on best practices to protect their accounts.


[Secure Audit Log]: https://pangea.cloud/docs/audit/
[Pangea signup]: https://pangea.cloud/signup
[Secure by Design Hub]: https://pangea.cloud/securebydesign/
[OpenAI API keys]: https://platform.openai.com/api-keys
[uv]: https://docs.astral.sh/uv/
