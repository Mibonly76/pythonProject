budged = float(input())
amount_video_cards = int(input())
amount_processors = int(input())
amount_ram = int(input())

PRICE_VIDEO_CARDS = 250
PRICE_PROCESSORS = (PRICE_VIDEO_CARDS * amount_video_cards) * 0.35
PRICE_RAM = (PRICE_VIDEO_CARDS * amount_video_cards) * 0.1

total_price = \
    (PRICE_PROCESSORS * amount_processors) + \
    (PRICE_VIDEO_CARDS * amount_video_cards) + \
    (PRICE_RAM * amount_ram)

if amount_video_cards > amount_processors:
    total_price *= 0.85

if budged >= total_price:
    print(f"You have {budged - total_price:.2F} leva left!")
else:
    print(f"Not enough money! You need {total_price - budged:.2F} leva more!")
