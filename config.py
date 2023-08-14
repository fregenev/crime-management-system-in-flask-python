# Create dummy secrey key so we can use sessions
SECRET_KEY = 'my super secret key that no one is supposed to know'

# Create in-memory database
DATABASE_FILE = 'our_users.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
SQLALCHEMY_ECHO = False

# Flask-Security config
SECURITY_URL_PREFIX = "/admin"
SECURITY_PASSWORD_HASH = "pbkdf2_sha256"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

#STORAGE PATH FOR FILE
UPLOAD_FOLDER = 'static/images/'
UPLOAD_FOLDER2 = 'static/images/fingerprint/'

UPLOAD_FOLDER = UPLOAD_FOLDER
UPLOAD_FINGER = UPLOAD_FOLDER2
#app.config['UPLOAD_DIR'] = 'static/Uploads'
FLASK_ADMIN_SWATCH = 'cerulean'
