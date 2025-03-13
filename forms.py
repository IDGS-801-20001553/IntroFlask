from wtforms import Form
from wtforms import StringField, PasswordField,EmailField, BooleanField,SubmitField, IntegerField, RadioField
from wtforms import validators


class UserForm(Form):
    mat = StringField("Matricula",[
        validators.DataRequired(message="El campo es requerido")
    ])
    nom = StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido")
    ])
    ap = StringField("Apellido",[
        validators.DataRequired(message="El campo es requerido")
    ])
    correo = EmailField("Correo",[
        validators.DataRequired(message="El campo es requerido")
    ])


class ZodiacoForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido")
        ])
    apaterno = StringField("Apellido Paterno", [
        validators.DataRequired(message="El campo es requerido")
        ])
    amaterno = StringField("Apellido Materno", [
        validators.DataRequired(message="El campo es requerido")
        ])
    dia = IntegerField("Día", [
        validators.DataRequired(message="El campo es requerido")
        ])
    mes = IntegerField("Mes", [
        validators.DataRequired(message="El campo es requerido")
        ])
    anio = IntegerField("Año", [
        validators.DataRequired(message="El campo es requerido")
        ])
    sexo = RadioField("Sexo", choices=[("Masculino", "Masculino"), ("Femenino", "Femenino")], validators=[
        validators.DataRequired(message="El campo es requerido")
        ])