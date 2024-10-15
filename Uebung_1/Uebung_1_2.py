import requests

BASE_URL = "https://api.fda.gov/food/enforcement.json?"

def endpuntkSuche():
    foodendpunkt = "search=country:Germany"
    endpunkt = BASE_URL + foodendpunkt
    print("Endpunkt: " + endpunkt)
    respone = requests.get(endpunkt)
    print(respone.text)
    return respone.json()

def endpunktSuche2():
    print("Hallo Welt 2")

if __name__ == '__main__':
    endpuntkSuche()

    endpunktSuche2()