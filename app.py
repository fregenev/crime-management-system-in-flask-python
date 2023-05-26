from email import policy
from models import Message,app,db,Role,User,Crimerecords,Location
from markupsafe import Markup
import base64
import folium
from flask_admin.contrib.sqla import ModelView
import datetime
from webforms import PoliceForm, CrimeForm, activeForm, MessageForm,LoginForm,PasswordUpdateForm
# from flask_security import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash 
from flask import Flask, request, redirect,url_for,request,flash, request, redirect, abort
from flask.templating import render_template
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib import sqla as flask_admin_sqla
from flask_admin import AdminIndexView
from flask_admin import helpers, expose
from flask_admin.menu import MenuLink
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
import numpy as np
from flask_admin.contrib.sqla import ModelView
from werkzeug.utils import secure_filename
import uuid as uuid
import os
import cv2
from flask import request, jsonify
from flask_admin import Admin 
import os.path as op
from flask_admin.contrib.fileadmin import FileAdmin


# app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"

path = op.join(op.dirname(__file__), 'static')




# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///our_users.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/our_users'

#admin = Admin(app, name='CRIME DATABASE', template_mode='bootstrap3')

# Flask_Login Stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


# class MicroBlogModelView(sqla.ModelView):

#     def is_accessible(self):
#         return login.current_user.is_authenticated

#     def inaccessible_callback(self, name, **kwargs):
#         # redirect to login page if user doesn't have access
#         return redirect(url_for('login', next=request.url))

# Create customized model view class

@app.template_filter('b64encode')
def b64encode_filter(s):
    return Markup(base64.b64encode(s.encode('utf-8')).decode('utf-8'))



@app.route('/ddd', methods=['GET', 'POST'])
@app.route('/allofficer')
def allofficer():
    #profiles1 = Police.query.all()
    return render_template('officer.html', police= User.query.all())


@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    # get the list of users from the database
    users = User.query.all()

    # create the form and populate the recipient field with the list of users
    form = MessageForm(request.form)
    form.recipient_id.choices = [(str(user.id), user.batchno) for user in users]
    if request.method == 'POST' and form.validate():
        text = form.text.data
        recipient_id = form.recipient_id.data
        # sender_id = 1  # hardcoded for simplicity, you can use a session variable to store the current user's id
        message = Message(recipient_id=recipient_id, sender_id=current_user.id)
        message.set_text(text)
        db.session.add(message)
        db.session.commit()
        return redirect('/messages')
    return render_template('send_message.html', form=form)

@app.route('/messages')
def messages():
    user_id = current_user.id  # hardcoded for simplicity, you can use a session variable to store the current user's id
    user = User.query.get(user_id)
    received_messages = user.messages_received
    sent_messages = user.messages_sent
    return render_template('messages.html', received_messages=received_messages, sent_messages=sent_messages)	

@app.route('/officer')
def officer():
   # Police.query.filter_by(rank = 'cpp').all() #= Police.query.all()
   #police = current_user.rank
  # return render_template('officer.html', police= Police.query.all())
   return render_template('officer.html', police = User.query.filter_by(station = current_user.station).all())#=profiles1)


@app.route('/admin1')
@login_required
def admin():
	id = current_user.id
	if id == 1:
		return render_template("Admin/admin.html")
	else:
		flash("Sorry you must be the Admin to access the Admin Page...")
		return render_template('Admin/admin.html')   
    # return render_template('Admin/admin.html')   


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = PasswordUpdateForm()
    id = current_user.id
    user = User.query.get_or_404(id)
    if form.validate_on_submit():
        if current_user.check_password(form.old_password.data):
            current_user.set_password(form.new_password.data)
            db.session.commit()
            flash('Password updated successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Incorrect password. Please try again.', 'danger')
            form.old_password.errors.append('Incorrect password')

    return render_template('index.html',user=user, form=form)



@app.route('/view_all')
#@login_required
def view_all():
   # profiles = Crimerecords.query.all()
    return render_template('view_all.html', crime= Crimerecords.query.all())

@app.route('/map1')
#@login_required
def map1():
   # profiles = Crimerecords.query.all()
    return render_template('mapcopy.html', map= Location.query.all())


@app.route('/station')
#@login_required
def station():
   # profiles = Crimerecords.query.all()
    return render_template('station.html', station= Location.query.all())


@app.route('/details_station/<int:id>', methods=['GET', 'POST'])
@login_required
def details_station(id):
	name = Location.query.get_or_404(id)
	return render_template('station_details.html',
				name = name,
				id = id)



@app.route('/view')
#@login_required
def view():
   # profiles = Crimerecords.query.all()
    return render_template('view.html', crime= Crimerecords.query.filter_by(station = current_user.station).all())


@app.route('/admindashboard/<int:id>',methods=['GET', 'POST'])
@login_required
def admindashboard(id):
    # form = activeForm(request.form, obj=data)
    data = User.query.get_or_404(id)
    form = activeForm(request.form, obj=User)
    if form.validate_on_submit():
     #if request.method == "POST":
       data.active = form.active.data
    #    db.session.add(data)
       db.session.commit()
       flash('ACCOUNT UPDATED!!!')
    #    return redirect(url_for("admindashboard/<int:id>")) 
    return render_template('view.html', police= User.query.all(), 
				form=form, data = data)
  

@app.route('/test')
#@login_required
def test():
    return render_template('test_pw.html')

@app.route('/wanted')
@login_required
def wanted():
   # profiles = Crimerecords.query.all()
    return render_template('wanted.html', crime= Crimerecords.query.filter_by(wanted='YES').all())

@app.route('/addprofile', methods=["GET", "POST"])
@login_required
def addprofile():
    if request.method == 'POST':
        try:
           first_name=request.form['first_name']
           last_name=request.form['last_name']
           username=request.form['username']
           age=request.form['age']
        #    #check profile
        #    if request.files['profile_pic']:
        #       profile_pic = request.files[' profile_pic']
        #       #grab image name
        #       pic_filename = secure_filename(profile_pic.filename)
        #       #set uuid
        #       pic_name = str(uuid.uuid1()) + "_" + pic_filename
        #       #save that image
        #       saver = request.files['profile_pic']
        #       #change it to a string to save to db
        #       profile_pic = pic_name
           if first_name != '' and last_name !='' and username !='' and age is not None:
            p = User(first_name=first_name, last_name=last_name, username=username,age=age)
            db.session.add(p)
            db.session.commit()
            # saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
           
            
            flash("Record Added  Successfully","success")
            return redirect(url_for("view"))
        except:
            flash("ERROR IN OPERATION")
        finally:
            return redirect(url_for("view")) 

    return render_template('addprofile.html')


@app.route('/addcrime', methods=['GET', 'POST'])
def addcrime():
	name = None
	form = CrimeForm()
	if form.validate_on_submit() and request.method == "POST":
		user = Crimerecords.query.filter_by(first_name=form.first_name.data).first()
		if user is None:
			#upload 
			profile_pic = request.files['profile_pic']
			profile_pic2 = request.files['profile_pic2']
			fingerprint = request.files['fingerprint']

			# Grab Image Name
			pic_filename1 = secure_filename(profile_pic.filename)
			pic_filename2= secure_filename(profile_pic2.filename)
			pic_filename3 = secure_filename(fingerprint.filename)
			# Set UUID
			pic_name = str(uuid.uuid1()) + "_" + pic_filename1
			pic_name2 = str(uuid.uuid1()) + "_" + pic_filename2
			fingerprint = str(uuid.uuid1()) + "_" + pic_filename3
			# Save That Image
			saver = request.files['profile_pic']
			saver2 = request.files['profile_pic2']
			saver1 = request.files['fingerprint']
			# Change it to a string to save to db
			profile_pic = pic_name
			#file2 = request.files["profile_pic"]
			#hashed_pw = generate_password_hash(form.password_hash.data, "sha256")
			user = Crimerecords(first_name=form.first_name.data,
			 last_name=form.last_name.data, 
			 mother_name=form.mother_name.data,
             motive=form.motive.data,
             nationality=form.nationality.data,
             phone_No=form.phone_no.data,
             case_id=form.case_id.data,
             medicals=form.medicals.data,
             address=form.address.data,
			 crime_type=form.crime_type.data, 
			 wanted=form.wanted.data,
			 gender=form.gender.data,
			 dob=form.dob.data,
			 profile_pic= pic_name,
			 profile_pic2= pic_name2,
			 fingerprint= fingerprint,
			 caught_by= current_user.id,
			 station=current_user.station)
			db.session.add(user)
			db.session.commit()
			saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
			saver1.save(os.path.join(app.config['UPLOAD_FINGER'], fingerprint))
			saver2.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name2))
			#file2.save(os.path.join(app.config['UPLOAD_FOLDER'],file2.filename))
			
			
		form.first_name.data= ''
		form.last_name.data = ''
		form.mother_name.data = ''
		form.motive.data = ''
		form.nationality.data = ''
		form.case_id.data = ''
		form.phone_no.data = ''
		form.case_id.data = ''
		form.medicals.data = ''
		form.address.data = ''
		form.crime_type.data = ''
		form.wanted.data = ''
		form.gender.data = ''
		form.dob.data = ''
		# form.profile_pic2.data = ''
		# form.fingerprint.data = ''
		flash("RECORD SUCCEFULLY ADDED!!!")
		return redirect(url_for('view'))
	our_users = Crimerecords.query.order_by(Crimerecords.date_added)
	return render_template("addcrime.html",
		form=form,
		name=name,
		our_users=our_users)



@app.route('/details_crime/<int:id>', methods=['GET', 'POST'])
@login_required
def details_crime(id):
	form = CrimeForm()
	person = Crimerecords.query.get(id)
	birth_date = person.dob
	today = datetime.utcnow()
	name = Crimerecords.query.get_or_404(id)
	age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
	return render_template('details_crime.html', 
	 			form=form,
				name = name,
				id = id,age=age)

def calculate(born):
	today = datetime.now()
	return today.year - born.year - ((today.month, today.day)<(born.month, born.day))
#Create Dashboard Page
@app.route('/dashboard/<int:id>', methods=['GET', 'POST'])
#@login_required
def dashboard(id):
	form = PoliceForm()
	id = current_user.id
	name_to_update = User.query.get_or_404(id)
	birth_date = name_to_update.dob
	today = datetime.utcnow()
	age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

	if request.method == "POST":
		name_to_update.first_name = request.form['first_name']
		name_to_update.last_name = request.form['last_name']
		name_to_update.batchno = request.form['batchno']
		# age = (datetime.today() - dob).days/365
		# age = round(age, 1)
		# name_to_update.username = request.form['username']
		# name_to_update.about_author = request.form['about_author']
		# Check for profile pic
		if request.files['profile_pic']:
			name_to_update.profile_pic = request.files['profile_pic']

			# Grab Image Name
			pic_filename = secure_filename(name_to_update.profile_pic.filename)
			# Set UUID
			pic_name = str(uuid.uuid1()) + "_" + pic_filename
			# Save That Image
			saver = request.files['profile_pic']
			

			# Change it to a string to save to db
			
			name_to_update.profile_pic = pic_name
			try:
				db.session.commit()
				saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
				flash("User Updated Successfully!")
				return render_template("dashboard.html", 
					form=form,
					name_to_update = name_to_update,
				id = id,age=age)
			except:
				flash("Error!  Looks like there was a problem...try again!")
				return render_template("dashboard.html", 
					form=form,
					name_to_update = name_to_update,age=age)
		else:
			db.session.commit()
			flash("User Updated Successfully!")
			return render_template("dashboard.html", 
				form=form, 
				name_to_update = name_to_update,
				id = id,age=age)
	else:
		return render_template("dashboard.html", 
				form=form,
				name_to_update = name_to_update,
				id = id ,age=age)
	return render_template('dashboard.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
	name = None
	form = PoliceForm(active=True)
	if form.validate_on_submit() and request.method == "POST":
		user = User.query.filter_by(batchno=form.batchno.data).first()
		if user is None:
			# Hash the password!!!
			profile_pic = request.files['profile_pic']

			# Grab Image Name
			pic_filename = secure_filename(profile_pic.filename)
			# Set UUID
			pic_name = str(uuid.uuid1()) + "_" + pic_filename
			# Save That Image
			saver = request.files['profile_pic']
			# Change it to a string to save to db
			profile_pic = pic_name
			#file2 = request.files["profile_pic"]
			hashed_pw = generate_password_hash(form.password_hash.data, "sha256")
			user = User(batchno=form.batchno.data, 
               first_name=form.first_name.data, 
               last_name=form.last_name.data, 
               rank=form.rank.data,
               Personal_email=form.personal_email.data,
               Phone_No=form.phone_no.data,
               gender=form.gender.data,
               station=current_user.station,
               dob=form.dob.data,
               Supervisor_id=current_user.batchno,
               profile_pic= pic_name, 
               password_hash=hashed_pw, active=True)
			db.session.add(user)
			db.session.commit()
			saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
			#file2.save(os.path.join(app.config['UPLOAD_FOLDER'],file2.filename))
			
			
		form.personal_email= ''
		form.batchno.data = ''
		form.first_name.data = ''
		form.profile_pic.data = ''
		form.last_name.data = ''
		form.gender.data = ''
		form.dob.data = ''
		form.rank.data = ''
		form.password_hash.data = ''
		flash("added")
		return redirect(url_for('register'))
	our_users = User.query.order_by(User.date_added)
	return render_template("register.html",
		form=form,
		name=name,
		our_users=our_users)


# Update Database Record
@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
	form = PoliceForm(active=True)
	name_to_update = User.query.get_or_404(id)
	if request.method == "POST":
		name_to_update.rank = request.form['rank']
		# name_to_update.active = request.form['active']
		name_to_update.station = request.form['station']
		try:
			db.session.commit()
			flash("User Updated Successfully!")
			return render_template("update.html", 
				form=form,
				name_to_update = name_to_update, id=id)
		except:
			flash("Error!  Looks like there was a problem...try again!")
			return render_template("update.html", 
				form=form,
				name_to_update = name_to_update,
				id=id)
	else:
		return render_template("update.html", 
				form=form,
				name_to_update = name_to_update,
				id = id)

# Update Database Record
@app.route('/edit_crime/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_crime(id):
	form =CrimeForm()
	name_to_update = Crimerecords.query.get_or_404(id)
	if request.method == "POST":
		name_to_update.last_name = request.form['last_name']
		name_to_update.first_name = request.form['first_name']
		try:
			db.session.commit()
			flash("User Updated Successfully!")
			return render_template("edit_crime.html", 
				form=form,
				name_to_update = name_to_update, id=id)
		except:
			flash("Error!  Looks like there was a problem...try again!")
			return render_template("edit_crime.html", 
				form=form,
				name_to_update = name_to_update,
				id=id)
	else:
		return render_template("edit_crime.html", 
				form=form,
				name_to_update = name_to_update,
				id = id)


@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    filter_option = request.form['filter_option']
    if filter_option == 'last_name':
        results = User.query.filter(User.last_name.like(f'%{search_term}%')).all()
    elif filter_option == 'first_name':
        results = User.query.filter(User.first_name.like(f'%{search_term}%')).all()
    elif filter_option=='c_first_name':
          results=Crimerecords.query.filter(Crimerecords.first_name.like(f'%{search_term}%')).all()
    return render_template('results.html',results=results)

@app.route('/upload', methods=['POST'])
def upload():
    fingerprint = request.files['file'].read()
    fingerprint = Crimerecords(name=fingerprint)
    db.session.add(fingerprint)
    db.session.commit()
    return jsonify({'message': 'Fingerprint uploaded successfully!'})


class DefaultModelView(flask_admin_sqla.ModelView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def is_accessible(self):
        return current_user.is_authenticated 

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated 

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))

    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            flash('Please log in first...', 'error')
            next_url = request.url
            login_url = '%s?next=%s' % (url_for('login'), next_url)
            return redirect(login_url)
        # import pdb;pdb.set_trace()
        if current_user.id == 2 or current_user.id == 1:
            return super(MyAdminIndexView,self).index()
        else:
            flash('YOU ARE NOT AUTHORIZE TO ACCESS THIS PAGE!!!')
            return redirect(url_for("index"))
        
  
# further in app.py
admin = Admin(
        app,
        name='DATABASE',
         template_mode='bootstrap4',
        index_view=MyAdminIndexView()
    )


def __init__(self,id,uname, password_hash):
    self.id = id
    self.username = uname
    self.password_hash = password_hash
    #self.id = id


class DefaultModelView(ModelView):
	column_exclude_list = ['password_hash', ]
	column_searchable_list = ['first_name', 'last_name']
	can_export = True
	
	can_view_details = True
	edit_modal = True
	column_editable_list = ['first_name', 'last_name','active','batchno']
	

	
class CrimerecordsView(ModelView):
	column_exclude_list = ['Profile_Pic', ]
	column_exclude_list = ['ProfilePic2', ]
	column_searchable_list = ['first_name', 'last_name']
	can_export = True
	can_view_details = True

class MessageView(ModelView):
	can_export = True
	can_view_details = True

class LocationView(ModelView):
	can_export = True
	can_view_details = True

admin.add_view(DefaultModelView(User, db.session))
admin.add_link(MenuLink(name='Logout', category='', url='/logout'))
admin.add_view(FileAdmin(path, '/static/', name='Static Files'))
admin.add_view(LocationView(Location, db.session))
# admin.add_view(NotificationsView(name='Notifications', endpoint='notify'))
admin.add_view(MessageView(Message, db.session))
admin.add_view(CrimerecordsView(Crimerecords, db.session))
admin.add_view(ModelView(Role, db.session))
# class MyModelView(sqla.ModelView):

#     def is_accessible(self):
#         if not current_user.is_active or not current_user.is_authenticated:
#             return False

#         # if current_user.has_role('superuser'):
#         #     return True

#         return False

#     def _handle_view(self, name, **kwargs):
#         """
#         Override builtin _handle_view in order to redirect users when a view is not accessible.
#         """
#         if not self.is_accessible():
#             if current_user.is_authenticated:
#                 # permission denied
#                 abort(403)
#             else:
#                 # login
#                 return redirect(url_for('security.login', next=request.url))

# Create Login Page


@app.route('/match', methods=['GET', 'POST'])
def match():
    if request.method == 'POST':
        # get the uploaded file
        file = request.files['file']
        # read the file as an image
        try:
            file_bytes = file.read()
            if not file_bytes:
                raise ValueError("Error: Empty file.")
            sample = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), cv2.IMREAD_UNCHANGED)
            if sample is None:
                raise ValueError("Error: Invalid image file.")
        except Exception as e:
            print(str(e))  # Print the error message for debugging purposes
            return render_template('error.html', error=str(e))

    else:
        # load a default image
        return render_template('match.html')

    best_score = 0
    filename = None
    image = None
    kp1, kp2, mp = None, None, None

    counter = 0
    for record in Crimerecords.query.limit(1000).all():
        file = record.fingerprint
        if counter % 10 == 0:
            print(counter)
            print(file)

        counter += 1
        fingerprint_image = cv2.imread("static/images/fingerprint/" + file)
        if fingerprint_image is None:
            print("Error: Could not read fingerprint image")
            continue

        sift = cv2.SIFT_create()
        keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None)
        keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)

        matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, {}).knnMatch(descriptors_1, descriptors_2, k=2)
        match_points = []

        for p, q in matches:
            if p.distance < 0.1 * q.distance:
                match_points.append(p)

        keypoints = 0
        if len(keypoints_1) < len(keypoints_2):
            keypoints = len(keypoints_1)
        else:
            keypoints = len(keypoints_2)

        if len(match_points) / keypoints * 100 > best_score:
            best_score = len(match_points) / keypoints * 100
            filename = file
            image = fingerprint_image
            kp1, kp2, mp = keypoints_1, keypoints_2, match_points
            kp1, kp2, mp = keypoints_1, keypoints_2, match_points

    print("BEST MATCH:" + file)
    print("Score: " + str(best_score))

    if image is None:
        return render_template('error.html', error="Error: No matching image found.")

    try:
        result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
        result = cv2.resize(result, None, fx=4, fy=4)

        # Convert the image to a PNG format
        _, buffer = cv2.imencode('.png', result)
        result = buffer.tobytes()
        b64_result = base64.b64encode(result).decode('utf-8')
    except Exception as e:
        print(str(e))  # Print the error message for debugging purposes
        return render_template('error.html', error=str(e))

    if filename:
        best_match = Crimerecords.query.filter_by(fingerprint=filename).first()
    else:
        best_match = None

    return render_template('match.html', result=b64_result, best_match=best_match, score=best_score)

    
@app.route('/face_match', methods=['GET', 'POST'])
def face_match():
    if request.method =='POST':
     file = request.files['file']
    # Load the image of the face you want to match
     face_to_match = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    else:
      return render_template ("match_faces.html")
# Convert the face to grayscale
    gray_face_to_match = cv2.cvtColor(face_to_match, cv2.COLOR_BGR2GRAY)

# Create an ORB object for feature detection and description
    orb = cv2.ORB_create()

# Get the keypoints and descriptors for the face to match
    kp1, des1 = orb.detectAndCompute(gray_face_to_match, None)

# Create a list of all the images in the folder
    image_files = [f for f in os.listdir("static\images") if f.endswith(".jpg")]

# Initialize variables for tracking the best match
    best_match_image = None
    best_match_distance = np.inf

# Loop through each image in the folder and find the best match
    for image_file in image_files:
    # Load the image
     image = cv2.imread(os.path.join("static\images", image_file))
    
    # Convert the image to grayscale
     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Get the keypoints and descriptors for all faces in the image
     kp2, des2 = orb.detectAndCompute(gray_image, None)
    
    # Create a brute-force matcher object
     bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
    # Match the descriptors for the face to match and the current face in the loop
     matches = bf.match(des1, des2)
    
    # Calculate the distance between the two feature sets
     distance = sum([match.distance for match in matches])
    
    # Check if this is the best match so far
     if distance < best_match_distance:
         best_match_distance = distance
         best_match_image = image_file

# Print the best match image file name
    print("Best match: " + best_match_image)
    return render_template ("match_faces.html",best_match =best_match_image, best_score =best_match_distance)

@app.route('/map')
def map():
    # get all locations from the database
    locations = Location.query.all()

    # create a Folium map centered on the first location
    map = folium.Map(location=[locations[0].latitude, locations[0].longitude], zoom_start=10)

    # add a marker for each location to the map
    for location in locations:
        folium.Marker(location=[location.latitude, location.longitude], popup=location.name).add_to(map)

    # render the map using an HTML template
    return render_template('map.html', map=map._repr_html_())



@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(batchno=form.batchno.data).first()
		if user :
			# Check the hash
			if check_password_hash(user.password_hash, form.password.data)and user.active == True:
				login_user(user)
				flash("Login Succesfull!!")
				return redirect(url_for('index'))
			elif user.active == False:
				flash("Account Disabled - Ask Admin for permission!")
			else:
				flash("password incorrect")	
		else:
			flash("That User Doesn't Exist! Try Again...")
	return render_template('login.html', form=form)


# Create Logout Page
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	flash("You Have Been Logged Out!  Thanks For Stopping By...")
	return redirect(url_for('login'))    


@app.route('/delete/<int:id>')
def delete(id):
    data = User.query.get(id)
    db.session.delete(data)
    db.session.commit()
    flash("deleted succesfully")
    return redirect('/allofficer')


@app.route('/deletecrme/<int:id>')
def deletecrme(id):
    data = Crimerecords.query.get(id)
    db.session.delete(data)
    db.session.commit()
    flash("deleted succesfully")
    return redirect('/view')	


@app.route("/", defaults={"path": ""})
@app.route("/<string:path>")
@app.route("/<path:path>")
def catch_all(path):
    """Catches all routes and returns 404 if url does not much
    """
    
    return render_template('404.html')


@app.route('/adminofficer/<int:id>')
def adminofficer(id):
    
    flash("deleted succesfully")
    return render_template("Admin/adminofficer.html")

@property
def password(self):
		raise AttributeError('password is not a readable attribute!')

@password.setter
def password(self, password):
		self.password_hash = generate_password_hash(password)

def verify_password(self, password):
	return check_password_hash(self.password_hash, password)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")