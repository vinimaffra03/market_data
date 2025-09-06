from crypto_utils import coingecko_data
import json

market_data = coingecko_data()

btc_dominance = market_data["data"]["market_cap_percentage"]["btc"]

market_cap_change = market_data["data"]["market_cap_change_percentage_24h_usd"]

print(f"Market Cap Change 24h : {market_cap_change:.2f}%, Bitcoin dominance : {btc_dominance:.2f}%")

#print(json.dumps(dados, indent=4, ensure_ascii=False))

#print(dados)