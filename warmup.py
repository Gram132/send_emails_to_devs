from db import get_db

db = get_db()

# Warm-up levels
LEVELS = {
    1: {"emails_per_day": 5, "days": 7},
    2: {"emails_per_day": 8, "days": 7},
    3: {"emails_per_day": 12, "days": 7},
    4: {"emails_per_day": 20, "days": 7},
    5: {"emails_per_day": 30, "days": float('inf')}  # Continuous sending
}

def get_warmup_info(email_account):
    """ Fetch current level info for an email account. """
    account = db.find_one({"email_account": email_account})
    if not account:
        db.insert_one({
            "email_account": email_account,
            "current_level": 1,
            "emails_sent_today": 0,
            "emails_limit": LEVELS[1]["emails_per_day"],
            "days_left": LEVELS[1]["days"]
        })
        return get_warmup_info(email_account)
    return account

def update_warmup_level(email_account):
    """ Updates the warm-up level based on emails sent. """
    account = get_warmup_info(email_account)
    if account["emails_sent_today"] >= account["emails_limit"]:
        db.update_one({"email_account": email_account}, {"$inc": {"days_left": -1}, "$set": {"emails_sent_today": 0}})
    
    if account["days_left"] == 0:
        new_level = account["current_level"] + 1
        if new_level in LEVELS:
            db.update_one(
                {"email_account": email_account},
                {"$set": {"current_level": new_level, "emails_limit": LEVELS[new_level]["emails_per_day"], "days_left": LEVELS[new_level]["days"], "emails_sent_today": 0}}
            )
