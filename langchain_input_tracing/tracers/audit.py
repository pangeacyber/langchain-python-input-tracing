from __future__ import annotations

from typing import Any, override

from langchain_core.tracers.base import BaseTracer
from langchain_core.tracers.schemas import Run
from pangea import PangeaConfig
from pangea.services import Audit
from pangea.services.audit.util import canonicalize_json
from pydantic import SecretStr

__all__ = ["PangeaAuditCallbackHandler"]


class PangeaAuditCallbackHandler(BaseTracer):
    """
    Tracer that creates an event in Pangea's Secure Audit Log when input for an
    LLM is received.
    """

    _client: Audit

    def __init__(
        self,
        *,
        token: SecretStr,
        config_id: str | None = None,
        domain: str = "aws.us.pangea.cloud",
        log_missing_parent: bool = False,
        **kwargs: Any,
    ) -> None:
        """
        Args:
            token: Pangea Secure Audit Log API token.
            config_id: Pangea Secure Audit Log configuration ID.
            domain: Pangea API domain.
        """

        super().__init__(**kwargs)
        self.log_missing_parent = log_missing_parent
        self._client = Audit(token=token.get_secret_value(), config=PangeaConfig(domain=domain), config_id=config_id)

    @override
    def _persist_run(self, run: Run) -> None:
        pass

    @override
    def _on_llm_start(self, run: Run) -> None:
        inputs = {"prompts": [p.strip() for p in run.inputs["prompts"]]} if "prompts" in run.inputs else run.inputs
        self._client.log_bulk(
            [
                {
                    "event_type": "inference:user_prompt",
                    "event_tools": run.name,
                    "event_input": canonicalize_json(inputs).decode("utf-8"),
                }
            ]
        )
