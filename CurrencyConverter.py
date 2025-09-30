def usd_to_eur(usd):
    return usd * 0.90   
def usd_to_gbp(usd):
    return usd * 0.80   # example rate
def usd_to_inr(usd):
    return usd * 83.00  # example rate
def main():
    print("Currency Converter")
    print("Available conversions: EUR, GBP, INR")
    try:
        usd = float(input("Enter amount in USD: "))
        currency = input("Convert to (EUR/GBP/INR): ").upper()
        if currency == "EUR":
            print(f"${usd} = €{usd_to_eur(usd):.2f}")
        elif currency == "GBP":
            print(f"${usd} = £{usd_to_gbp(usd):.2f}")
        elif currency == "INR":
            print(f"${usd} = ₹{usd_to_inr(usd):.2f}")
        else:
            print("Unsupported currency.")
    except ValueError:
        print("lease enter a valid number.")
if __name__ == "__main__":
    main()
