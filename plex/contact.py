from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from flask_wtf import FlaskForm
import json
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

bp = Blueprint('contact', __name__)

class ContactForm(FlaskForm):
    firstname = StringField("FirstName",validators=[DataRequired()])
    lastname = StringField("LastName",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired()])
    phone = StringField("Phone")
    message = TextAreaField("Message",validators=[DataRequired()])

@bp.route("/contact", methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if request.method == 'POST':
        firstname =  request.form["firstname"]
        lastname =  request.form["lastname"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        dictionary = {'firstname':firstname, 'lastname':lastname, 'email':email, 'phone':phone ,'message':message}
        json_object = json.dumps(dictionary, indent=4)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
        flash("Your message was sent.")
        return redirect(url_for('movies.library'))
    else:
        return render_template('contact/contact.html', form=form)