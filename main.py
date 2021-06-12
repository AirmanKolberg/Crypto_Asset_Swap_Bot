from secrets import *
from data_retrieval import get_current_time, get_crypto_price
from time import sleep
from system_commands import clear_screen, bash_command
# from twilio import *
import pyautogui as pag


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

    # Insert the currency of your choice
    sell_coin_price = get_crypto_price(sell_coin, 'USD')
    buy_coin_price = get_crypto_price(buy_coin, 'USD')

    new_assets = compare_values(sell_coin_price, buy_coin_price,
                                sell_amount)

    return new_assets, time_now


def run_the_bot():
    try:
        clear_screen()

        waiting_for_opportunity = True
        while waiting_for_opportunity:

            # Crunch all of the numbers
            potential_rewards, time_now = check_for_update(sell_coin, buy_coin,
                                                           sell_amount)

            # Display the current progress on the screen
            print(f"{time_now}  -  {potential_rewards}")

            # If the price is right, notify me
            if potential_rewards >= coin_rewards:
                # text_me(f"Hello, there!\nPotential coin trade of {potential_rewards} right now!")
                # call_me()

                """
                This will serve as a test until I can get Twilio
                back up and running again...
                """

                # Open the Messages app
                bash_command("open -a 'Messages'")
                sleep(5)

                # Type a message to me (from myself, if not using Twilio)
                pag.write(f"Potential coin trade of {potential_rewards} right now!",
                          interval=0.8)
                sleep(0.2)

                # Send the message
                pag.press('return')
                sleep(0.2)

                # Close the Messages application
                pag.hotkey('command', 'q')

                waiting_for_opportunity = False

            # Wait a minute and try again
            sleep(60)
    except Exception:
        run_the_bot()


if __name__ == '__main__':

    run_the_bot()
