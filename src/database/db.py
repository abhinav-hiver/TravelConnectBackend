from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from src.config import env


def get_conn_str(user, password, host, port=3306, db=""):
    conn_str = (
        "mysql://"
        + str(user)
        + ":"
        + str(password)
        + "@"
        + str(host)
        + ":"
        + str(port)
        + "/"
        + db
        + "?charset=utf8mb4"
    )

    return conn_str


def create_db_conn(db_uri):
    """
    Function will retur session and engine for specific db uri \n
    :param db_uri: format : "mysql://user:password@host/dbname?charset=utf8" \n
    :return session,engine
    """
    # Change to env.app_debug. Remove before prod
    engine = create_engine(db_uri, pool_recycle=3600, echo=env.APP_DEBUG or True)

    session_maker = sessionmaker(autocommit=True, bind=engine)
    session = scoped_session(session_maker)

    return session, session_maker


def get_db():
    return create_db_conn(
        get_conn_str(
            env.DATABASE_USER,
            env.DATABASE_PASSWORD,
            env.DATABASE_HOST,
            env.DATABASE_PORT,
            env.DATABASE_NAME,
        )
    )


def db_session():
    session, session_maker = get_db()
    return session


def db_session_maker():
    session, session_maker = get_db()
    return session_maker
