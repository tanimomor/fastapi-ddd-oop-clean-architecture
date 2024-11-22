from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.Expenses.adapters.orm import start_mappers
from src.Expenses.domain.models import ExpenseCategoryModel

# Create the engine manually
DATABASE_URL = "postgresql://postgres:root@localhost:5432/abcd"  # Replace with your DB details
engine = create_engine(DATABASE_URL, echo=True)  # echo=True logs SQL statements

# Start mappers
start_mappers()

# Test query
with Session(engine) as session:
    result = session.query(ExpenseCategoryModel).all()
    print(result)
