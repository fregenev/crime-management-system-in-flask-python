from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, PasswordField, BooleanField, DateField, RadioField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from flask_wtf.file import FileField
from wtforms import validators
from models import Message,User,Crimerecords,Location
from wtforms.validators import DataRequired, EqualTo,Email, Length
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField,RadioField,IntegerField, DateField ,PasswordField, BooleanField, ValidationError, TextAreaField, SelectField, HiddenField
from wtforms import StringField

class MessageForm(FlaskForm):
    recipient_id = SelectField('Recipient', validators=[DataRequired()])
    picture = FileField('Picture')
    text = StringField('Message', validators=[DataRequired()], widget=TextArea())


# Create A Search Form
class LoginForm(FlaskForm):
	# This is checking the login info given by user, and checking
    # if the database contains the user and if the password provided
    # is the correct password.
	batchno = StringField("Batchno", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Submit")

# Create a Form Class to regster users
class PoliceForm(FlaskForm):
	# This the where all the info from the Registration_Page gets store in.
    # All the different attributes are each a input field in Registration_Page
    # See the Registration_Page.html file to see how they are connected
	def validate_batchno(self, batchno_to_check):
		user = User.query.filter_by(batchno=batchno_to_check.data).first()
		if user:
			raise ValidationError('Batch No already exists! Please try a different Batch no')
	
	def validate_batchno(self, personal_email_to_check):
		personal_email = User.query.filter_by(Personal_email=personal_email_to_check.data).first()
		if personal_email:
			raise ValidationError('Batch No already exists! Please try a different Batch no')
	

	batchno = StringField("Batchno", validators=[DataRequired()])
	first_name = StringField("First_name", validators=[DataRequired()])
	last_name = StringField("Last name", validators=[DataRequired()])
	phone_no = IntegerField("Phone Number", validators=[DataRequired()])
	personal_email = StringField("Email Address", validators=[Email()])
	active = BooleanField('active', default="checked")
	rank = SelectField("Rank", choices = [('15','Inspector General of Police'),
				       ('14', 'Additional Inspector General of Police'),
					   ('13', 'Deputy Inspector General of Police'),
					   ('12', 'Additional Deputy Inspector General of Police'),
					     ('11','Superintendent of Police'),
                   ('10','Additional Superintendent of Police'),
				   ('8', 'Senior Assistant Superintendent of Police'),
				   ('7', 'Assistant Superintendent of Police'),
				   ('6', 'Inspector'),
				   ('5', 'Sub Inspector'),
				     ('4','Sergent'),
					 ('3', 'Assisteant Sub Inspector'),
					 ('2', 'Nayek'),
					 ('1', 'Constable')],
					   validators=[DataRequired()])
	gender = RadioField("Gender", choices=[('MALE', 'Male'), ('FEMALE', 'Female')], validators=[DataRequired()])
	dob = DateField("DOB", validators=[DataRequired()])
	password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo('password_hash2', message='Passwords Must Match!')])
	password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
	profile_pic = FileField("Image")
	submit = SubmitField("Submit")

# define the form for updating the user's disabled status
class PasswordUpdateForm(FlaskForm):
    old_password = PasswordField('Old Password', [
        validators.DataRequired(),
        validators.Length(min=2, message='Password must be at least 8 characters long')
    ])
    new_password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.Length(min=2, message='Password must be at least 8 characters long'),
        validators.EqualTo('confirm_password', message='Passwords do not match')
    ])
    confirm_password = PasswordField('Confirm New Password', [
        validators.DataRequired(),
        validators.Length(min=2, message='Password must be at least 8 characters long')
    ])
    submit = SubmitField("Update")

class CrimeForm(FlaskForm):
	#  This the where all the info to store a criminal in database is first store in.
	
	first_name = StringField("FIRST_NAME", validators=[DataRequired()])
	last_name = StringField("LAST_NAME", validators=[DataRequired()])
	mother_name = StringField("MOTHER_NAME", validators=[DataRequired()])
	motive = StringField("MOTIVE", validators=[DataRequired()])
	nationality = StringField("NATIONALITY", validators=[DataRequired()])
	phone_no = IntegerField("PHONE_NUMBER", validators=[DataRequired()])
	case_id = StringField("CASE_ID", validators=[DataRequired()])
	medicals = StringField("MEDICAL", validators=[DataRequired()])
	address = StringField("ADDRESS", validators=[DataRequired()], widget=TextArea())
	wanted = RadioField("WANTED", choices=[('YES', 'YES'), ('NO', 'No')], validators=[DataRequired()])
	gender = RadioField("GENDER", choices=[('MALE', 'Male'), ('FEMALE', 'Female')], validators=[DataRequired()])
	crime_type = SelectField("TYPE OF CRIME", choices=[('steal', 'steal'), ('fight', 'fight'), ('cry','cry')], validators=[DataRequired()])
	dob = DateField("DATE OF BIRTH", validators=[DataRequired()])
	profile_pic = FileField("PHOTO")
	profile_pic2 = FileField("EVIDENCE")
	fingerprint = FileField("UPLOAD FINGER PRINT")
	submit = SubmitField("SUBMIT")

class PasswordForm(FlaskForm):
	batchno = StringField("What's Your Email", validators=[DataRequired()])
	password_hash = PasswordField("What's Your Password", validators=[DataRequired()])
	submit = SubmitField("Submit")


class SearchForm(FlaskForm):
    search_term = StringField('Enter your search term:')
    filter_option = SelectField(
        'Filter by:',
        choices=[('first_name', 'first_name'), ('last_name', 'last_name')]
    )
    submit = SubmitField('Search')
    
class PoliceUpdateForm(FlaskForm):
	station = SelectField("station", choices=[('del', 'deltasate'), ('ab', 'abj'), ('lag','lagos')])
	active = BooleanField("DISABLE ACCOUNT")
	rank = SelectField("Rank", choices = [('Inspector General of Police','Inspector General of Police'),
				       ('Additional Inspector General of Police', 'Additional Inspector General of Police'),
					   ('Deputy Inspector General of Police', 'Deputy Inspector General of Police'),
					   ('Additional Deputy Inspector General of Police', 'Additional Deputy Inspector General of Police'),
					     ('Superintendent of Police','Superintendent of Police'),
                   ('Additional Superintendent of Police','Additional Superintendent of Police'),
				   ('Senior Assistant Superintendent of Police', 'Senior Assistant Superintendent of Police'),
				   ('Assistant Superintendent of Police', 'Assistant Superintendent of Police'),
				   ('Inspector', 'Inspector'),
				   ('Sub Inspector', 'Sub Inspector'),
				     ('Sergent','Sergent'),
					 ('Assisteant Sub Inspector', 'Assisteant Sub Inspector'),
					 ('Nayek', 'Nayek'),
					 ('Constable', 'Constable')],
					   )
	password_hash = PasswordField('Password', validators=[EqualTo('password_hash2', message='Passwords Must Match!')])
	password_hash2 = PasswordField('Confirm Password')
	submit = SubmitField('submit')



class LocationForm(FlaskForm):
    about = StringField('ABOUT', validators=[DataRequired()],widget=TextArea())
    station_name = StringField('STATION NAME', validators=[DataRequired()])
    latitude = IntegerField('LATITUDE', validators=[DataRequired()])
    longitude = IntegerField('LONGITUDE', validators=[DataRequired()])
    submit =SubmitField('Submit')