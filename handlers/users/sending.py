import asyncio

from keyboards.inline.news import create_but2
from loader import db, dp
from utils.parsing.news import check_if_news


async def news():
    while True:
        await asyncio.sleep(5)
        set = await db.all_comps()
        for s in set:
            data = await check_if_news(str(s))

            The_Article = data[0]
            new_hash = str(data[1])
            company = data[2].upper()

            subs = await db.subs(company)
            for i in subs:
                i = str(i)
                hash_first = i.find('last_news=') + 10
                hash_last = i.find('>', hash_first)
                last_news = str(i[hash_first:hash_last])

                if last_news == "None" or last_news != new_hash:
                    print(f"{company} : {last_news} : {new_hash}")

                    id_first = i.find('user_id=') + 8
                    id_last = i.find(' ', id_first)
                    cur_id = int(i[id_first:id_last])

                    await dp.bot.send_photo(cur_id, The_Article.pic, caption=
                    f"{The_Article.title}\n"
                    f"\n"
                    f"{The_Article.text}\n"
                    f"{The_Article.link}", reply_markup=await create_but2(company))
                    new_hash = int(new_hash)
                    await db.set_hash(new_hash, cur_id, company)