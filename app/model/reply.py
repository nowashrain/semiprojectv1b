from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.model.base import Base


class Reply(Base):
    __tablename__ = 'reply'

    rno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    reply: Mapped[str] = mapped_column(index=True)
    userid: Mapped[str] = mapped_column(ForeignKey('member.userid'), index=True)
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    bno: Mapped[int] = mapped_column(ForeignKey('board.bno'))
    rpno: Mapped[int] = mapped_column(ForeignKey('reply.rno'))