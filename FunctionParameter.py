def travel():
    print("hello there")
    print("are you excited?")
    
travel()



def travel_to_country(country: str):
    print("hello there")
    print(f"you are going to travel to {country}")
    print("are you excited?")
    
travel_to_country("USA")


def travel_to_country(country: str, name: str):
    print(f"hello {name}")
    print(f"you are going to travel to {country}")
    print("are you excited?")
    
travel_to_country("USA", "chanho")
travel_to_country(country="USA", name="chanho")



def get_name(first_name, last_name):
    return f"{first_name}, {last_name}"

return_value = get_name(first_name=input("your first name?"), last_name=input("your last name?"))

print(return_value)