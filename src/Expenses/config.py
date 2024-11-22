from dataclasses import dataclass
from typing import Tuple, Literal
from pydantic_settings import BaseSettings
from src.config import RouterConfig as BaseRouterConfig

@dataclass(frozen=True)
class URLPathsConfig:
    CREATE: str = '/expense-categories'
    GET: str = '/expense-categories/{category_id}'
    UPDATE: str = '/expense-categories/{category_id}'
    DELETE: str = '/expense-categories/{category_id}'
    LIST: str = '/expense-categories'

@dataclass(frozen=True)
class URLNamesConfig:
    CREATE: str = 'expense__categories'
    GET: str = 'expense-categories__category_id}'
    UPDATE: str = 'expense-categories__category_id}'
    DELETE: str = 'expense-categories__category_id}'
    LIST: str = 'expense-categories'

@dataclass(frozen=True)
class RouterConfig(BaseRouterConfig):
    PREFIX: str = '/expense-categories'
    TAGS: Tuple[str] = ('expense_categories', )