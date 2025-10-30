from wtforms import StringField, FloatField, EmailField, PasswordField, IntegerField, SelectField, RadioField
from wtforms.validators import InputRequired, NumberRange, Email
from wtforms import validators
from wtforms import Form
from flask_wtf import FlaskForm 
# ----- FIGURAS -----
class FiguraForm(Form):
    figura = RadioField('FIGURAS:', choices=[
        ('rectangulo', 'RECTANGULO'),('circulo', 'CIRCULO'),
        ('triangulo', 'TRIANGULO'), ('pentagono', 'PENTAGONO')], 
        validators=[validators.DataRequired()])
    num1 = FloatField('numero 1:',
        [validators.DataRequired(message="El numero es obligatorio")])
    num2 = FloatField('numero 2:',
        [validators.DataRequired(message="El numero es obligatorio")]) 
# ----- ALUMNOS -----
class UserForm(Form):
    matricula = IntegerField('Matricula',
        [validators.DataRequired(message="La matricula es obligatoria")])
    
    nombre = StringField('Nombre',
        [validators.DataRequired(message="El nombre es obligatorio")])
    
    apellido = StringField('Apellido',
        [validators.DataRequired(message="El apellido es obligatorio")])
    
    email = EmailField('Email',
        [validators.Email(message="El email no es valido")])