import sqlite3
import datetime
from basketball_reference_web_scraper import client

def get_connection():
    conn = None
    try: 
        conn = sqlite3.connect("var/sports_analytics.sqlite3")
    except Error as e:
        print(e)
    return conn



start_date = datetime.date(2019, 10, 22)
end_date = datetime.date(2020, 3, 11)
delta = datetime.timedelta(days=1)

# while start_date <= end_date:
#     start_date += delta

play_box_score = client.players_season_totals(season_end_year=2019)

for key in play_box_score: 
    if key["name"] == 'LeBron James':
        conn = get_connection()
        cur = conn.cursor() 
        print(key["name"])
        tup = (1, key['name'], key['points'], int(key['assists']), int(key['defensive_rebounds']) + int(key['offensive_rebounds']), int(key['steals']), int(key['blocks']))
        print(tup)
        cur.execute("INSERT INTO season (playerid,fullname,points,assists,rebounds,steals,blocks) " + "VALUES(?,?,?,?,?,?,?)", tup)
        print("here")
        conn.commit()
        conn.close()
        
        




# conn = get_connection()
# print(conn)
# cur = conn.cursor()

# tup = (1,'Roberto', 10)
# cur.execute("INSERT INTO games (gameid,fullname,points) " +
#                            "VALUES(?,?,?)", tup)
# conn.commit()
# conn.close()
