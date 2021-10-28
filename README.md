# NASDAQ-NYSE-bot

Subscribe to the latest news of any american stocks

![](https://img.shields.io/pypi/implementation/aiogram?style=plastic)
![Version](https://img.shields.io/pypi/v/aiogram?style=plastic)
![License](https://img.shields.io/pypi/l/aiogram?style=plastic)
![License](https://img.shields.io/pypi/l/asyncpg?style=plastic)
![last_commit](https://img.shields.io/github/last-commit/bigfoot19982/Selling_Books_Bot?style=plastic)

## Why one might need this telegram bot?
No matter if you're a long term investor or a daily trader,
plunge into company sentiment must be one of the major parts of your due diligence before stock purchase. 
For instance, if a person hadn't got the news that the Chinese leader Xi Jinping has banned paid tutor education in China, 
he would have bought the TAL Education dip and lost a huge part of his money.

On top of that, even if you've bought a stock already you're supposed to follow the news on it
to make sure that the company keeps on progressing. Otherwise, you may buy one of the top S&P 500 stocks and in a decade turn out to be holding a toxic non-profitable asset (AT&T in the beginning of the century and now).

The best way to stay in the loop is to get short corporate news on a daily basis.
This telegram bot provides you with such opportunity.

## How does it work? 

### Concealed from user

On bot startup we create two tables in Postgresql:
1) A table of companies that people are subscribed to. Each company in the table is unique. 
We need the table to repeatedly go through the companies and check for news on the websites dedicated to the stocks.
2) A table of users. If while going through companies we found that there are some news on the stock site,
we go through the users who have subscription to the company and send them the news.

Every 5 seconds the bot checks if there are news on the websites dedicated to the stocks users are subscribed to.

Companies in pgAdmin | Users in pgAdmin
:----------:|:------------:
<img src="https://sun9-79.userapi.com/impg/cT5xjChp2NtSORz9RqwKsAiwxm6tK8ppStvkjw/fEyE2FjpQVA.jpg?size=1315x650&quality=96&sign=448cefc377ae86b84305e2f9f9935bd3&type=album" width="1000"> | <img src="https://sun9-48.userapi.com/impg/fZw7fB0Ar1vWOcjIMnzfIbOMwcAug4NKicg5LA/j5xFPiy97cs.jpg?size=1313x602&quality=96&sign=e91b71bb906dc27d0b49c707ca12e530&type=album" width="1000">

### Interaction with user

When a user starts working with the bot, he is required to type in a ticker of a company he is interested in.

<img src="https://sun9-73.userapi.com/impg/pAJkFUzrvXIfqZ8xogqWTWhpAXMuPxhTrcgeiQ/8fdmrUmS8zU.jpg?size=738x1600&quality=96&sign=534afdb4bb174702be0025b6fecff75e&type=album" width="250">

On receiving the ticker the bot parses stockanalysis.com to get the picture(if present), primary data, and a short description of the stock.
The bot returns the parsed data providing the opportunity to subcribe to the stock news if the user finds the company interesting.

<img src="https://sun9-19.userapi.com/impg/wggrLf-wIrQ7XkESg7jPrBB9gs_v6SbqNGCIzg/keSF9Wh2YvI.jpg?size=738x1600&quality=96&sign=32f3bf3f4fa75c33f37b7637de503838&type=album" width="250"> <img src="https://sun9-64.userapi.com/impg/daKyvKY0YwlPShvtfQO5wQxf9p-IEIuw_nKjlA/wVnsvUEzhjc.jpg?size=738x1600&quality=96&sign=098788a166032b998bcb73c1ef970818&type=album" width="250"> <img src="https://sun1-84.userapi.com/impg/TV3SAI9oAJqzJy3CgVKpi13zheKvhgowPvS7zA/nvfWlkwdSmo.jpg?size=738x1600&quality=96&sign=1c2faea7345adf89b01c2a9dad3d84a3&type=album" width="250">

if the user presses the button, the bot checks if the company is in the table of companies(if not adds it there) and:
1) if user was not subscribed to the stock news notifies the user of the subscription and sends the first news on the stock
2) otherwise merely reminds him of presence of subscription

*For the convenience of user under each news sent there is a button to unsubscribe

The first news 
:------------:
<img src="https://sun9-69.userapi.com/impg/4SokBLXKGEX61RCm5wOUbyMwKDlUZVD43ZElDQ/I9XVr8qEMs8.jpg?size=738x1600&quality=96&sign=b073c82a09597580e7c5d5c7a895dd6e&type=album" width="250"> <img src="https://sun9-83.userapi.com/impg/Btev9ZeoWBwXlZWNzBCyXNaz_7IivAFLiMpk0Q/mzaRRjH-O0g.jpg?size=738x1600&quality=96&sign=057409ee915952e93dd273cd07975b15&type=album" width="250"> <img src="https://sun9-45.userapi.com/impg/btGqt-eJOTnxJUP1y_qPZKuU6LB7CX_TM7Pr5w/s1oMCv5_tu0.jpg?size=738x1600&quality=96&sign=d1bf526009e338763b72d1f0eada5a58&type=album" width="250"> 
