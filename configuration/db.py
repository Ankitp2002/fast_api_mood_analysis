from tortoise import Tortoise
from apis.reg_model import __models__


async def init_db(db_url):
    await Tortoise.init(
        db_url=db_url,
        modules={'models': [*__models__]}
    )
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
