print("📈 Binary Trading AI Started...")

# Basic structure
def get_signal():
    return "BUY"  # or "SELL"

for i in range(5):
    signal = get_signal()
    print(f"Signal {i+1}: {signal}")
