from sqlalchemy import insert, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.operators import and_

from app.model.member import Member


class MemberService:
    @staticmethod
    def insert_member(db, member):
        try:
            stmt = insert(Member).values(
                userid=member.userid, passwd=member.passwd,
                name=member.name, email=member.email)
            result = db.execute(stmt)
            db.flush()
            db.commit()
            return result

        except SQLAlchemyError as ex:
            print(f'▶▶▶ insert_member 오류발생: {str(ex)}')
            db.rollback()

    @staticmethod
    def login_member(db,data):
        try:
            find_login = and_(Member.userid == data.get('userid'),
                              Member.passwd == data.get('passwd'))
            stmt = select(Member.userid).where(find_login)
            result = db.execute(stmt).scalars().first()

            return result

        except SQLAlchemyError as ex:
            print(f'▶▶▶ login_member 오류 발생 : {str(ex)} ')


