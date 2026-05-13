from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
import datetime

Base = declarative_base()

class User(Base):

    __tablename__ = "user"

    u_id = Column(Integer, primary_key=True, index=True)
    uname = Column(String)


class Course(Base):

    __tablename__ = "course"

    c_id = Column(Integer, primary_key=True, index=True)
    cname = Column(String)
    description = Column(String)

    resources = relationship("Resource", back_populates="course")

class Resource(Base):

    __tablename__ = "resource"

    r_id = Column(Integer, primary_key=True, index=True)
    c_id = Column(Integer, ForeignKey("course.c_id"))
    title = Column(String)
    file_path = Column(String)
    uploaded_at = Column(DateTime, default=lambda: datetime.datetime.now(datetime.UTC))

    course = relationship("Course", back_populates="resources")

class isEnrolled(Base):

    __tablename__ = "is_enrolled"

    c_id = Column(Integer, ForeignKey("course.c_id"), primary_key=True)
    u_id = Column(Integer, ForeignKey("user.u_id"), primary_key=True)


