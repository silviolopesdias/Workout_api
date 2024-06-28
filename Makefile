run:
    @uvicorn workout_api.main:app --reload
    
create-migrations:
    @PYTHOONPATH=$PYTHOONPATH:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
    @PYTHOONPATH=$PYTHOONPATH:$(pwd) alembic upgrade head
 