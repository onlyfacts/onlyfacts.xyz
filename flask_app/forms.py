from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class FactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[
        DataRequired(),
        Email(granular_message=True)
    ])
    facts = TextAreaField(label='Fact (If more than 1, separate by new line.)', validators=[DataRequired()])
    sources = TextAreaField(label='Source (If more than 1, separate by new line.)', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField(label="Submit")

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[
        DataRequired(),
        Email(granular_message=True)
    ])
    message = TextAreaField(label='Message')
    recaptcha = RecaptchaField()
    submit = SubmitField(label="Submit")
