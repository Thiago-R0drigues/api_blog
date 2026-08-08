from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = 'posts'

    post_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    post_title: Mapped[str]
    post_description: Mapped[str]

