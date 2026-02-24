# GymBot


## Database migration
alembic init -t async migration    //create migration folder and alembic.ini
alembic revision --autogenerate -m "Initial revision"
alembic upgrade head