num_of_ppl = 3
food_price = [5, 20, 15, 17, 50]


def dutch_Fuction(pplnum: int, priceList: list):
    sum = 0
    for i in priceList:
        sum += i
        
    return sum / pplnum

bill = dutch_Fuction(num_of_ppl, food_price)
print(int(bill))