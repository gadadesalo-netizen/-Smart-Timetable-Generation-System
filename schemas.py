from pydantic import BaseModel, EmailStr
from typing import Optional


# -----------------------
# Admin
# -----------------------

class AdminLogin(BaseModel):
    username: str
    password: str


# -----------------------
# Faculty
# -----------------------

class FacultyCreate(BaseModel):
    name: str
    department: str
    email: EmailStr
    phone: str
    designation: str
    max_workload: int


class FacultyResponse(FacultyCreate):
    id: int
    available: bool

    class Config:
        from_attributes = True


# -----------------------
# Subject
# -----------------------

class SubjectCreate(BaseModel):
    subject_code: str
    name: str
    academic_year: str
    division: str
    faculty: str
    subject_type: str
    weekly_limit: int


class SubjectResponse(SubjectCreate):
    id: int

    class Config:
        from_attributes = True


# -----------------------
# Division
# -----------------------

class DivisionCreate(BaseModel):
    academic_year: str
    name: str
    students: int


class DivisionResponse(DivisionCreate):
    id: int

    class Config:
        from_attributes = True


# -----------------------
# Classroom
# -----------------------

class ClassroomCreate(BaseModel):
    room_no: str
    capacity: int


class ClassroomResponse(ClassroomCreate):
    id: int

    class Config:
        from_attributes = True


# -----------------------
# Laboratory
# -----------------------

class LaboratoryCreate(BaseModel):
    lab_name: str
    capacity: int


class LaboratoryResponse(LaboratoryCreate):
    id: int

    class Config:
        from_attributes = True


# -----------------------
# Timetable
# -----------------------

class TimetableResponse(BaseModel):
    id: int
    day: str
    slot: str
    division: str
    subject: str
    faculty: str
    room: str
    session_type: str

    class Config:
        from_attributes = True
