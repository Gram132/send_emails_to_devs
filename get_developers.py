from db import get_db
db = get_db()


def get_devs(year):
    # Query documents where Year = 2025
    documents = db.find({"Year": year})
    # Print results
    
    for doc in documents:
        print(doc)

get_devs(2015)