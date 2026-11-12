import requests

url = "https://api.coingecko.com/api/v3/simple/price"
coin = input("Coin (e.g. bitcoin): ").lower()

params = {
    "ids": coin,
    "vs_currencies": "usd"
}

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    if coin not in data:
        print("Coin not found")
    else:
        price = data[coin]["usd"]
        print(f"{coin.capitalize()} price: ${price:,}")

except requests.exceptions.ConnectionError:
    print("No internet connection")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
except ValueError:
    print("Invalid response from server")