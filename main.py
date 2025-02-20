from warmup import get_warmup_info, update_warmup_level
from email_sender import process_emails
from scheduler import random_delay
from utils import is_active_hour
from db import get_db
from get_sending_emails import get_developers_not_sent
import os
db = get_db()

EMAIL_ACCOUNT = os.getenv("EMAIL_ACCOUNT")


EMAIL_ACCOUNT = "abdellahgram01@gmail.com"

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
    
    emails_to_send = [{"email":"abdellahgram13@outlook.com" , "username": "ahmed brahim"},
                      {"email":"abdolahwidadi00@gmail.com" , "username":"mhmed brahim"},
                      {"email":"abdellahgram02@outlook.com" , "username": "ahmed brahim"},
                      {"email":"abdellahgram05@gmail.com" , "username": "ahmed brahim"},
                      {"email":"abdellahgram07@gmail.com" , "username": "ahmed brahim"},
                      {"email":"abdellahgram05@gmail.com" , "username": "ahmed brahim"},
                      {"email":"tijobme01@gmail.com" , "username": "TI Jobme"}]
    
    developers_not_sent = get_developers_not_sent()

    process_emails(EMAIL_ACCOUNT, developers_not_sent)
#
    # Update warm-up level
    update_warmup_level(EMAIL_ACCOUNT)

    # Introduce a random delay
    random_delay()

if __name__ == "__main__":
    run_warmup()
