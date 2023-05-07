# from email import policy
# from multiprocessing.dummy import active_children
# import profile
# from markupsafe import Markup
# import base64
# from flask_admin.contrib.sqla import ModelView
# import datetime
# from webforms import LoginForm, PoliceForm, CrimeForm, activeForm, MessageForm
# from tkinter import ACTIVE
# from flask_security import LoginForm
# from werkzeug.security import generate_password_hash, check_password_hash 
# from flask import Flask, request, redirect,url_for,session,logging, request, current_app, flash, request, redirect, abort
# from flask.templating import render_template
# from werkzeug.utils import secure_filename
# from datetime import datetime
# from datetime import date
# from flask_admin import Admin
# from flask_admin.contrib import sqla as flask_admin_sqla
# from flask_admin import AdminIndexView
# from flask_admin import expose
# from flask_admin.menu import MenuLink
# from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
# from flask_sqlalchemy import SQLAlchemy
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# import numpy as np
# from flask_admin.contrib.sqla import ModelView
# from werkzeug.utils import secure_filename
# from wtforms.validators import DataRequired, EqualTo, Length
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField,RadioField, DateField ,PasswordField, BooleanField, ValidationError, TextAreaField, SelectField, HiddenField
# from wtforms.validators import DataRequired, EqualTo, Length
# from wtforms.widgets import TextArea
# from flask_ckeditor import CKEditorField
# from flask_wtf.file import FileField
# from wtforms import Form, StringField, IntegerField, validators
# import re
# from flask_security import Security, SQLAlchemyUserDatastore 
# from flask_security import RoleMixin, UserMixin
# import uuid as uuid
# import os
# import cv2
# from flask import request, jsonify
# from flask_admin import Admin 
# from sqlalchemy import false, func
# from flask_admin.contrib import sqla
# from flask_migrate import Migrate, migrate
# import os.path as op
# from flask_admin.contrib.fileadmin import FileAdmin


# app = Flask(__name__)
# app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"

# UPLOAD_FOLDER = 'static/images/'
# UPLOAD_FOLDER2 = 'static/images/fingerprint/'
# path = op.join(op.dirname(__file__), 'static')


# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['UPLOAD_FINGER'] = UPLOAD_FOLDER2
# #app.config['UPLOAD_DIR'] = 'static/Uploads'
# app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///our_users.db'
# #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/our_users'

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# #admin = Admin(app, name='CRIME DATABASE', template_mode='bootstrap3')

# # Flask_Login Stuff
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# @login_manager.user_loader
# def load_user(user_id):
# 	return User.query.get(int(user_id))


# # class MicroBlogModelView(sqla.ModelView):

# #     def is_accessible(self):
# #         return login.current_user.is_authenticated

# #     def inaccessible_callback(self, name, **kwargs):
# #         # redirect to login page if user doesn't have access
# #         return redirect(url_for('login', next=request.url))


# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String)
#     picture = db.Column(db.String(80), nullable=True)
#     recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __repr__(self):
#         return '<Message %r>' % (self.id)
#     # def __str__(self):
#     #     return '<Message %r>' % (self.id)

# class Role(db.Model, RoleMixin):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(80), unique=True)
#     description = db.Column(db.String(255))

#     def __str__(self):
#         return self.name

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     batchno = db.Column(db.String(20), unique=False, nullable=False)
#     first_name = db.Column(db.String(20), unique=False, nullable=False)
#     last_name = db.Column(db.String(20), unique=False, nullable=False)
#     rank = db.Column(db.String(20), unique=False, nullable=False)
#     station = db.Column(db.String(20), unique=False, nullable=False)
#     profile_pic = db.Column(db.String(), nullable=True)
#     dob = db.Column(db.DateTime, nullable=False)
#     active = db.Column(db.Boolean, default=False, nullable=False)
#     gender = db.Column(db.String(20), unique=False, nullable=False)
#     messages_sent = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender')
#     messages_received = db.relationship('Message', foreign_keys='Message.recipient_id', backref='recipient')
#     station_dis = db.relationship('Crimerecords', foreign_keys='Crimerecords.station', backref='station_discription')
#     date_added = db.Column(db.DateTime, default=datetime.utcnow) 
# 	# Do some password stuff!
#     password_hash = db.Column(db.String(128))


#     def __repr__(self):
#         return '<User %r>' % (self.first_name)


# def __init__(self,id,batchno, first_name,last_name,rank,station,profile_pic, dob,password_hash,gender,active,sender):
#     self.id = id
#     self.batchno = batchno
#     self.first_name = first_name
#     self.last_name = last_name
#     self.rank = rank
#     self.station = station
#     self.profile_pic = profile_pic
#     self.sender = Message.recipient_id 
#     self.password_hash =password_hash
#     self.active =active
#     self.gender =gender
# # def __repr__(self):
# #     return f"Name : {self.first_name}, Age: {self.age}"
# class Crimerecords(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	first_name = db.Column(db.String(20), nullable=False, unique=False)
# 	last_name = db.Column(db.String(200), nullable=False)
# 	mother_name = db.Column(db.String(120), nullable=False, unique=False)
# 	# User Can Have Many Posts 
# 	image = db.Column(db.LargeBinary)
# 	case_id = db.Column(db.String(120))
# 	# Foreign Key To Link Users (refer to primary key of the user)
# 	crime_type = db.Column(db.String(120), nullable=False, unique=False)
# 	wanted = db.Column(db.String(120), nullable=False, unique=False)
# 	fingerprint = db.Column(db.String(120), nullable=False, unique=False)
# 	station = db.Column(db.String(120), db.ForeignKey('user.id'))
# 	gender = db.Column(db.String(120), nullable=False, unique=False)
# 	dob = db.Column(db.DateTime, nullable=False, unique=False)
# 	date_added = db.Column(db.DateTime, default=datetime.utcnow)
# 	profile_pic = db.Column(db.String(),nullable=True)
# 	profile_pic2 = db.Column(db.String(),nullable=True)
# 	# Foreign Key To Link Users (refer to primary key of the user)
# 	#station_added_id = db.Column(db.Integer, db.ForeignKey('police.station'))

# 	def age(self):#
# 		today = datetime.now()
# 		return int((datetime.now() - self.dob).days / 365.25)

# # Create customized model view class

# @app.template_filter('b64encode')
# def b64encode_filter(s):
#     return Markup(base64.b64encode(s.encode('utf-8')).decode('utf-8'))




# @app.route('/allofficer')
# def allofficer():
#     #profiles1 = Police.query.all()
#     return render_template('officer.html', police= User.query.all())

# @app.route('/send_message', methods=['GET', 'POST'])
# def send_message():
#     # get the list of users from the database
#     users = User.query.all()

#     # create the form and populate the recipient field with the list of users
#     form = MessageForm(request.form)
#     form.recipient_id.choices = [(str(user.id), user.batchno) for user in users]
#     if request.method == 'POST' and form.validate():
#         text = form.text.data
#         recipient_id = form.recipient_id.data
#         text = form.text.data
#         # sender_id = 1  # hardcoded for simplicity, you can use a session variable to store the current user's id
#         message = Message(recipient_id=recipient_id, text=text, sender_id=current_user.id)
#         db.session.add(message)
#         db.session.commit()
#         return redirect('/messages')
#     return render_template('send_message.html', form=form)


# @app.route('/messages')
# def messages():
#     user_id = current_user.id  # hardcoded for simplicity, you can use a session variable to store the current user's id
#     user = User.query.get(user_id)
#     received_messages = user.messages_received
#     sent_messages = user.messages_sent
#     return render_template('messages.html', received_messages=received_messages, sent_messages=sent_messages)	

# @app.route('/officer')
# def officer():
#    # Police.query.filter_by(rank = 'cpp').all() #= Police.query.all()
#    #police = current_user.rank
#   # return render_template('officer.html', police= Police.query.all())
#    return render_template('officer.html', police = User.query.filter_by(station = current_user.station).all())#=profiles1)


# @app.route('/admin.add_view')
# @login_required
# def admin():
# 	id = current_user.id
# 	if id == 2:
# 		return render_template("admin.html")
# 	else:
# 		flash("Sorry you must be the Admin to access the Admin Page...")
# 		return render_template('Admin/admin.html')   
#     # return render_template('Admin/admin.html')   

# @app.route('/detect', methods=['GET', 'POST'])
# def detect():
#     if request.method == 'POST':
#         # Get image from request
#         image = request.files['image'].read()
#         # Convert image to grayscale
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         # Load face detection classifier
#         face_cascade = cv2.CascadeClassifier('path/to/haarcascade_frontalface_default.xml')
#         # Detect faces in image
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
#         # Draw rectangles around detected faces
#         for (x, y, w, h) in faces:
#             cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
#         # Convert processed image to binary data
#         image_data = cv2.imencode('.jpg', image)[1].tostring()
#         db_face = User(image=image)
#         db.session.add(db_face)
#         db.session.commit()
#         # Return image with rectangles drawn around detected faces
       
#         # Pass image data to template
#         return render_template('detect.html', image_data=image_data)

# @app.route('/home')
# def home():
#     return render_template('home.html')

# @app.route('/', methods=['GET', 'POST'])
# @login_required
# def index():
#     id=current_user.id
#     user = User.query.get(id)
#     received_messages = user.messages_received
#     sent_messages = user.messages_sent
#     # get the list of users from the database
#     users = User.query.all()
#     # create the form and populate the recipient field with the list of users
#     form = MessageForm(request.form)
#     form.recipient_id.choices = [(str(user.id), user.batchno) for user in users]
#     if request.method == 'POST' and form.validate():
#         text = form.text.data
#         recipient_id = form.recipient_id.data
#         text = form.text.data
#         # sender_id = 1  # hardcoded for simplicity, you can use a session variable to store the current user's id
#         message = Message(recipient_id=recipient_id, text=text, sender_id=current_user.id)
#         db.session.add(message)
#         db.session.commit()
#         return redirect('/messages')
#     return render_template('index.html', form=form,received_messages=received_messages, sent_messages=sent_messages)


# @app.route('/view_all')
# #@login_required
# def view_all():
#    # profiles = Crimerecords.query.all()
#     age=Crimerecords.age
#     return render_template('view_all.html', crime= Crimerecords.query.all(),age=age)


# @app.route('/view')
# #@login_required
# def view():
#    # profiles = Crimerecords.query.all()
#     return render_template('view.html', crime= Crimerecords.query.filter_by(station = current_user.station).all())


# @app.route('/admindashboard/<int:id>',methods=['GET', 'POST'])
# @login_required
# def admindashboard(id):
#     # form = activeForm(request.form, obj=data)
#     data = User.query.get_or_404(id)
#     form = activeForm(request.form, obj=User)
#     if form.validate_on_submit():
#      #if request.method == "POST":
#        data.active = form.active.data
#     #    db.session.add(data)
#        db.session.commit()
#        flash('ACCOUNT UPDATED!!!')
#     #    return redirect(url_for("admindashboard/<int:id>")) 
#     return render_template('Admin/view.html', police= User.query.all(), 
# 				form=form, data = data)
  

# @app.route('/test')
# #@login_required
# def test():
#     return render_template('test_pw.html')

# @app.route('/wanted')
# @login_required
# def wanted():
#    # profiles = Crimerecords.query.all()
#     return render_template('wanted.html', crime= Crimerecords.query.filter_by(wanted='YES').all())

# @app.route('/addprofile', methods=["GET", "POST"])
# @login_required
# def addprofile():
#     if request.method == 'POST':
#         try:
#            first_name=request.form['first_name']
#            last_name=request.form['last_name']
#            username=request.form['username']
#            age=request.form['age']
#         #    #check profile
#         #    if request.files['profile_pic']:
#         #       profile_pic = request.files[' profile_pic']
#         #       #grab image name
#         #       pic_filename = secure_filename(profile_pic.filename)
#         #       #set uuid
#         #       pic_name = str(uuid.uuid1()) + "_" + pic_filename
#         #       #save that image
#         #       saver = request.files['profile_pic']
#         #       #change it to a string to save to db
#         #       profile_pic = pic_name
#            if first_name != '' and last_name !='' and username !='' and age is not None:
#             p = User(first_name=first_name, last_name=last_name, username=username,age=age)
#             db.session.add(p)
#             db.session.commit()
#             # saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
           
            
#             flash("Record Added  Successfully","success")
#             return redirect(url_for("view"))
#         except:
#             flash("ERROR IN OPERATION")
#         finally:
#             return redirect(url_for("view")) 

#     return render_template('addprofile.html')


# @app.route('/addcrime', methods=['GET', 'POST'])
# def addcrime():
# 	name = None
# 	form = CrimeForm()
# 	if form.validate_on_submit() and request.method == "POST":
# 		user = Crimerecords.query.filter_by(first_name=form.first_name.data).first()
# 		if user is None:
# 			#upload 
# 			profile_pic = request.files['profile_pic']
# 			profile_pic2 = request.files['profile_pic2']
# 			fingerprint = request.files['fingerprint']

# 			# Grab Image Name
# 			pic_filename = secure_filename(profile_pic.filename)
# 			pic_filename = secure_filename(profile_pic2.filename)
# 			pic_filename = secure_filename(fingerprint.filename)
# 			# Set UUID
# 			pic_name = str(uuid.uuid1()) + "_" + pic_filename
# 			pic_name2 = str(uuid.uuid1()) + "_" + pic_filename
# 			fingerprint = str(uuid.uuid1()) + "_" + pic_filename
# 			# Save That Image
# 			saver = request.files['profile_pic']
# 			saver2 = request.files['profile_pic2']
# 			saver1 = request.files['fingerprint']
# 			# Change it to a string to save to db
# 			profile_pic = pic_name
# 			#file2 = request.files["profile_pic"]
# 			#hashed_pw = generate_password_hash(form.password_hash.data, "sha256")
# 			user = Crimerecords(first_name=form.first_name.data,
# 			 last_name=form.last_name.data, 
# 			 mother_name=form.mother_name.data, 
# 			 crime_type=form.crime_type.data, 
# 			 wanted=form.gender.data,
# 			 gender=form.gender.data,
# 			 dob=form.dob.data,
# 			 profile_pic= pic_name,
# 			 profile_pic2= pic_name2,
# 			 fingerprint= fingerprint, 
# 			 station=current_user.station)
# 			db.session.add(user)
# 			db.session.commit()
# 			saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
# 			saver1.save(os.path.join(app.config['UPLOAD_FINGER'], fingerprint))
# 			saver2.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name2))
# 			#file2.save(os.path.join(app.config['UPLOAD_FOLDER'],file2.filename))
			
			
# 		# name = form.name.data
# 		form.mother_name.data = ''
# 		form.first_name.data = ''
# 		form.profile_pic.data = ''
# 		form.last_name.data = ''
# 		form.gender.data = ''
# 		form.wanted.data = ''
# 		form.dob.data = ''
# 		form.crime_type.data = ''
# 		form.profile_pic2.data = ''
# 		form.fingerprint.data = ''
# 		flash("added")
# 		return redirect(url_for('view'))
# 	our_users = Crimerecords.query.order_by(Crimerecords.date_added)
# 	return render_template("addcrime.html",
# 		form=form,
# 		name=name,
# 		our_users=our_users)



# @app.route('/details_crime/<int:id>', methods=['GET', 'POST'])
# @login_required
# def details_crime(id):
# 	form = CrimeForm()
# 	age=Crimerecords.age
# 	name = Crimerecords.query.get_or_404(id)
# 	return render_template('details_crime.html', 
# 	 			form=form,
# 				name = name,
# 				id = id,age=age)

# def calculate(born):
# 	today = datetime.now()
# 	return today.year - born.year - ((today.month, today.day)<(born.month, born.day))
# #Create Dashboard Page
# @app.route('/dashboard/<int:id>', methods=['GET', 'POST'])
# #@login_required
# def dashboard(id):
# 	form = PoliceForm()
# 	id = current_user.id
# 	name_to_update = User.query.get_or_404(id)
# 	# dob = datetime.strptime(dob, '%Y-%m-%d')
# 	# age = (datetime.today() - dob).days/365
# 	# age = round(age, 1)
# 	if request.method == "POST":
# 		name_to_update.first_name = request.form['first_name']
# 		name_to_update.last_name = request.form['last_name']
# 		name_to_update.batchno = request.form['batchno']
# 		# age = (datetime.today() - dob).days/365
# 		# age = round(age, 1)
# 		# name_to_update.username = request.form['username']
# 		# name_to_update.about_author = request.form['about_author']
# 		# Check for profile pic
# 		if request.files['profile_pic']:
# 			name_to_update.profile_pic = request.files['profile_pic']

# 			# Grab Image Name
# 			pic_filename = secure_filename(name_to_update.profile_pic.filename)
# 			# Set UUID
# 			pic_name = str(uuid.uuid1()) + "_" + pic_filename
# 			# Save That Image
# 			saver = request.files['profile_pic']
			

# 			# Change it to a string to save to db
			
# 			name_to_update.profile_pic = pic_name
# 			try:
# 				db.session.commit()
# 				saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
# 				flash("User Updated Successfully!")
# 				return render_template("dashboard.html", 
# 					form=form,
# 					name_to_update = name_to_update)
# 			except:
# 				flash("Error!  Looks like there was a problem...try again!")
# 				return render_template("dashboard.html", 
# 					form=form,
# 					name_to_update = name_to_update)
# 		else:
# 			db.session.commit()
# 			flash("User Updated Successfully!")
# 			return render_template("dashboard.html", 
# 				form=form, 
# 				name_to_update = name_to_update)
# 	else:
# 		return render_template("dashboard.html", 
# 				form=form,
# 				name_to_update = name_to_update,
# 				id = id )
# 	return render_template('dashboard.html')


# @app.route('/register', methods=['GET', 'POST'])
# def register():
# 	name = None
# 	form = PoliceForm(active=True)
# 	if form.validate_on_submit() and request.method == "POST":
# 		user = User.query.filter_by(batchno=form.batchno.data).first()
# 		if user is None:
# 			# Hash the password!!!
# 			profile_pic = request.files['profile_pic']

# 			# Grab Image Name
# 			pic_filename = secure_filename(profile_pic.filename)
# 			# Set UUID
# 			pic_name = str(uuid.uuid1()) + "_" + pic_filename
# 			# Save That Image
# 			saver = request.files['profile_pic']
# 			# Change it to a string to save to db
# 			profile_pic = pic_name
# 			#file2 = request.files["profile_pic"]
# 			hashed_pw = generate_password_hash(form.password_hash.data, "sha256")
# 			user = User(batchno=form.batchno.data, first_name=form.first_name.data, last_name=form.last_name.data, rank=form.rank.data, gender=form.gender.data,station=form.station.data,dob=form.dob.data,profile_pic= pic_name, password_hash=hashed_pw, active=True)
# 			db.session.add(user)
# 			db.session.commit()
# 			saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
# 			#file2.save(os.path.join(app.config['UPLOAD_FOLDER'],file2.filename))
			
			
# 		# name = form.name.data
# 		form.batchno.data = ''
# 		form.first_name.data = ''
# 		form.profile_pic.data = ''
# 		form.last_name.data = ''
# 		form.gender.data = ''
# 		form.station.data = ''
# 		form.dob.data = ''
# 		form.rank.data = ''
# 		form.password_hash.data = ''
# 		flash("added")
# 		return redirect(url_for('register'))
# 	our_users = User.query.order_by(User.date_added)
# 	return render_template("register.html",
# 		form=form,
# 		name=name,
# 		our_users=our_users)


# # Update Database Record
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# @login_required
# def update(id):
# 	form = PoliceForm(active=True)
# 	name_to_update = User.query.get_or_404(id)
# 	if request.method == "POST":
# 		name_to_update.rank = request.form['rank']
# 		name_to_update.active = request.form['active']
# 		name_to_update.station = request.form['station']
# 		try:
# 			db.session.commit()
# 			flash("User Updated Successfully!")
# 			return render_template("update.html", 
# 				form=form,
# 				name_to_update = name_to_update, id=id)
# 		except:
# 			flash("Error!  Looks like there was a problem...try again!")
# 			return render_template("update.html", 
# 				form=form,
# 				name_to_update = name_to_update,
# 				id=id)
# 	else:
# 		return render_template("update.html", 
# 				form=form,
# 				name_to_update = name_to_update,
# 				id = id)

# # Update Database Record
# @app.route('/edit_crime/<int:id>', methods=['GET', 'POST'])
# @login_required
# def edit_crime(id):
# 	form =CrimeForm()
# 	name_to_update = Crimerecords.query.get_or_404(id)
# 	if request.method == "POST":
# 		name_to_update.first_name = request.form['first_name']
# 		name_to_update.last_name = request.form['last_name']
# 		#name_to_update.favorite_color = request.form['favorite_color']
# 		#name_to_update.username = request.form['username']
# 		try:
# 			db.session.commit()
# 			flash("User Updated Successfully!")
# 			return render_template("edit_crime.html", 
# 				form=form,
# 				name_to_update = name_to_update, id=id)
# 		except:
# 			flash("Error!  Looks like there was a problem...try again!")
# 			return render_template("edit_crime.html", 
# 				form=form,
# 				name_to_update = name_to_update,
# 				id=id)
# 	else:
# 		return render_template("edit_crime.html", 
# 				form=form,
# 				name_to_update = name_to_update,
# 				id = id)

# # @app.route('/search', methods=['GET', 'POST'])
# # def search():
# #     form = SearchForm()
# #     if form.validate_on_submit():
# #         search_term = form.search_term.data
# #         filter_option = form.filter_option.data
# #         if filter_option == 'first_name':
# #             results = User.query.filter(User.first_name.like(f'%{search_term}%')).all()
# #         elif filter_option == 'last_name':
# #             results = User.query.filter(User.last_name.like(f'%{search_term}%')).all()
# #         return render_template('results.html', results=results, form=form)
# #     return render_template('search.html', form=form)

# @app.route('/search', methods=['POST'])
# def search():
#     search_term = request.form['search_term']
#     filter_option = request.form['filter_option']
#     if filter_option == 'last_name':
#         results = User.query.filter(User.last_name.like(f'%{search_term}%')).all()
#     elif filter_option == 'first_name':
#         results = User.query.filter(User.first_name.like(f'%{search_term}%')).all()
#     return render_template('results.html',results=results)

# @app.route('/upload', methods=['POST'])
# def upload():
#     fingerprint = request.files['file'].read()
#     fingerprint = Crimerecords(name=fingerprint)
#     db.session.add(fingerprint)
#     db.session.commit()
#     return jsonify({'message': 'Fingerprint uploaded successfully!'})


# class DefaultModelView(flask_admin_sqla.ModelView):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def is_accessible(self):
#         return current_user.is_authenticated 

#     def inaccessible_callback(self, name, **kwargs):
#         # redirect to login page if user doesn't have access
#         return redirect(url_for('login', next=request.url))


# class MyAdminIndexView(AdminIndexView):
#     def is_accessible(self):
#         return current_user.is_authenticated 

#     def inaccessible_callback(self, name, **kwargs):
#         # redirect to login page if user doesn't have access
#         return redirect(url_for('login', next=request.url))

#     @expose('/')
#     def index(self):
#         if not current_user.is_authenticated:
#             flash('Please log in first...', 'error')
#             next_url = request.url
#             login_url = '%s?next=%s' % (url_for('login'), next_url)
#             return redirect(login_url)
#         # import pdb;pdb.set_trace()
#         if current_user.id == 2:
#             return super(MyAdminIndexView,self).index()
#         else:
#             flash('Please log in first...', 'error')
#             return redirect(url_for("login"))
# # further in app.py
# admin = Admin(
#         app,
#         name='DATABASE',
#          template_mode='bootstrap4',
#         index_view=MyAdminIndexView()
#     )


# def __init__(self,id,uname, password_hash):
#     self.id = id
#     self.username = uname
#     self.password_hash = password_hash
#     #self.id = id

# class DefaultModelView(ModelView):
# 	column_exclude_list = ['password_hash', ]
# 	column_searchable_list = ['first_name', 'last_name']
# 	can_export = True
	
# 	can_view_details = True
# 	edit_modal = True
# 	column_editable_list = ['first_name', 'last_name','active','batchno']
	

	
# class CrimerecordsView(ModelView):
# 	column_exclude_list = ['Profile_Pic', ]
# 	column_exclude_list = ['ProfilePic2', ]
# 	column_searchable_list = ['first_name', 'last_name']
# 	can_export = True
# 	can_view_details = True

# class MessageView(ModelView):
# 	can_export = True
# 	can_view_details = True

# admin.add_view(DefaultModelView(User, db.session))
# admin.add_link(MenuLink(name='Logout', category='', url='/logout'))
# admin.add_view(FileAdmin(path, '/static/', name='Static Files'))
# # admin.add_view(UserView(User, db.session))
# # admin.add_view(NotificationsView(name='Notifications', endpoint='notify'))
# admin.add_view(MessageView(Message, db.session))
# admin.add_view(CrimerecordsView(Crimerecords, db.session))
# admin.add_view(ModelView(Role, db.session))
# # class MyModelView(sqla.ModelView):

# #     def is_accessible(self):
# #         if not current_user.is_active or not current_user.is_authenticated:
# #             return False

# #         # if current_user.has_role('superuser'):
# #         #     return True

# #         return False

# #     def _handle_view(self, name, **kwargs):
# #         """
# #         Override builtin _handle_view in order to redirect users when a view is not accessible.
# #         """
# #         if not self.is_accessible():
# #             if current_user.is_authenticated:
# #                 # permission denied
# #                 abort(403)
# #             else:
# #                 # login
# #                 return redirect(url_for('security.login', next=request.url))

# # Create Login Page




# # @app.route('/match', methods=['POST'])
# # def match():
# #     # data = request.files['file'].read()
# #     sample = cv2.imread("static/images/fingerprint/hard/1__M_Left_index_finger_CR.bmp")
# @app.route('/match', methods=['GET', 'POST'])
# def match():
#     if request.method == 'POST':
#         # get the uploaded file
#         file = request.files['file']
#         # read the file as an image
#         sample = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
#     else:
#         # load a default image
#         return render_template('match.html')

#     best_score = 0
#     filename = None
#     image = None
#     kp1, kp2, mp = None, None, None

#     counter = 0
#     for file in Crimerecords.query.limit(1000).all():
#         file = file.fingerprint
#         if counter%10 == 0:
#             print(counter)
#             print(file)

#         counter += 1
#         fingerprint_image = cv2.imread("static/images/fingerprint/"+ file)
#         if fingerprint_image is None:

#             print("Error: could not read fingerprint image")
#             continue

#         sift = cv2.SIFT_create()
#         keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None)
#         keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)

#         matches = cv2.FlannBasedMatcher({'algorithm':1, 'trees':10},
#                                         {}).knnMatch(descriptors_1, descriptors_2, k=2)
#         match_points = []

#         for p, q in matches:
#             if p.distance <0.1 * q.distance:
#                 match_points.append(p)

#         keypoints = 0
#         if len(keypoints_1) < len(keypoints_2):
#             keypoints = len(keypoints_1)
#         else:
#             keypoints = len(keypoints_2)

#         if len(match_points) / keypoints*100 > best_score:
#             best_score = len(match_points)/keypoints*100
#             filename = file
#             image = fingerprint_image
#             kp1, kp2, mp = keypoints_1, keypoints_2, match_points
#             kp1, kp2, mp = keypoints_1, keypoints_2, match_points

#     print("BEST MATCH:" + file)
#     print("Score: " + str(best_score))

#     result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
#     result = cv2.resize(result, None, fx=4, fy=4)

#     # Convert the image to a PNG format
#     _, buffer = cv2.imencode('.png', result)
#     result = buffer.tobytes()
#     b64_result = base64.b64encode(result).decode('utf-8')

#     if filename:
#         best_match = Crimerecords.query.filter_by(fingerprint=filename).first()
#     else:
#         best_match = None

#     return render_template('match.html', result=b64_result, best_match=best_match, score=best_score)
        


# @app.route('/match_face', methods=['GET', 'POST'])
# def match_face():
#     if request.method == 'POST':
#         # Get the uploaded file
#         file = request.files['file']
#         # Read the file as an image
#         img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
#         # Compute the face embedding
#         dist = match_faces(img)
#         # Find the matching face in the database
#         face = Crimerecords.query.filter(Crimerecords.embedding < 0.5 * dist).first()
#         # Render the result template
#         return render_template('match_faces.html', face=face)
#     else:
#         return render_template('match_faces.html')

# def match_faces(img1, img2):
#     # Load the images and convert to grayscale
#     img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#     img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the images using Haar Cascade classifier
#     face_cascade = cv2.CascadeClassifier('static/haarcascade_frontalface_default.xml')
#     faces1 = face_cascade.detectMultiScale(img1_gray, scaleFactor=1.1, minNeighbors=5)
#     faces2 = face_cascade.detectMultiScale(img2_gray, scaleFactor=1.1, minNeighbors=5)

#     # If no faces are detected in either image, return None
#     if len(faces1) == 0 or len(faces2) == 0:
#         return None

#     # Find the largest face in each image
#     largest_face1 = max(faces1, key=lambda x: x[2])
#     largest_face2 = max(faces2, key=lambda x: x[2])

#     # Extract the face regions from the images
#     x1, y1, w1, h1 = largest_face1
#     x2, y2, w2, h2 = largest_face2
#     face1 = img1_gray[y1:y1+h1, x1:x1+w1]
#     face2 = img2_gray[y2:y2+h2, x2:x2+w2]

#     # Resize the face regions to a fixed size
#     face1 = cv2.resize(face1, (256, 256))
#     face2 = cv2.resize(face2, (256, 256))

#     # Compute the difference between the faces using L2 distance
#     diff = cv2.absdiff(face1, face2)
#     dist = np.sum(diff) / (256 * 256)

#     return dist


	
# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	form = LoginForm()
# 	if form.validate_on_submit():
# 		user = User.query.filter_by(batchno=form.batchno.data).first()
# 		if user :
# 			# Check the hash
# 			if check_password_hash(user.password_hash, form.password.data)and user.active == True:
# 				login_user(user)
# 				flash("Login Succesfull!!")
# 				return redirect(url_for('index'))
# 			elif user.active == False:
# 				flash("Account Disabled - Ask Admin for permission!")
# 			else:
# 				flash("password incorrect")	
# 		else:
# 			flash("That User Doesn't Exist! Try Again...")


# 	return render_template('login.html', form=form)

# # Create Logout Page
# @app.route('/logout', methods=['GET', 'POST'])
# @login_required
# def logout():
# 	logout_user()
# 	flash("You Have Been Logged Out!  Thanks For Stopping By...")
# 	return redirect(url_for('login'))    


# # Create A Search Form
# class LoginForm(FlaskForm):
# 	batchno = StringField("Batchno", validators=[DataRequired()])
# 	password = PasswordField("Password", validators=[DataRequired()])
# 	submit = SubmitField("Submit")

# @app.route('/delete/<int:id>')
# def delete(id):
#     data = User.query.get(id)
#     db.session.delete(data)
#     db.session.commit()
#     flash("deleted succesfully")
#     return redirect('/allofficer')


# @app.route('/deletecrme/<int:id>')
# def deletecrme(id):
#     data = Crimerecords.query.get(id)
#     db.session.delete(data)
#     db.session.commit()
#     flash("deleted succesfully")
#     return redirect('/view')	

from app import db, Location,User
from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import datetime
# create the database tables
db.create_all()
hashed_pw = generate_password_hash('admin', "sha256")


user1= User(batchno='admin', first_name='admin',
 last_name='admin', rank='del',
   station=3, profile_pic='admin', dob=datetime(2023,12,31),
  active=1, gender='MALE', password_hash=hashed_pw, Personal_email='1fregenevwegba@gmail.com',Phone_No='013777979',Supervisor_id='admn' )

user2= User(batchno='admin1', first_name='admin',
 last_name='admin', rank='del',
   station=2, profile_pic='admin', dob=datetime(2023,12,31),
  active=1, gender='MALE', password_hash=hashed_pw, Personal_email='2fregenevwegba@gmail.com',Phone_No='013777979',Supervisor_id='admn')

user3= User(batchno='admin3', first_name='admin',
 last_name='admin', rank='del',
   station=2, profile_pic='admin', dob=datetime(2023,12,31),
  active=1, gender='MALE', password_hash=hashed_pw, Personal_email='3fregenevwegba@gmail.com',Phone_No='013777979',Supervisor_id='admn')

user4= User(batchno='admin4', first_name='admin',
 last_name='admin', rank='del',
   station=2, profile_pic='admin', dob=datetime(2023,12,31),
  active=1, gender='MALE', password_hash=hashed_pw, Personal_email='4fregenevwegba@gmail.com',Phone_No='013777979',Supervisor_id='admn')

user5= User(batchno='admin5', first_name='admin',
 last_name='admin', rank='del',
   station=1, profile_pic='admin', dob=datetime(2023,12,31),
  active=1, gender='MALE', password_hash=hashed_pw, Personal_email='5fregenevwegba@gmail.com',Phone_No='013777979',Supervisor_id='admn')

user6= User(batchno='admin6', first_name='admin',
 last_name='admin', rank='del',
   station=1, profile_pic='admin', dob=datetime(2023,12,31),
  active=1, gender='MALE', password_hash=hashed_pw, Personal_email='6fregenevwegba@gmail.com',Phone_No='013777979',Supervisor_id='admn')

user7= User(batchno='admin7', first_name='admin',
 last_name='admin', rank='del',
   station=2, profile_pic='admin', dob=datetime(2023,12,31),
  active=1, gender='MALE', password_hash=hashed_pw, Personal_email='7fregenevwegba@gmail.com',Phone_No='013777979',Supervisor_id='admn')
# add some test data
location1 = Location(name='Lagos', latitude=51.5074, longitude=-0.1278)
location2 = Location(name='abuja', latitude=40.7128, longitude=-74.0060)
location3 = Location(name='jos', latitude=35.6895, longitude=139.6917)
db.session.add_all([ user1 ,user2,user3,user4,user5,user6,user7,location1,location2,location3])
db.session.commit()

# @app.route('/adminofficer/<int:id>')
# def adminofficer(id):
    
#     flash("deleted succesfully")
#     return render_template("Admin/adminofficer.html")

# @property
# def password(self):
# 		raise AttributeError('password is not a readable attribute!')

# @password.setter
# def password(self, password):
# 		self.password_hash = generate_password_hash(password)

# def verify_password(self, password):
# 	return check_password_hash(self.password_hash, password)

# if __name__ == '__main__':
#     app.debug = True
#     app.run(host="0.0.0.0")    
