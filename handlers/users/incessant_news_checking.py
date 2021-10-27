import asyncio

from handlers.users.supplementary.get_indexes import indexes
from keyboards.inline.news import create_button_unsubscribe
from loader import db, dp
from utils.parsing.get_news_from_site import check_on_company_site, new_article


# from time to time pics in telegram cannot be sent
# the best solution is to add a parameter to them
async def form_peculiar_pic(pic: str):
    pic += '?random=58'
    return pic


# the func to send pictures that we need not to double the code on 50-54 lines
# while trying to send picture without the parameter and with it
async def send_news(company: str, new_hash: str, cur_id: int, pic: str, The_Article: new_article):
    await dp.bot.send_photo(cur_id, pic, caption=
    f"{The_Article.title}\n"
    f"\n"
    f"{The_Article.text}\n"
    f"\n"
    f"{The_Article.link}", reply_markup=await create_button_unsubscribe(company))

    # afterwards we set new hash, not to send this news next time
    await db.set_hash(new_hash, cur_id, company)

# a func to constantly check for the stocks news
async def checking_for_news():
    while True:
        # sleep some time before another iteration
        await asyncio.sleep(20)
        # from the DB get all companies people subscribed to
        set_of_companies = await db.all_comps()

        for s in set_of_companies:
            # parse last news from site
            data = await check_on_company_site(str(s))

            The_Article = data[0]
            new_hash = str(data[1])
            company = data[2].upper()

            # collect all subscribers to the company news
            set_of_subs = await db.subscribers_of_the_company(company)
            for i in set_of_subs:
                i = str(i)
                positions_of_last_hash = await indexes('last_news=', '\'', i, 11)
                last_news = str(i[positions_of_last_hash[0]:positions_of_last_hash[1]])

                # check if the last hash is not the same as the current one
                if last_news != new_hash:
                    print(f"{company} : {last_news} : {new_hash}")
                    # getting the user id
                    positions_in_user = await indexes('user_id=', ' ', i, 8)
                    cur_id = int(i[positions_in_user[0]:positions_in_user[1]])

                    try:
                        # try sending news with a pic with no parameter
                        await send_news(company, new_hash, cur_id, The_Article.pic,
                                        The_Article)
                    except:
                        # try sending news with a pic with a special parameter
                        await send_news(company, new_hash, cur_id, await form_peculiar_pic(The_Article.pic),
                                        The_Article)
