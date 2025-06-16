import time
import matplotlib.pyplot as plt
from signal_generator import get_signal

def show_chart(iterations=10, symbol="BINANCE:BTCUSDT"):
    signals = []
    for i in range(iterations):
        signal = get_signal(symbol)
        print(f"Signal {i+1}: {signal}")
        signals.append(1 if signal == "BUY" else -1)
        time.sleep(1)

    plt.plot(signals, marker='o')
    plt.title("Buy/Sell Signal Chart")
    plt.xlabel("Time")
    plt.ylabel("Signal (1=BUY, -1=SELL)")
    plt.grid(True)
    plt.show()

# Test Run
if __name__ == "__main__":
    show_chart()
