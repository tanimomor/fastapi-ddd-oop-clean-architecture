from sqlalchemy import Table, Column, Integer, String, Boolean

from src.Expenses.domain.models import ExpenseCategoryModel
from src.core.database.metadata import mapper_registry

# Define the table
expense_categories_table = Table(
    'expense_categories',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),  # Primary Key
    Column('name', String, nullable=False),  # Required category
    Column('code', String, nullable=False, unique=True),  # Required code
    Column('type', String, nullable=False),  # Required type
    Column('icon', String, nullable=True),  # Optional icon
    Column('is_active', Boolean),  # Boolean flag for active status
)

def start_mappers():
    mapper_registry.map_imperatively(class_=ExpenseCategoryModel, local_table=expense_categories_table)