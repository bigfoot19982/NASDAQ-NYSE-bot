import asyncio
import asyncpg
from aiogram import types

from data import config
from keyboards.inline.news import create_button_unsubscribe
from utils.db_api.big_scripts import create_tab_companies, create_tab_users, add_comp, add_user, unsubscribe, \
    check_if_exists, count_comps, delete, all_comps, comp_subscribers, set_hash


class Database:
    # connecting the DB
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                password=config.PGPASSWORD,
                host=config.IP, max_inactive_connection_lifetime=3
            )
        )

    async def create_table_companies(self):
        await self.pool.execute(create_tab_companies)

    async def create_table_users(self):
        await self.pool.execute(create_tab_users)

    async def add_company(self, name: str):
        try:
            await self.pool.execute(add_comp, name)
        except:
            print("The company is in the list already")

    async def add_user(self, id: int, company_name: str, user_name: str, call: types.CallbackQuery):
        num = await self.pool.fetchval(check_if_exists, id, company_name)
        if num > 0:
            await call.message.answer("Вы уже подписаны на новости о данной компании!",
                                      reply_markup=await create_button_unsubscribe(company_name))
            return False
        else:
            await self.pool.execute(add_user, id, company_name, user_name)
            return True

    async def unsubscribe(self, id: int, company: str):
        await self.pool.execute(unsubscribe, id, company)
        num = await self.pool.fetchval(count_comps, company)
        if num == 0:
            await self.pool.execute(delete, company)

    async def set_hash(self, new_hash: str, id: int, company):
        await self.pool.execute(set_hash, new_hash, id, company)

    async def subscribers_of_the_company(self, company: str):
        return await self.pool.fetch(comp_subscribers, company)

    async def all_comps(self):
        return await self.pool.fetch(all_comps)
