from pathlib import Path

from fastapi_startkit import Application
from fastapi_startkit.logging import LogProvider
from config.app import AppConfig
from config.logging import LoggingConfig
from fastapi_startkit.masoniteorm import DatabaseProvider
from config.database import DatabaseConfig
from config.fastapi import FastAPIConfig
from providers.fastapi_provider import FastapiProvider
from fastapi_startkit.inertia import InertiaProvider
from fastapi_startkit.vite import ViteProvider
from config.vite import ViteConfig

app = Application(
    base_path=Path(__file__).resolve().parent.parent,
    config=AppConfig,
    providers=[
        (LogProvider, LoggingConfig),
        (DatabaseProvider, DatabaseConfig),
        (FastapiProvider, FastAPIConfig),
        (ViteProvider, ViteConfig),
        InertiaProvider,
    ],
)
