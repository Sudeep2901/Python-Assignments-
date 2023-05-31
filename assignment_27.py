import requests
import json

while True:
    print("________________________________")
    print("-------- REST COUNTRIES --------")
    print("________________________________")

    ch = input("Press Enter to Start !")

    if ch == "":
        print("\n* * * * * * FIND COUNTRY * * * * * *")
        name = input("Enter Name of The Country = ")
        result = requests.get(f"https://restcountries.com/v3.1/name/{name}")
        data = result.json()
        name = name.lower().strip()
        c_name = data[0]["name"]["official"]
        print(f"\n~ Official Name of the Country = {c_name}")

        capital = data[0]["capital"][0]
        print(f"\n~ Capital of {c_name} = {capital}")

        currency_list = data[0]["currencies"]
        for k in currency_list:
            k = k

        currency_name = data[0]["currencies"][k]["name"]
        print(f"\n~ Name of Currency  = {currency_name}")

        currency_symbol = data[0]["currencies"][k]["symbol"]
        print(f"\n~ Symbol of Currency = {currency_symbol}")

        lang = data[0]["languages"]
        for k in lang.values():
            k = k
        print(f"\n~ Language Spoke in {c_name} = {k}")

        timezone = data[0]["timezones"][0]
        print(f"\n~ Timezone in {c_name} = {timezone}")

        flag = data[0]["flags"]["png"]
        print(f"\n~ Link For the flag of the Country = {flag}")

        _continue = input("\nEnter Do You Want to [Y/N] = ")
        _continue.lower().strip()
        if _continue == "y":
            continue
        else:
            break

    else:
        print("Enter Valid Choice !")
