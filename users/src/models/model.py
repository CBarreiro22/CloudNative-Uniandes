import os
from datetime import datetime

from dotenv import load_dotenv
from sqlalchemy import Column, DateTime, create_engine, String
from sqlalchemy.orm import declarative_base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import scoped_session, sessionmaker

# Load environment variables from the .env.development file
loaded = load_dotenv('.env.development')

# Create a SQLAlchemy engine using environment variables for database connection
engine = create_engine(os.environ['DATABASE_URL'])

# Create a scoped database session
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Create a base class for declarative models
Base = declarative_base()
Base.query = db_session.query_property()


# Initialize the database schema
def init_db():
    print("Voy a inicializar con engine")
    Base.metadata.create_all(bind=engine)


# Define a base class for models with common attributes

class Model(Base):
    __abstract__ = True

    # Common attributes for all models
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self):
        # Set the creation and update timestamps
        self.createdAt = datetime.utcnow()
        self.updatedAt = datetime.utcnow()

