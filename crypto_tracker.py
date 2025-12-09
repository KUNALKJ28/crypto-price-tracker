import requests

coin = input("Enter cryptocurrency (e.g., bitcoin, ethereum, dogecoin): ").lower()

url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=inr,usd"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if coin in data:
        price_inr = data[coin].get("inr", "Not available")
        price_usd = data[coin].get("usd", "Not available")

        print(f"\n⭐ Live Price for {coin.capitalize()}:")
        print(f"INR: ₹{price_inr}")
        print(f"USD: ${price_usd}")
    else:
        print("❌ Invalid coin name. Please try again.")
else:
    print("❌ Failed to fetch data from API.")

# Optional logging (very good for resume)
with open("crypto_logs.txt", "a") as f:
    f.write(f"{coin} | status: {response.status_code}\n")
