import requests

def lastUpdatedGermany():
    BASE_URL = "https://api.fda.gov/food/enforcement.json?"
    foodLastUpdatedGermany = "search=country:Germany"
    endpunkt = BASE_URL + foodLastUpdatedGermany
    print("Endpunkt der genutzt wird: " + endpunkt)

    response = requests.get(endpunkt)
    data = response.json()

    results = data["meta"].get("last_updated")
    print("Der Eintrag für das Land Deutschland, wann das letzte Mal geupdated wurde, als in Deutschland das letzte Mal ein Produkt zurückgerufen wurde: " + results)

def countGermanyOccureny():
    BASE_URL = "https://api.fda.gov/device/510k.json?"
    occurCountry = "count=country_code"
    endpunkt = BASE_URL + occurCountry
    print("Endpunkt der genutzt wird: " + endpunkt)

    response = requests.get(endpunkt)
    data = response.json()

    for item in data['results']:
        if item.get("term") == "DE":
            print("Anzahl wie häufig der Ländercode DE in der API vorkommt: ", item.get("count"))


if __name__ == '__main__':
    lastUpdatedGermany()
    countGermanyOccureny()