from dataclasses import dataclass


@dataclass
class Config:
    """Configuration for the API and Lambda function."""

    bucket_name: str
    code: str = "src/demo_function"
    timeout_seconds: int = 10
    memory_size: int = 128


class EnvironmentConfig:
    """
    Configuration for all environments.

    Production is disabled for now because we don't need to deploy docs to production
    """

    development: Config = Config(bucket_name="demo-api-development-supletivo-data-hackers-dev")
    staging: Config = Config(bucket_name="demo-api-staging-supletivo-data-hackers-dev")
    production: Config = Config(bucket_name="demo-api-production-supletivo-data-hackers-dev")
