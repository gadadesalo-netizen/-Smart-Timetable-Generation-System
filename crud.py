from sqlalchemy.orm import Session
from . import models


# ==========================
# FACULTY CRUD
# ==========================

def get_all_faculty(db: Session):
    return db.query(models.Faculty).all()


def get_faculty(db: Session, faculty_id: int):
    return db.query(models.Faculty).filter(
        models.Faculty.id == faculty_id
    ).first()


def create_faculty(db: Session, faculty):
    obj = models.Faculty(
        name=faculty.name,
        department=faculty.department,
        email=faculty.email,
        phone=faculty.phone,
        designation=faculty.designation,
        max_workload=faculty.max_workload,
        available=True
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj


def update_faculty(db: Session, faculty_id: int, data):
    faculty = get_faculty(db, faculty_id)

    if faculty is None:
        return None

    faculty.name = data.name
    faculty.department = data.department
    faculty.email = data.email
    faculty.phone = data.phone
    faculty.designation = data.designation
    faculty.max_workload = data.max_workload

    db.commit()
    db.refresh(faculty)

    return faculty


def delete_faculty(db: Session, faculty_id: int):
    faculty = get_faculty(db, faculty_id)

    if faculty is None:
        return None

    db.delete(faculty)
    db.commit()

    return True


# ==========================
# SUBJECT CRUD
# ==========================

def get_all_subjects(db: Session):
    return db.query(models.Subject).all()


def create_subject(db: Session, subject):
    obj = models.Subject(
        subject_code=subject.subject_code,
        name=subject.name,
        academic_year=subject.academic_year,
        division=subject.division,
        faculty=subject.faculty,
        subject_type=subject.subject_type,
        weekly_limit=subject.weekly_limit
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj


# ==========================
# DIVISION CRUD
# ==========================

def get_all_divisions(db: Session):
    return db.query(models.Division).all()


def create_division(db: Session, division):
    obj = models.Division(
        academic_year=division.academic_year,
        name=division.name,
        students=division.students
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj


# ==========================
# CLASSROOM CRUD
# ==========================

def get_all_classrooms(db: Session):
    return db.query(models.Classroom).all()


def create_classroom(db: Session, room):
    obj = models.Classroom(
        room_no=room.room_no,
        capacity=room.capacity
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj


# ==========================
# LAB CRUD
# ==========================

def get_all_laboratories(db: Session):
    return db.query(models.Laboratory).all()


def create_laboratory(db: Session, lab):
    obj = models.Laboratory(
        lab_name=lab.lab_name,
        capacity=lab.capacity
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj


# ==========================
# TIMETABLE
# ==========================

def get_timetable(db: Session):
    return db.query(models.Timetable).all()
