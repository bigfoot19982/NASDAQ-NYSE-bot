async def form_text(data: list):
    text = (f"{data[0]}\n"
            f"\n"
            f"{data[3]}\n"
            f"\n"
            f"Цена акции {data[1]}$.\n"
            f"Капитализация {data[2][0]}$.\n"
            f"Общая выручка {data[2][1]}$\n"
            f"Чистый доход {data[2][2]}$\n"
            f"P/E равен {data[2][3]} (в норме он меньше 15)\n"
            f"Дивиденды составляют {data[2][4]}\n"
            f"Потенциал роста до {data[2][5]}.\n")

    return text
