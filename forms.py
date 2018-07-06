from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError
import datetime

class ContactForm(FlaskForm):
   name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")
   
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   
   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'), 
      ('py', 'Python')])
   submit = SubmitField("Send")

class DateTimeForm(FlaskForm):
   now = str(datetime.datetime.now())
   submit = SubmitField("Get date and time")

class USBStatusForm(FlaskForm):
   submit = SubmitField("Get USB status")

class SerialStatusForm(FlaskForm):
   submit = SubmitField("Get Serial USB status")

class CommandForm(FlaskForm):
   parametar = TextField("Parametar za komandu: ")
   filterfield = TextField("Filter za komandu: ")
   submit = SubmitField("Pokreni komandu")

class SubmitForm(FlaskForm):
   submit = SubmitField("Run command")

class PaperMoveForm(FlaskForm):
   lines = SelectField("Number of lines", choices = [("3","3 Lines"),("5","5 Lines"),("10","10 Lines")])
   submit = SubmitField("Move paper")
