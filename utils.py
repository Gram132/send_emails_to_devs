import datetime

def is_active_hour():
    """ Returns True if within active sending hours (9 AM - 6 PM) """
    now = datetime.datetime.now()
    return 1 <= now.hour <= 24
