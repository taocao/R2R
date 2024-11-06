from .auth import R2RAuthProvider, SupabaseAuthProvider
from .crypto import BCryptConfig, BCryptProvider
from .database import PostgresDBProvider
from .email import AsyncSMTPEmailProvider, ConsoleMockEmailProvider
from .embeddings import (
    LiteLLMEmbeddingProvider,
    OllamaEmbeddingProvider,
    OpenAIEmbeddingProvider,
)
from .ingestion import (  # type: ignore
    R2RIngestionConfig,
    R2RIngestionProvider,
    UnstructuredIngestionConfig,
    UnstructuredIngestionProvider,
)
from .llm import LiteLLMCompletionProvider, OpenAICompletionProvider
from .logger import SqlitePersistentLoggingProvider
from .orchestration import (
    HatchetOrchestrationProvider,
    SimpleOrchestrationProvider,
)
from .user_management import R2RUserManagementProvider

__all__ = [
    # Auth
    "R2RAuthProvider",
    "SupabaseAuthProvider",
    # Ingestion
    "R2RIngestionProvider",
    "R2RIngestionConfig",
    "UnstructuredIngestionProvider",
    "UnstructuredIngestionConfig",
    # Crypto
    "BCryptProvider",
    "BCryptConfig",
    # Database
    "PostgresDBProvider",
    # Embeddings
    "LiteLLMEmbeddingProvider",
    "OllamaEmbeddingProvider",
    "OpenAIEmbeddingProvider",
    # Email
    "AsyncSMTPEmailProvider",
    "ConsoleMockEmailProvider",
    # Orchestration
    "HatchetOrchestrationProvider",
    "SimpleOrchestrationProvider",
    # LLM
    "OpenAICompletionProvider",
    "LiteLLMCompletionProvider",
    # Logging
    "SqlitePersistentLoggingProvider",
    # User Management
    "R2RUserManagementProvider",
]
