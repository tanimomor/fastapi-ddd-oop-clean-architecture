from src.core.constants import ErrorDetails as BaseErrorDetails

class ErrorDetails(BaseErrorDetails):
    """
    Error messages related to expense category operations.
    """

    CATEGORY_NOT_FOUND: str = 'Expense category with the provided ID was not found'
    CATEGORY_ALREADY_EXISTS: str = 'An expense category with the provided name or code already exists'
    CATEGORY_CREATION_FAILED: str = 'Failed to create expense category'
    CATEGORY_UPDATE_FAILED: str = 'Failed to update expense category'
    CATEGORY_DELETE_FAILED: str = 'Failed to delete expense category'
    INVALID_CATEGORY_ID: str = 'The provided category ID is invalid'
    CATEGORY_NAME_REQUIRED: str = 'Category name is required'
    CATEGORY_CODE_REQUIRED: str = 'Category code is required'
    CATEGORY_ATTRIBUTE_REQUIRED: str = 'Category code is required'
    CATEGORY_TYPE_INVALID: str = 'Provided category type is invalid'
    CATEGORY_ICON_INVALID: str = 'Provided category icon is invalid'
    CATEGORY_STATUS_INVALID: str = 'Provided category status is invalid'
