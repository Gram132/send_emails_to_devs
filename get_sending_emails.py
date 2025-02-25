from db import get_db

db = get_db()

def get_developers_not_sent():
    """ Retrieve developers with 'is_sent' = False in random order """
    
    query = {"is_sent": False}

    # Use aggregation with $sample to shuffle the order randomly
    documents = db.aggregate([
        {"$match": query},
        {"$sample": {"size": db.count_documents(query)}}  # Shuffle all matching documents
    ])

    return list(documents)

def get_developers_not_sent_in(country):
    """ Retrieve developers with 'is_sent' = False in random order """
    
    query = {"is_sent": False, "location":country}

    # Use aggregation with $sample to shuffle the order randomly
    documents = db.aggregate([
        {"$match": query},
        {"$sample": {"size": db.count_documents(query)}}  # Shuffle all matching documents
    ])

    return list(documents)

get_developers_not_sent_in("Malaysia")

