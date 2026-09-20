from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Exercise, MuscleGroup


router = APIRouter(
    prefix="/catalog",
    tags=["catalog"],
)


@router.get("/muscle-groups")
def get_muscle_groups(db: Session = Depends(get_db)):
    return db.query(MuscleGroup).order_by(MuscleGroup.name).all()


@router.get("/exercises")
def get_exercises(db: Session = Depends(get_db)):
    return db.query(Exercise).order_by(Exercise.name).all()