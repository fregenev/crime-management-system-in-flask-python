from flask_security import RoleMixin, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask import Flask
from sqlalchemy import LargeBinary
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
from datetime import datetime


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# create a key to encrypt and decrypt messages
key = Fernet.generate_key()
cipher_suite = Fernet(key)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    encrypted_text = db.Column(db.LargeBinary)  # store the encrypted message as binary data
    picture = db.Column(db.String(80), nullable=True)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def set_text(self, text):
        # encrypt the message before storing it
        self.encrypted_text = cipher_suite.encrypt(text.encode())
        self.text = text

    def get_text(self):
        # decrypt the message before returning it
        return cipher_suite.decrypt(self.encrypted_text).decode()



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    batchno = db.Column(db.String(20), unique=True, nullable=False)
    Phone_No = db.Column(db.String(21), nullable=True)
    Personal_email = db.Column(db.String(128), unique=True, nullable=False)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    rank = db.Column(db.String(20), unique=False, nullable=False)
    station = db.Column(db.Integer, db.ForeignKey('location.id'))
    profile_pic = db.Column(db.String(100))
    media_type = db.Column(db.String(10))
    media_data = db.Column(LargeBinary)
    dob = db.Column(db.DateTime, nullable=False)
    Supervisor_id = db.Column(
        db.String(128), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable=False)
    caught_by_user = db.relationship('Crimerecords', foreign_keys='Crimerecords.caught_by', backref='caught_by_id')
    messages_sent = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender')
    messages_received = db.relationship('Message', foreign_keys='Message.recipient_id', backref='recipient')
    date_added = db.Column(db.DateTime, default=datetime.utcnow) 
	# Do some password stuff!
    password_hash = db.Column(db.String(128))
    
    @property
    def password(self):
        return self.password
    
    @password.setter
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.first_name)


def __init__(self,id,batchno, first_name,last_name,rank,profile_pic, dob,password_hash,gender,active,sender):
    self.id = id
    self.batchno = batchno
    self.first_name = first_name
    self.last_name = last_name
    self.rank = rank
    self.profile_pic = profile_pic
    self.sender = Message.recipient_id 
    self.password_hash =password_hash
    self.active =active
    self.gender =gender
# def __repr__(self):
#     return f"Name : {self.first_name}, Age: {self.age}"
class Crimerecords(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20), nullable=False, unique=False)
	last_name = db.Column(db.String(60), nullable=False)
	mother_name = db.Column(db.String(40), nullable=False, unique=False)
	motive = db.Column(db.String(64))
	nationality = db.Column(db.String(32))
	phone_No = db.Column(db.String(64))
	case_id = db.Column(db.String(10))
	medicals = db.Column(db.String(64))
	address = db.Column(db.String(208))
	crime_type = db.Column(db.String(120), nullable=False, unique=False)
	wanted = db.Column(db.String(120), nullable=False, unique=False)
	fingerprint = db.Column(db.String(120), nullable=False, unique=False)
	station = db.Column(db.Integer, db.ForeignKey('location.id'))
	caught_by = db.Column(db.Integer, db.ForeignKey('user.id'))
	gender = db.Column(db.String(20), nullable=False, unique=False)
	dob = db.Column(db.DateTime, nullable=False, unique=False)
	date_added = db.Column(db.DateTime, default=datetime.utcnow)
	profile_pic = db.Column(db.String(300))
	evidence = db.Column(db.String(300))
	media_type = db.Column(db.String(10))
	media_data = db.Column(LargeBinary)
        
    
    
	def __repr__(self):#
		return (self.first_name,self.station)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_name=db.Column(db.String(20))
    name = db.Column(db.String(50))
    data = db.Column(db.LargeBinary(length=(2**32)-1))
    about = db.Column(db.String(150))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    station_crimerecord = db.relationship('Crimerecords', foreign_keys='Crimerecords.station', backref='station_id')
    station_user = db.relationship('User', foreign_keys='User.station', backref='station_id')

    def __repr__(self):
        return (self.station_name)
    
    def __init__(self, name, data,about,latitude,longitude,station_name):
        self.name = name
        self.data = data
        self.about= about
        self.latitude=latitude
        self.longitude=longitude
        self.station_name=station_name
        
