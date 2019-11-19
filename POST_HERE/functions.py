import pymongo


def get_subreddit_info(array, code):
    """Function written by Matthew that gets subreddit information based on ID numbers"""
    client = pymongo.MongoClient(code)
    db = client.sub2
    data = [db.sub2.find({'sub_id':int(num)})[0] for num in array]
    return(data)
