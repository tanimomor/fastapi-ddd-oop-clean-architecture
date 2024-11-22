from typing import Self

from src.Expenses.adapters.repositories import SQLAlchemyExpenseCategoryRepository
from src.Expenses.interfaces.repositories import ExpenseCategoryRepository
from src.Expenses.interfaces.units_of_work import ExpenseCategoryUnitOfWork
from src.core.database.interfaces.units_of_work import SQLAlchemyAbstractUnitOfWork


class SQLAlchemyExpenseCategoryUnitOfWork(SQLAlchemyAbstractUnitOfWork, ExpenseCategoryUnitOfWork):

    async def __aenter__(self) -> Self:
        uow = await super().__aenter__()
        self.expense_categories: ExpenseCategoryRepository = SQLAlchemyExpenseCategoryRepository(session=self._session)
        return uow
