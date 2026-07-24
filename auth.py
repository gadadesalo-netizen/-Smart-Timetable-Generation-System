from sqlalchemy.orm import Session
from fastapi import HTTPException
from .models import Admin


# ----------------------------
# Default Admin Credentials
# ----------------------------
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin123"


def create_default_admin(db: Session):
    """
    Create a default admin account if one doesn't exist.
    """
    admin = db.query(Admin).filter(Admin.username == DEFAULT_USERNAME).first()

    if admin is None:
        admin = Admin(
            username=DEFAULT_USERNAME,
            password=DEFAULT_PASSWORD
        )

        db.add(admin)
        db.commit()
        db.refresh(admin)

    return admin


def authenticate(db: Session, username: str, password: str):
    """
    Authenticate admin user.
    """

    admin = db.query(Admin).filter(
        Admin.username == username
    ).first()

    if admin is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Username"
        )

    if admin.password != password:
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    return admin


def change_password(
    db: Session,
    username: str,
    old_password: str,
    new_password: str
):
    admin = authenticate(db, username, old_password)

    admin.password = new_password

    db.commit()

    return {
        "message": "Password Changed Successfully"
    }
