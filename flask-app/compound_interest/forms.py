from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, NumberRange
from compound_interest import db

class RegisterForm(FlaskForm):
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

    def validate_username(self, field):
        username_to_check = field.data
        users = list(db.users.find({"username": username_to_check}))
        num_of_users = len(users)
        if num_of_users != 0:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, field):
        email_address_to_check = field.data
        emails = list(db.users.find({"email": email_address_to_check}))
        num_of_emails = len(emails)
        if num_of_emails != 0:
            raise ValidationError('Email Address already exists! Please try a different email address')



class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label='Sign in')

class AddInvestmentForm(FlaskForm):
    initial_deposit = FloatField(label='Initial Deposit:', validators=[DataRequired(), NumberRange(min=1)])
    monthly_deposit = FloatField(label='Monthly Deposit:', validators=[DataRequired(), NumberRange(min=1)])
    yearly_interest = FloatField(label='Yearly Interest:', validators=[DataRequired(), NumberRange(min=0.1)])
    years_of_investment = IntegerField(label='Years of Investment:', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField(label='Add Investment')

class DeleteInvestmentForm(FlaskForm):
    submit = SubmitField(label='Delete')

