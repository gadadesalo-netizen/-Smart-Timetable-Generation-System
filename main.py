from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from . import models
from . import crud
from . import schemas
from . import auth

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Timetable Generation System",
    version="2.0"
)

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# --------------------------
# Startup
# --------------------------
@app.on_event("startup")
def startup():
    db = next(get_db())
    auth.create_default_admin(db)


# --------------------------
# Home
# --------------------------
@app.get("/")
def home():
    return FileResponse("app/static/login.html")


@app.get("/dashboard")
def dashboard():
    return FileResponse("app/static/dashboard.html")


# --------------------------
# Login
# --------------------------
@app.post("/api/login")
def login(
    admin: schemas.AdminLogin,
    db: Session = Depends(get_db)
):
    user = auth.authenticate(
        db,
        admin.username,
        admin.password
    )

    return {
        "status": "success",
        "message": "Login Successful",
        "username": user.username
    }


# --------------------------
# Change Password
# --------------------------
@app.post("/api/change-password")
def change_password(
    data: dict,
    db: Session = Depends(get_db)
):

    return auth.change_password(
        db,
        data["username"],
        data["old_password"],
        data["new_password"]

    )
# =====================================
# Faculty APIs
# =====================================

@app.get("/api/faculty", response_model=list[schemas.FacultyResponse])
def get_faculty(db: Session = Depends(get_db)):
    return crud.get_all_faculty(db)


@app.post("/api/faculty", response_model=schemas.FacultyResponse)
def add_faculty(
    faculty: schemas.FacultyCreate,
    db: Session = Depends(get_db)
):
    return crud.create_faculty(db, faculty)


@app.put("/api/faculty/{faculty_id}")
def update_faculty(
    faculty_id: int,
    faculty: schemas.FacultyCreate,
    db: Session = Depends(get_db)
):

    data = crud.update_faculty(db, faculty_id, faculty)

    if data is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty Not Found"
        )

    return {
        "message": "Faculty Updated Successfully"
    }


@app.delete("/api/faculty/{faculty_id}")
def delete_faculty(
    faculty_id: int,
    db: Session = Depends(get_db)
):

    status = crud.delete_faculty(db, faculty_id)

    if status is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty Not Found"
        )

    return {
        "message": "Faculty Deleted Successfully"
    }
# =====================================
# Subject APIs
# =====================================

@app.get("/api/subjects", response_model=list[schemas.SubjectResponse])
def get_subjects(db: Session = Depends(get_db)):
    return crud.get_all_subjects(db)


@app.post("/api/subjects", response_model=schemas.SubjectResponse)
def add_subject(
    subject: schemas.SubjectCreate,
    db: Session = Depends(get_db)
):
    return crud.create_subject(db, subject)


# =====================================
# Division APIs
# =====================================

@app.get("/api/divisions", response_model=list[schemas.DivisionResponse])
def get_divisions(db: Session = Depends(get_db)):
    return crud.get_all_divisions(db)


@app.post("/api/divisions", response_model=schemas.DivisionResponse)
def add_division(
    division: schemas.DivisionCreate,
    db: Session = Depends(get_db)
):
    return crud.create_division(db, division)


# =====================================
# Classroom APIs
# =====================================

@app.get("/api/classrooms", response_model=list[schemas.ClassroomResponse])
def get_classrooms(db: Session = Depends(get_db)):
    return crud.get_all_classrooms(db)


@app.post("/api/classrooms", response_model=schemas.ClassroomResponse)
def add_classroom(
    classroom: schemas.ClassroomCreate,
    db: Session = Depends(get_db)
):
    return crud.create_classroom(db, classroom)


# =====================================
# Laboratory APIs
# =====================================

@app.get("/api/laboratories", response_model=list[schemas.LaboratoryResponse])
def get_laboratories(db: Session = Depends(get_db)):
    return crud.get_all_laboratories(db)
@app.post("/api/laboratories", response_model=schemas.LaboratoryResponse)
def add_laboratory(
    laboratory: schemas.LaboratoryCreate,
    db: Session = Depends(get_db)
):
    return crud.create_laboratory(db, laboratory)

# =====================================
# Timetable APIs
# =====================================

@app.get("/api/timetable")
def get_timetable(db: Session = Depends(get_db)):
    return crud.get_timetable(db)



# =====================================
# Dashboard Statistics
# =====================================

@app.get("/api/dashboard")
def dashboard_stats(db: Session = Depends(get_db)):

    return {
        "faculty": len(crud.get_all_faculty(db)),
        "subjects": len(crud.get_all_subjects(db)),
        "divisions": len(crud.get_all_divisions(db)),
        "classrooms": len(crud.get_all_classrooms(db)),
        "laboratories": len(crud.get_all_laboratories(db)),
        "timetable_entries": len(crud.get_timetable(db))
    }


# =====================================
# Health Check
# =====================================

@app.get("/api/health")
def health():
    return {
        "status": "running",
        "application": "Smart Timetable Generation System",
        "version": "2.0"
    }

