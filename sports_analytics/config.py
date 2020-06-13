import os 

APPLICATION_ROOT = '/'

# UPLOAD_FOLDER = os.path.join(
#     os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
#     'var', 'uploads'
# )
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'sports_analytics.sqlite3'
)