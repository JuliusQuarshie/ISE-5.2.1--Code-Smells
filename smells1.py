PRICES = {
    "apple": 1.0,
    "banana": 0.5,
    "cherry": 0.75,
    "mango": 1.0,
    "pineapple": 1.5,
    "dragonfruit": 2.0,
    "durian": 2.75,
}

DISCOUNT_THRESHOLD = 10
DISCOUNT_RATE = 0.10


def get_item_price(item):
    return PRICES.get(item)


def apply_discount(total):
    if total >= DISCOUNT_THRESHOLD:
        return total * (1 - DISCOUNT_RATE)
    return total


def calculate_total_price(items):
    total = 0

    for item in items:
        price = get_item_price(item)

        if price is None:
            print("Unknown item: " + item)
        else:
            total += price

    return apply_discount(total)


if __name__ == "__main__":
    print("run `pytest tests/smells1_test.py` instead.")