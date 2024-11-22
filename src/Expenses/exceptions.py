from fastapi import status

from src.Expenses.constants import ErrorDetails
from src.core.exceptions import (
    DetailedHTTPException,
    PreconditionFailedError,
    AlreadyExistsError,
    NotFoundError,
    ValidationError,
    BadRequestError
)


class ExpenseCategoryNotFoundError(NotFoundError):
    DETAIL = ErrorDetails.CATEGORY_NOT_FOUND


class ExpenseCategoryAlreadyExistsError(AlreadyExistsError):
    DETAIL = ErrorDetails.CATEGORY_ALREADY_EXISTS


class ExpenseCategoryCreationFailedError(DetailedHTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = ErrorDetails.CATEGORY_CREATION_FAILED


class ExpenseCategoryUpdateFailedError(DetailedHTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = ErrorDetails.CATEGORY_UPDATE_FAILED


class ExpenseCategoryDeleteFailedError(DetailedHTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = ErrorDetails.CATEGORY_DELETE_FAILED


class InvalidExpenseCategoryIdError(ValidationError):
    DETAIL = ErrorDetails.INVALID_CATEGORY_ID


class ExpenseCategoryNameRequiredError(ValidationError):
    DETAIL = ErrorDetails.CATEGORY_NAME_REQUIRED


class ExpenseCategoryCodeRequiredError(ValidationError):
    DETAIL = ErrorDetails.CATEGORY_CODE_REQUIRED


class InvalidExpenseCategoryTypeError(ValidationError):
    DETAIL = ErrorDetails.CATEGORY_TYPE_INVALID


class InvalidExpenseCategoryIconError(ValidationError):
    DETAIL = ErrorDetails.CATEGORY_ICON_INVALID


class InvalidExpenseCategoryStatusError(ValidationError):
    DETAIL = ErrorDetails.CATEGORY_STATUS_INVALID
