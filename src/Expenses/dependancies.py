from typing import List
from fastapi import Depends

from src.Expenses.domain.models import ExpenseCategoryModel
from src.Expenses.exceptions import ExpenseCategoryAlreadyExistsError
from src.Expenses.schemas import CreateExpenseCategorySchema
from src.Expenses.service import ExpenseCategoryService
from src.Expenses.units_of_work import SQLAlchemyExpenseCategoryUnitOfWork



async def get_all_expense_categories() -> List[ExpenseCategoryModel]:
    service: ExpenseCategoryService = ExpenseCategoryService(uow=SQLAlchemyExpenseCategoryUnitOfWork())
    categories: List[ExpenseCategoryModel] = await service.get_all_categories()
    return categories


async def create_expense_category(data: CreateExpenseCategorySchema) -> ExpenseCategoryModel:

    service: ExpenseCategoryService = ExpenseCategoryService(uow=SQLAlchemyExpenseCategoryUnitOfWork())
    if await service.check_category_existence(name=data.name):
        raise ExpenseCategoryAlreadyExistsError

    print("###############")
    print(data)
    print("")

    category: ExpenseCategoryModel = ExpenseCategoryModel(**data.model_dump())
    return await service.create_category(category=category)
#
#
# async def get_expense_category_by_id(category_id: int) -> ExpenseCategoryModel:
#     service: ExpenseCategoryService = ExpenseCategoryService(uow=SQLAlchemyExpenseCategoryUnitOfWork())
#     category: ExpenseCategoryModel = await service.get_category_by_id(category_id=category_id)
#     if not category:
#         raise ExpenseCategoryNotFoundError
#
#     return category
#
#
# async def update_expense_category(
#     category_id: int, data: UpdateExpenseCategorySchema
# ) -> ExpenseCategoryModel:
#     service: ExpenseCategoryService = ExpenseCategoryService(uow=SQLAlchemyExpenseCategoryUnitOfWork())
#     category: ExpenseCategoryModel = await service.update_category(category_id=category_id, data=data)
#     if not category:
#         raise ExpenseCategoryNotFoundError
#
#     return category
#
#
# async def delete_expense_category(category_id: int) -> None:
#     service: ExpenseCategoryService = ExpenseCategoryService(uow=SQLAlchemyExpenseCategoryUnitOfWork())
#     if not await service.delete_category(category_id=category_id):
#         raise ExpenseCategoryNotFoundError

