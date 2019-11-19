from decouple import config
import pymongo


def get_subreddit_info(array, code):
    """Function written by Matthew that gets subreddit information based on ID numbers"""
    client = pymongo.MongoClient(code)
    db = client.sfw_db
    data = [db.sfw_db.find({'sub_id':int(num)})[0] for num in array]
    return(data)


def list_subreddits(prediction):
    """Uses the previous function to get the information the FE needs"""
    subreddits = get_subreddit_info(prediction, config('SECRET_CODE'))
    output = []
    for subreddit in subreddits:
        sub_dict = {}
        sub_dict['name'] = subreddit['name']
        sub_dict['url'] = 'https://www.reddit.com' + subreddit['url']
        sub_dict['subscribers'] = subreddit['subscribers']
        sub_dict['active_accounts'] = subreddit['active_accounts']
        sub_dict['score'] = subreddit['score']
        if type(subreddit['description']) is float:
            sub_dict['description'] = 'None'
        else:
            sub_dict['description'] = subreddit['description']
        output.append(sub_dict)
    return output
