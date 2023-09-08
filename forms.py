from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class AddPetForm(FlaskForm):
    """Add a furry friend"""

    name = StringField("Pet name", validators=[InputRequired(message='Name cannot be blank')])
    species = SelectField("Pet species", choices=[('cat', 'cat'), ('dog','dog'),('porcupine','porcupine')], validators=[InputRequired(message='Species cannot be blank')])
    photo_url = StringField("Pet photo", validators=[Optional(), URL(require_tld=True, message='Must be a valid URL')])
    age = FloatField("Pet age", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 1 and 30")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Pet availabile")
