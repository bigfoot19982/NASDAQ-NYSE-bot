async def indexes(first: str, second: str, basic: str, add_to_first: int):
    ind_1 = basic.find(first) + add_to_first
    ind_2 = basic.find(second, ind_1)

    return ind_1, ind_2
