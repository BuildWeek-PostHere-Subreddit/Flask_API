def get_subreddit_info(id):
    import sqlite3

    conn = sqlite3.connect('subreddit_db.sqlite3')
    curs = conn.cursor()
    query = f'SELECT name, url FROM subreddit WHERE id = {id};'
    output = curs.execute(query).fetchone()

    return output
