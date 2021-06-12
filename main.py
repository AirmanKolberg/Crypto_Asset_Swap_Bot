from secrets import *
from data_retrieval import get_current_time, get_crypto_price
from time import sleep
from system_commands import clear_screen


# This function is called from within check_for_updates()
def compare_values(sell_coin_price, buy_coin_price,
                   total_coin_to_sell):

    # Determine sell price to fiat money
    fiat = sell_coin_price * total_coin_to_sell

    # Determine fiat back to coin to buy
    coins_to_get = int(fiat / buy_coin_price)

    return coins_to_get


# Compares the two coins in question
def check_for_update(sell_coin, buy_coin, sell_amount):

    time_now = get_current_time()
    sell_coin_price = get_crypto_price(sell_coin)
    buy_coin_price = get_crypto_price(buy_coin)

    new_assets = compare_values(sell_coin_price, buy_coin_price,
                                sell_amount)

    return new_assets, time_now


if __name__ == '__main__':

    clear_screen()

    potential_rewards, time_now = check_for_update(sell_coin, buy_coin,
                                                   sell_amount)
    print(f"Potential rewards at {time_now}  -  {potential_rewards}")

    if potential_rewards >= coin_rewards:

