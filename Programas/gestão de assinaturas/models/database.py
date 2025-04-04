from sqlmodel import SQLModel, create_engine
from .model import *

sqlite_file_name = r"Programas\gestão de assinaturas\database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=False)

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)