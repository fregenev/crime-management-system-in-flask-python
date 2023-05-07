from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, PasswordField, BooleanField, DateField, RadioField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from flask_wtf.file import FileField
from wtforms import validators
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
	# station = SelectField("station", choices=[('del', 'deltasate'), ('ab', 'abj'), ('lag','lagos')], validators=[DataRequired()])
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
	# rank = SelectField("rank", choices=[('cpp', 'c++'), ('py', 'python'), ('ja','java')], validators=[DataRequired()])
	wanted = RadioField("Wanted", choices=[('YES', 'YES'), ('NO', 'No')], validators=[DataRequired()])
	gender = RadioField("Gender", choices=[('MALE', 'Male'), ('FEMALE', 'Female')], validators=[DataRequired()])
	crime_type = SelectField("crime", choices=[('steal', 'steal'), ('fight', 'fight'), ('cry','cry')], validators=[DataRequired()])
	dob = DateField("dob", validators=[DataRequired()])
	profile_pic = FileField("Profile Pic")
	profile_pic2 = FileField("Profile Pic2")
	fingerprint = FileField("fingerprint")
	submit = SubmitField("Submit")

class PasswordForm(FlaskForm):
	batchno = StringField("What's Your Email", validators=[DataRequired()])
	password_hash = PasswordField("What's Your Password", validators=[DataRequired()])
	submit = SubmitField("Submit")

class activeForm(FlaskForm):
	active = BooleanField("DISABLE ACCOUNT")
	submit = SubmitField("Submit")	

class SearchForm(FlaskForm):
    search_term = StringField('Enter your search term:')
    filter_option = SelectField(
        'Filter by:',
        choices=[('first_name', 'first_name'), ('last_name', 'last_name')]
    )
    submit = SubmitField('Search')