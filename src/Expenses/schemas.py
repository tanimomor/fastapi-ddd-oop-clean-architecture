from pydantic import BaseModel, Field, field_validator
from typing import Optional

from src.Expenses.exceptions import ExpenseCategoryNameRequiredError, ExpenseCategoryCodeRequiredError, \
    InvalidExpenseCategoryIconError


class ExpenseCategoryBaseSchema(BaseModel):
    name: str
    code: str
    type: Optional[str] = Field(None, description="Category type, e.g., 'expense', 'income'")
    icon: Optional[str] = Field(None, description="Icon identifier for the category")
    is_active: Optional[bool] = Field(None, description="Status of the category, where `True` means active and `False` means inactive")

    @field_validator("name", mode="before")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value or len(value.strip()) == 0:
            raise ExpenseCategoryNameRequiredError
        return value

    @field_validator("code", mode="before")
    @classmethod
    def validate_code(cls, value: str) -> str:
        if not value or len(value.strip()) == 0:
            raise ExpenseCategoryCodeRequiredError
        return value

    # @field_validator("type", mode="before")
    # @classmethod
    # def validate_type(cls, value: Optional[str]) -> Optional[str]:
    #     if value and value not in ExpenseCategoryValidationConfig.ALLOWED_TYPES:
    #         raise InvalidExpenseCategoryTypeError
    #     return value

    # @field_validator("icon", mode="before")
    # @classmethod
    # def validate_icon(cls, value: Optional[str]) -> Optional[str]:
    #     if value and not value.startswith("icon-"):
    #         raise InvalidExpenseCategoryIconError
    #     return value

    # @field_validator("status", mode="before")
    # @classmethod
    # def validate_status(cls, value: Optional[str]) -> Optional[str]:
    #     if value and value not in ExpenseCategoryValidationConfig.ALLOWED_STATUSES:
    #         raise InvalidExpenseCategoryStatusError
    #     return value


class CreateExpenseCategorySchema(ExpenseCategoryBaseSchema):
    """
    Schema for creating a new expense category.
    """
    pass


class UpdateExpenseCategorySchema(ExpenseCategoryBaseSchema):
    """
    Schema for updating an existing expense category.
    """
    pass