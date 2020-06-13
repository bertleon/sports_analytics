import flask
import sports_analytics

@sports_analytics.app.route('/')
def getLeBron():
    connection = sports_analytics.model.get_db()
    cursor = connection.cursor()
    dict  = {}
    for row in  cursor.execute('SELECT * FROM season'):
        dict['name'] = row['fullname']
 
    cursor.close()
    return dict