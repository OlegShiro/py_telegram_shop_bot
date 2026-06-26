from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


base = declarative_base()
__session = None


def create_session(database_path):
    global __session, base

    con_str = f"sqlite:///{database_path}?check_same_thread=False"
    engine = create_engine(con_str, echo=False)
    __session = sessionmaker(engine)
    base.metadata.create_all(engine)

    return con_str


def get_session():
    return None if __session is None else __session()
