from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


# -----------------------
# Admin User
# -----------------------
class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


# -----------------------
# Faculty
# -----------------------
class Faculty(Base):
    __tablename__ = "faculty"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    department = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    designation = Column(String)
    max_workload = Column(Integer, default=20)
    available = Column(Boolean, default=True)


# -----------------------
# Division
# -----------------------
class Division(Base):
    __tablename__ = "divisions"

    id = Column(Integer, primary_key=True, index=True)
    academic_year = Column(String)
    name = Column(String)
    students = Column(Integer)


# -----------------------
# Subject
# -----------------------
class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    subject_code = Column(String)
    name = Column(String)
    academic_year = Column(String)
    division = Column(String)
    faculty = Column(String)
    subject_type = Column(String)
    weekly_limit = Column(Integer)


# -----------------------
# Classroom
# -----------------------
class Classroom(Base):
    __tablename__ = "classrooms"

    id = Column(Integer, primary_key=True, index=True)
    room_no = Column(String)
    capacity = Column(Integer)


# -----------------------
# Laboratory
# -----------------------
class Laboratory(Base):
    __tablename__ = "laboratories"

    id = Column(Integer, primary_key=True, index=True)
    lab_name = Column(String)
    capacity = Column(Integer)


# -----------------------
# Timetable
# -----------------------
class Timetable(Base):
    __tablename__ = "timetable"

    id = Column(Integer, primary_key=True, index=True)

    day = Column(String)
    slot = Column(String)

    division = Column(String)
    subject = Column(String)

    faculty = Column(String)

    room = Column(String)

    session_type = Column(String)
