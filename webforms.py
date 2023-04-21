from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, PasswordField, BooleanField, DateField, RadioField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, EqualTo, Length
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField,RadioField, DateField ,PasswordField, BooleanField, ValidationError, TextAreaField, SelectField, HiddenField
from wtforms import StringField

class MessageForm(FlaskForm):
    recipient_id = SelectField('Recipient', validators=[DataRequired()])
    picture = FileField('Picture')
    text = StringField('Message', validators=[DataRequired()], widget=TextArea())


# Create A Search Form
class LoginForm(FlaskForm):
	batchno = StringField("Batchno", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Submit")

# Create a Form Class to regster users
class PoliceForm(FlaskForm):
	batchno = StringField("batchno", validators=[DataRequired()])
	first_name = StringField("first_name", validators=[DataRequired()])
	last_name = StringField("Last name", validators=[DataRequired()])
	active = BooleanField('active', default="checked")
	rank = SelectField("rank", choices=[('cpp', 'c++'), ('py', 'python'), ('ja','java')], validators=[DataRequired()])
	gender = RadioField("Gender", choices=[('MALE', 'Male'), ('FEMALE', 'Female')], validators=[DataRequired()])
	station = SelectField("station", choices=[('del', 'deltasate'), ('ab', 'abj'), ('lag','lagos')], validators=[DataRequired()])
	dob = DateField("dob", validators=[DataRequired()])
	password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo('password_hash2', message='Passwords Must Match!')])
	password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
	profile_pic = FileField("Profile Pic")
	submit = SubmitField("Submit")

# define the form for updating the user's disabled status
class UpdateUserForm(FlaskForm):
    disabled = BooleanField('Disable Account')
    submit = SubmitField('Update')


# Create a Form Class to regster users
class CrimeForm(FlaskForm):
	first_name = StringField("first_name", validators=[DataRequired()])
	last_name = StringField("last_name", validators=[DataRequired()])
	mother_name = StringField("mother_name", validators=[DataRequired()])
	#
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