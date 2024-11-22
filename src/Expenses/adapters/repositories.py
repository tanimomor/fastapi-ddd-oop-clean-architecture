from typing import List, Optional, Sequence, Any
from sqlalchemy import insert, select, delete, update, Result, RowMapping, Row

from src.Expenses.domain.models import ExpenseCategoryModel
from src.Expenses.interfaces.repositories import ExpenseCategoryRepository
from src.core.database.interfaces.repositories import SQLAlchemyAbstractRepository
from src.core.interfaces import AbstractModel


class SQLAlchemyExpenseCategoryRepository(SQLAlchemyAbstractRepository, ExpenseCategoryRepository):

    async def get(self, id: int) -> Optional[ExpenseCategoryModel]:
        """
        Retrieve an expense category by its ID.
        """
        result: Result = await self._session.execute(select(ExpenseCategoryModel).filter_by(id=id))
        return result.scalar_one_or_none()

    async def get_by_code(self, code: str) -> Optional[ExpenseCategoryModel]:
        """
        Retrieve an expense category by its code.
        """
        result: Result = await self._session.execute(select(ExpenseCategoryModel).filter_by(code=code))
        return result.scalar_one_or_none()

    async def add(self, model: AbstractModel) -> ExpenseCategoryModel:
        """
        Add a new expense category to the database.
        """
        result: Result = await self._session.execute(
            insert(ExpenseCategoryModel).values(**await model.to_dict(exclude={'id'})).returning(ExpenseCategoryModel)
        )
        return result.scalar_one()

    async def update(self, id: int, model: AbstractModel) -> ExpenseCategoryModel:
        """
        Update an existing expense category.
        """
        result: Result = await self._session.execute(
            update(ExpenseCategoryModel).filter_by(id=id).values(**await model.to_dict(exclude={'id'})).returning(
                ExpenseCategoryModel)
        )
        return result.scalar_one()

    async def delete(self, id: int) -> None:
        """
        Delete an expense category from the database.
        """
        await self._session.execute(delete(ExpenseCategoryModel).filter_by(id=id))

    async def list(self) -> List[ExpenseCategoryModel]:
        """
        List all expense categories in the database.
        """
        result: Result = await self._session.execute(select(ExpenseCategoryModel))
        expense_categories = result.scalars().all()

        # Asserting that the returned objects are of type `ExpenseCategoryModel`
        assert isinstance(expense_categories, List)
        for category in expense_categories:
            assert isinstance(category, ExpenseCategoryModel)

        return expense_categories