from dataclasses import dataclass
from dataclasses import field

from aws_cdk import aws_logs as logs


@dataclass
class Config:
    """Configuration for the API and Lambda function."""

    code: str = "src/demo_function"
    timeout_seconds: int = 10
    memory_size_mb: int = 128
    ephemeral_storage_size_mb: int = 512
    dead_letter_queue_enabled: bool = True
    log_retention: logs.RetentionDays = logs.RetentionDays.ONE_WEEK
    log_level: str = "DEBUG"
    extra_environment: dict = field(default_factory=lambda: {})


class EnvironmentConfig:
    """
    Configuration for all environments.

    Production is disabled for now because we don't need to deploy docs to production
    """

    development: Config = Config()
    staging: Config = Config(log_level="INFO")
    production: Config = Config(memory_size_mb=256, log_retention=logs.RetentionDays.TWO_MONTHS, log_level="WARNING")
