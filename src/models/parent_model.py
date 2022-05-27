from sqlalchemy.future import select
from sqlalchemy import update, delete
from sqlalchemy.sql.expression import delete
from src.database.db import db_session_maker


db_session_maker = db_session_maker()


class ParentModel:
    @classmethod
    def create(cls, **kwargs):
        with db_session_maker.begin() as session:
            row_obj = cls(**kwargs)
            session.add(row_obj)
            session.commit()
        return row_obj

    @classmethod
    def update(cls, where_clause, **kwargs):
        update_statement = update(cls)
        for column in where_clause:
            update_statement = update_statement.where(
                getattr(cls, column) == where_clause[column]
            )
        update_statement = update_statement.values(**kwargs).execution_options(
            synchronize_session="fetch"
        )
        with db_session_maker.begin() as session:
            res = session.execute(update_statement)
        return res

    @classmethod
    def get(cls, where_clause):
        select_statement = select(cls)
        for column in where_clause:
            select_statement = select_statement.where(
                getattr(cls, column) == where_clause[column]
            )
        with db_session_maker() as session:
            res = session.execute(
                select_statement, execution_options={"prebuffer_rows": True}
            )
            res = res.scalars()
        return res

    @classmethod
    def fetch_all(cls):
        with db_session_maker() as session:
            res = session.execute(
                select(cls), execution_options={"prebuffer_rows": True}
            )
            res = res.scalars()
        return res

    @classmethod
    def delete(cls, where_clause):
        delete_statement = delete(cls)
        for column in where_clause:
            delete_statement = delete_statement.where(
                getattr(cls, column) == where_clause[column]
            )
        with db_session_maker.begin() as session:
            session.execute(delete_statement)
