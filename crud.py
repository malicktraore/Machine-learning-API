from sqlalchemy.orm import Session

import models, schemas


def get_medecin(db: Session, medecin_id: int):
    return db.query(models.Medecin).filter(models.User.id == medecin_id).first()


#def get_users(db: Session, skip: int = 0, limit: int = 100):
#    return db.query(models.User).offset(skip).limit(limit).all()


def create_medecin(db: Session, medecin: schemas.Medecin):
    #db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db_medecin=models.Medecin(**medecin.dict())
    db.add(db_medecin)
    db.commit()
    db.refresh(db_medecin)
    return db_medecin

def get_medecins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Medecin).offset(skip).limit(limit).all()

def get_specialities(db:Session):
    return db.query(models.Speciality).all()

def get_docs_by_speciality(special_id,db:Session):
    return db.query(models.Medecin).where(models.Medecin.speciality_id==special_id).all()

def get_cabinets(db:Session, skip=0, limit=0):
    return db.query(models.Cabinet).offset(skip).limit(limit).all()