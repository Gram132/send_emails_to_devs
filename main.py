from warmup import get_warmup_info, update_warmup_level
from email_sender import process_emails
from scheduler import random_delay
from utils import is_active_hour
from db import get_db
from get_sending_emails import get_developers_not_sent , get_developers_not_sent_in
import os

db = get_db()

EMAIL_ACCOUNT = os.getenv("EMAIL_ACCOUNT")
SEND_TO =os.getenv("SEND_TO")

def run_warmup():
    """ Runs the warm-up email automation process """
    if not is_active_hour():
        print("Outside active hours, skipping...")
        return

    account = get_warmup_info(EMAIL_ACCOUNT)
    if account["emails_sent_today"] >= account["emails_limit"]:
        print("Email limit reached for today. Waiting for the next day...")
        return
    
    # Fetch emails from DB (replace with your method)
    
    emails_to_send = [{"emails":["abdellahgram13@outlook.com"] , "username": "ahmed brahim"},
                      {"emails":["abdolahwidadi00@gmail.com" ] , "username": "mhmed brahim"},
                      {"emails":["abdellahgram02@outlook.com"] , "username": "ahmed brahim"},
                      {"emails":["abdellahgram05@gmail.com"  ] , "username": "ahmed brahim"},
                      {"emails":["abdellahgram07@gmail.com"  ] , "username": "ahmed brahim"},
                      {"emails":["abdellahgram05@gmail.com"  ] , "username": "ahmed brahim"},
                      {"emails":["tijobme01@gmail.com"       ] , "username": "TI Jobme"    }]
    if SEND_TO == "everybody":
        developers_not_sent = get_developers_not_sent()
    else:
        developers_not_sent = get_developers_not_sent_in("Malaysia")

    for email in developers_not_sent:
        print(f"Location : {email['location']} Email : {email['emails'][0]}")

    #process_emails(EMAIL_ACCOUNT, developers_not_sent)
#
    # Update warm-up level
    #update_warmup_level(EMAIL_ACCOUNT)

    # Introduce a random delay
    #random_delay()

if __name__ == "__main__":
    run_warmup()
