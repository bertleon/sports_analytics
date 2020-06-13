import flask 

app = flask.Flask(__name__)

app.config.from_object('sports_analytics.config')

#not sure if this is needed
app.config.from_envvar('SPORTS_ANALYTICS_SETTINGS', silent=True)

import sports_analytics.calc_stats_api
import sports_analytics.model
