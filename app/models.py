from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base
Base = declarative_base()

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)  
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    owner_id =Column(Integer, ForeignKey("user.id", ondelete="CASCADE"),nullable=False )

    owner =relationship("User")

class User(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)  # A senha deve ser criptografada
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    phone_number = Column(String)


class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
