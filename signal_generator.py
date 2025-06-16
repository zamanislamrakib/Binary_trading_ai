from market_data import get_price

previous_price = None

def get_signal(symbol="BINANCE:BTCUSDT"):
    global previous_price
    current_price = get_price(symbol)

    if previous_price is None:
        previous_price = current_price
        return "HOLD"

    signal = "BUY" if current_price > previous_price else "SELL"
    previous_price = current_price
    return signal

# Test Run
if __name__ == "__main__":
    print(f"📊 Market Signal: {get_signal()}")
