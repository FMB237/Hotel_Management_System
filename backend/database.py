from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database URL. It will create a file named 'hostel.db' in the backend folder.
SQLALCHEMY_DATABASE_URL = "sqlite:///./hostel.db"

# check_same_thread=False is required for SQLite to work with FastAPI's async nature
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal is what we will use to interact with the database in our routes
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is what our models will inherit from
Base = declarative_base()

# Dependency: This function will be used in our routes to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()