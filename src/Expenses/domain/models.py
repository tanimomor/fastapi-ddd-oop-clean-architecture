from dataclasses import dataclass

from src.core.interfaces import AbstractModel

@dataclass
class ExpenseCategoryModel(AbstractModel):
    name: str
    code: str
    type: str
    icon: str = None  # Optional icon
    is_active: bool = True  # Default is_active to True

    # Optional args:
    id: int = 0