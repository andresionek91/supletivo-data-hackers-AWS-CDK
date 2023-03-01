from dataclasses import dataclass


@dataclass
class Config:
    """Configuration for the API and Lambda function."""

    foo: str = "bar"


class EnvironmentConfig:
    """
    Configuration for all environments.

    Production is disabled for now because we don't need to deploy docs to production
    """

    development: Config = Config()
    staging: Config = Config()
    production: Config = Config()
