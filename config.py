import os

# MongoDB Configuration
MONGO_URI =  os.getenv("MONGO_URI")

DB_NAME= os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
COLLECTION_NAME2 = os.getenv("COLLECTION_NAME2")


#gmail_app_password = "dyzx vbvr aaor oqyg"
#gmail_account_email = "tijobme01@gmail.com"

gmail_app_password = os.getenv("gmail_app_password")
gmail_account_email = os.getenv("gmail_account_email")

# Email Configuration (use environment variables for security)
EMAIL_USER = gmail_account_email
EMAIL_PASSWORD = gmail_app_password 
