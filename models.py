from flask_security import RoleMixin, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask import Flask
from datetime import datetime


app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from cryptography.fernet import Fernet


# create a key to encrypt and decrypt messages
key = Fernet.generate_key()
cipher_suite = Fernet(key)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
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


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    batchno = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    rank = db.Column(db.String(20), unique=False, nullable=False)
    station = db.Column(db.String(20), unique=False, nullable=False)
    profile_pic = db.Column(db.String(), nullable=True)
    dob = db.Column(db.DateTime, nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable=False)
    messages_sent = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender')
    messages_received = db.relationship('Message', foreign_keys='Message.recipient_id', backref='recipient')
    station_dis = db.relationship('Crimerecords', foreign_keys='Crimerecords.station', backref='station_discription')
    date_added = db.Column(db.DateTime, default=datetime.utcnow) 
	# Do some password stuff!
    password_hash = db.Column(db.String(128))


    def __repr__(self):
        return '<User %r>' % (self.first_name)


def __init__(self,id,batchno, first_name,last_name,rank,station,profile_pic, dob,password_hash,gender,active,sender):
    self.id = id
    self.batchno = batchno
    self.first_name = first_name
    self.last_name = last_name
    self.rank = rank
    self.station = station
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
	last_name = db.Column(db.String(200), nullable=False)
	mother_name = db.Column(db.String(120), nullable=False, unique=False)
	# User Can Have Many Posts 
	image = db.Column(db.LargeBinary)
	case_id = db.Column(db.String(120))
	# Foreign Key To Link Users (refer to primary key of the user)
	crime_type = db.Column(db.String(120), nullable=False, unique=False)
	wanted = db.Column(db.String(120), nullable=False, unique=False)
	fingerprint = db.Column(db.String(120), nullable=False, unique=False)
	station = db.Column(db.String(120), db.ForeignKey('user.id'))
	gender = db.Column(db.String(120), nullable=False, unique=False)
	dob = db.Column(db.DateTime, nullable=False, unique=False)
	date_added = db.Column(db.DateTime, default=datetime.utcnow)
	profile_pic = db.Column(db.String(),nullable=True)
	profile_pic2 = db.Column(db.String(),nullable=True)
	# Foreign Key To Link Users (refer to primary key of the user)
	# Foreign Key To Link Users (refer to primary key of the user)
	#station_added_id = db.Column(db.Integer, db.ForeignKey('police.station'))

	def age(self):#
		today = datetime.now()
		return int((datetime.now() - self.dob).days / 365.25)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)