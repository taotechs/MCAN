from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=8),
        EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    
    # Profile fields
    full_name = StringField('Full Name', validators=[DataRequired(), Length(1, 64)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(1, 20)])
    lga = StringField('LGA', validators=[DataRequired(), Length(1, 64)])
    batch = StringField('Batch', validators=[DataRequired(), Length(1, 20)])
    ppa = StringField('PPA', validators=[DataRequired(), Length(1, 128)])
    profession = StringField('Profession', validators=[DataRequired(), Length(1, 64)])
    
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class ProfileForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(), Length(1, 64)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(1, 20)])
    address = StringField('Address', validators=[Length(0, 128)])
    lga = StringField('LGA', validators=[DataRequired(), Length(1, 64)])
    batch = StringField('Batch', validators=[DataRequired(), Length(1, 20)])
    ppa = StringField('PPA', validators=[DataRequired(), Length(1, 128)])
    profession = StringField('Profession', validators=[DataRequired(), Length(1, 64)])
    bio = TextAreaField('Bio')
    profile_picture = StringField('Profile Picture URL')
    submit = SubmitField('Update Profile') 