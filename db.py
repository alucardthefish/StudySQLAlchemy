from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, update


Base = declarative_base()

# Database connection
database = "test.db"
engine = create_engine(f'sqlite:///{database}', connect_args={'timeout': 30})  # Use your database connection string
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
