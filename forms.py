from wtforms import Form
from wtforms import StringField, PasswordField,EmailField, BooleanField,SubmitField, IntegerField
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
