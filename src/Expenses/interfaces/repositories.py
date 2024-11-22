from typing import Optional, List
from abc import ABC, abstractmethod

from src.Expenses.domain.models import ExpenseCategoryModel
from src.core.interfaces import AbstractRepository, AbstractModel

class ExpenseCategoryRepository(AbstractRepository, ABC):
    """
    Repository for handling operations related to the ExpenseCategory model.
    Follows the repository pattern as part of DDD (Domain-Driven Design).
    """

    @abstractmethod
    async def get(self, id: int) -> Optional[ExpenseCategoryModel]:
        """
        Retrieve an expense category by its ID.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_by_code(self, code: str) -> Optional[ExpenseCategoryModel]:
        """
        Retrieve an expense category by its code.
        """
        raise NotImplementedError

    @abstractmethod
    async def add(self, model: AbstractModel) -> ExpenseCategoryModel:
        """
        Add a new expense category to the database.
        """
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: int, model: AbstractModel) -> ExpenseCategoryModel:
        """
        Update an existing expense category.
        """
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: int) -> None:
        """
        Delete an expense category from the database.
        """
        raise NotImplementedError

    @abstractmethod
    async def list(self) -> List[ExpenseCategoryModel]:
        """
        List all expense categories in the database.
        """
        raise NotImplementedError