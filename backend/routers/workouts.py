from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import  Exercise, MuscleGroup, Workout, WorkoutExercise, WorkoutMuscleGroup
from schemas import WorkoutCreate


router = APIRouter(
    prefix="/workouts",
    tags=["workouts"],
)


@router.get("/")
def get_workouts(db: Session = Depends(get_db)):
    return db.query(Workout).order_by(Workout.id).all()

@router.post("/")
def create_workout(
    workout_data: WorkoutCreate,
    db: Session = Depends(get_db),
):
    workout = Workout(name=workout_data.name)

    db.add(workout)
    db.flush()

    for item in workout_data.items:
        if item.type == "muscle_group":
            muscle_group = db.get(MuscleGroup, item.id)

            if not muscle_group:
                raise HTTPException(
                    status_code=404,
                    detail=f"Muscle group {item.id} not found",
                )

            workout_muscle_group = WorkoutMuscleGroup(
                workout_id=workout.id,
                muscle_group_id=item.id,
                rank=item.rank,
            )

            db.add(workout_muscle_group)

        elif item.type == "exercise":
            exercise = db.get(Exercise, item.id)

            if not exercise:
                raise HTTPException(
                    status_code=404,
                    detail=f"Exercise {item.id} not found",
                )

            workout_exercise = WorkoutExercise(
                workout_id=workout.id,
                exercise_id=item.id,
                rank=item.rank,
            )

            db.add(workout_exercise)

    db.commit()
    db.refresh(workout)

    return workout