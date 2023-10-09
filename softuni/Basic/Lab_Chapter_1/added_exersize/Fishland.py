price_skumria = float(input())
price_caca = float(input())
palamud = float(input())
safrid = float(input())
amount_shells = int(input())

PRICE_SHELLS = 7.50 * amount_shells

price_palamud = (price_skumria * 0.60) + price_skumria
total_price_palamud = palamud * price_palamud

price_safrid = (price_caca * 0.80) + price_caca
total_price_safrid = price_safrid * safrid


total_price = PRICE_SHELLS + \
              total_price_palamud + \
              total_price_safrid

print(f"{total_price:.2f}")
