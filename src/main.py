from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
   
# строка подключения
sqlite_database = "sqlite:///metanit.db"
   
# создаем движок SqlAlchemy
engine = create_engine(sqlite_database)
#создаем базовый класс для моделей
class Base(DeclarativeBase): pass

class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer,)

Base.metadata.create_all(bind=engine)
 
print("Database created")