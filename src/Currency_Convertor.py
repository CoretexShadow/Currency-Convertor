import requests
import os
from cachetools import cached, TTLCache
cache = TTLCache(maxsize=10000, ttl=86400)
API_KEY = os.environ.get("EXCHANGE_API_KEY")
@cached(cache)
def get_exchange_rate(base_Currency, target_Currency):
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_Currency}'
    if not API_KEY:
        raise ValueError("API key is missing. Set EXCHANGE_API_KEY environment variable.")
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()['conversion_rates'][target_Currency]
def Convert_Currency(amount, exchange_rate):
    return amount * exchange_rate
if __name__ == "__main__":
    user_base = input("Enter base_Currency :  ")
    user_target = input("Enter target_Currency :  ")
    amount = float(input("Enter amount : "))
    exchange_rate = get_exchange_rate(user_base, user_target)
    if exchange_rate:
        converted = Convert_Currency(amount, exchange_rate)
        print(f"\n {amount} {user_base} = {converted:.2f} {user_target}")
    else:
        print("Failed to get exchange rate.")
