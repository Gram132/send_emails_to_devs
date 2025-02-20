import time
import random

def random_delay():
    """ Introduces a random delay between 15 mins and 1 hour """
    delay = random.randint(900, 3600)  # 15 minutes to 1 hour
    print(f"Sleeping for {delay / 60} minutes...")
    time.sleep(delay)
