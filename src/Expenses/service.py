from typing import List, Optional

from src.Expenses.constants import ErrorDetails
from src.Expenses.domain.models import ExpenseCategoryModel
from src.Expenses.exceptions import ExpenseCategoryAlreadyExistsError, ExpenseCategoryNotFoundError
from src.Expenses.interfaces.units_of_work import ExpenseCategoryUnitOfWork


class ExpenseCategoryService:
    """
    Service layer for managing expense categories, implementing operations on the domain model using a unit of work.
    """

    def __init__(self, uow: ExpenseCategoryUnitOfWork) -> None:
        self._uow: ExpenseCategoryUnitOfWork = uow

    async def create_category(self, category: ExpenseCategoryModel) -> ExpenseCategoryModel:
        async with self._uow as uow:
            # existing_category = await uow.expense_categories.get_by_name(name=category.name)
            # if existing_category:
            #     raise ExpenseCategoryAlreadyExistsError

            category = await uow.expense_categories.add(model=category)
            await uow.commit()
            return category

    async def update_category(self, id: int, category: ExpenseCategoryModel) -> ExpenseCategoryModel:
        async with self._uow as uow:
            existing_category = await uow.expense_categories.get(id=id)
            if not existing_category:
                raise ExpenseCategoryNotFoundError

            updated_category = await uow.expense_categories.update(id=id, model=category)
            await uow.commit()
            return updated_category

    async def delete_category(self, id: int) -> None:
        async with self._uow as uow:
            existing_category = await uow.expense_categories.get(id=id)
            if not existing_category:
                raise ExpenseCategoryNotFoundError

            await uow.expense_categories.delete(id=id)
            await uow.commit()

    async def get_category_by_id(self, id: int) -> ExpenseCategoryModel:
        async with self._uow as uow:
            category = await uow.expense_categories.get(id=id)
            if not category:
                raise ExpenseCategoryNotFoundError

            return category

    async def get_all_categories(self) -> List[ExpenseCategoryModel]:
        async with self._uow as uow:
            categories: List[ExpenseCategoryModel] = await uow.expense_categories.list()
            return categories

    async def get_category_by_name(self, name: str) -> ExpenseCategoryModel:
        async with self._uow as uow:
            category = await uow.expense_categories.get_by_name(name=name)
            if not category:
                raise ExpenseCategoryNotFoundError

            return category

    async def check_category_existence(self, name: Optional[str] = None, id: Optional[int] = None) -> bool:
        if not (name or id):
            raise ValueError(ErrorDetails.CATEGORY_ATTRIBUTE_REQUIRED)

        async with self._uow as uow:
            # if name:
            #     category = await uow.expense_categories.get_by_name(name=name)
            #     if category:
            #         return True

            if id:
                category = await uow.expense_categories.get(id=id)
                if category:
                    return True

        return False
