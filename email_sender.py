import smtplib
import random
from email.mime.text import MIMEText
from config import EMAIL_USER, EMAIL_PASSWORD
from db import get_db

db = get_db()

def send_email(to_email, subject, body):
    """ Sends an email via SMTP """
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = to_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


email_templates = [
    {
        "subject": "Remote Freelance Developer Role – Work from Anywhere",
        "body": "Dear {username},\n\n"
                "I hope you're doing well! I came across your profile and wanted to share a freelance remote opportunity that could be a great fit for you.\n\n"
                "A company is currently looking for skilled developers to work on exciting projects remotely. If you’re open to freelance work, this could be a great way to gain experience and earn from anywhere.\n\n"
                "Would you be interested in learning more? Let me know, and I’ll send over the details!\n\n"
                "Looking forward to your response.\n\n"
                "Best regards,\n"
                "Abdellah Gram\n"  
                "{email_account}\n"
    },
    {
        "subject": "Freelance Developer Role – Fully Remote",
        "body": "Hi {username},\n\n"
                "I wanted to reach out because I found your profile and thought you might be a great fit for a remote freelance developer role.\n\n"
                "This opportunity allows you to work from anywhere, take on flexible projects, and collaborate with great teams. It’s perfect for developers who want freelance work with the freedom to manage their own time.\n\n"
                "Would you like me to share more details? Let me know, and I’ll send over the information!\n\n"
                "Best regards,\n"
                "Abdellah Gram\n"
                "{email_account}\n"
    },
    {
        "subject": "Work from Anywhere – Remote Freelance Developer Jobs",
        "body": "Hi {username},\n\n"
                "I hope you're having a great day! I wanted to let you know about freelance developer roles that are fully remote and flexible.\n\n"
                "These projects allow you to work from anywhere while building your experience and earning on your own schedule. If you're looking for freelance work, this could be a great opportunity!\n\n"
                "Would you be interested in hearing more? Let me know, and I’ll send over the details.\n\n"
                "Looking forward to connecting!\n\n"
                "Best regards,\n"
                "Abdellah Gram\n"
                "{email_account}\n"
    }
]

def process_emails(email_account, emails_list):
    """ Sends emails with a random template for each recipient """
    account = db.find_one({"email_account": email_account})
    if not account:
        print("No account found")
        return

    emails_sent = account["emails_sent_today"]
    emails_limit = account["emails_limit"]

    for email in emails_list:
        if emails_sent >= emails_limit:
            break
        
        # Select a random template
        template = random.choice(email_templates)

        email_username = email['username']
        subject = template["subject"]
        body = template["body"].format(username=email_username , email_account= email_account)

        success = send_email(email['emails'][0], subject, body)
        if success:
            emails_sent += 1
            db.update_one({"email_account": email_account}, {"$inc": {"emails_sent_today": 1}})
            # Update is_sent to True for the email
            db.update_one({"_id": email["_id"]}, {"$set": {"is_sent": True}})

    print(f"Sent {emails_sent} emails today.")
