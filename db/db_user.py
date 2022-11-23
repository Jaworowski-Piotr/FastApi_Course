from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash
from fastapi import HTTPException, status


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_user(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, id: int):
    if user := db.query(DbUser).filter(DbUser.id == id).first():
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with ID {id} not found')


def update_user(db: Session, id_: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id_)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'OK'


def delete_user(db: Session, id_: int):
    user = db.query(DbUser).filter(DbUser.id == id_).first()
    db.delete(user)
    db.commit()
    return "Deleted"
