from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class BaseDAO:
    model = None

    @classmethod
    async def add(cls, session: AsyncSession, **values):
        new_instance = cls.model(**values)
        session.add(new_instance)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return new_instance
    
    @classmethod
    async def get_one_by_id(cls, session: AsyncSession, id: int):
        query = select(cls.model).where(cls.model.id == id)
        result = await session.execute(query)
        return result.scalar_one_or_none()
    
    @classmethod
    async def getall(cls, session: AsyncSession):
        query = select(cls.model)
        result = await session.execute(query)
        records = result.scalars().all()
        return records
