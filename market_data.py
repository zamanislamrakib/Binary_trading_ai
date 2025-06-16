import requests

API_KEY = "d17iikpr01qtc1t8jr3gd17iikpr01qtc1t8jr40"
BASE_URL = "https://finnhub.io/api/v1"

def get_price(symbol="BINANCE:BTCUSDT"):
    url = f"{BASE_URL}/quote?symbol={symbol}&token={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["c"]  # current price

# Test Run
if __name__ == "__main__":
    price = get_price()
    print(f"📈 Current BTC Price: ${price}")
