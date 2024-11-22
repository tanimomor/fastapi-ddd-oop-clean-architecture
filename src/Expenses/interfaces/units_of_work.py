from abc import ABC

from src.Expenses.interfaces.repositories import ExpenseCategoryRepository
from src.core.interfaces import AbstractUnitOfWork


class ExpenseCategoryUnitOfWork(AbstractUnitOfWork, ABC):
    """
    An interface for working with expense categories, used by the service layer.
    The main goal is to encapsulate database operations related to expense categories
    and enable seamless replacement via dependency injection.
    """

    expense_categories: ExpenseCategoryRepository