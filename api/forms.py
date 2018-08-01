from wtforms import Form, StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField


class LoginForm(Form):
    username = StringField(
        'Nombre de usuario',
        [
            validators.length(min=4, max=25, message='Ingrese un usuario valido'),
            validators.required(message='El usuario el obligatorio')
        ]
    )
    password = PasswordField(
        'Password',
        [
            validators.length(min=4, max=25, message='Ingrese una clave valida'),
            validators.required(message='La clave el obligatoria')
        ]
    )


class CreateUserForm(Form):
    username = StringField(
        'Nombre de usuario',
        [
            validators.length(min=4, max=25, message='Ingrese un usuario valido'),
            validators.required(message='El usuario el obligatorio')
        ]
    )
    password = PasswordField(
        'Password',
        [
            validators.length(min=4, max=25, message='Ingrese una clave valida'),
            validators.required(message='La clave el obligatoria')
        ]
    )
    email = EmailField(
        'Correo electronico',
        [
            validators.required(message='El correo es obligatorio')
        ]
    )


class CreateCarreraForm(Form):
    cod_carrera = StringField(
        'Codigo de carrera',
        [
            validators.length(min=4, max=10, message='Ingrese un codigo valido'),
            validators.required(message='Debe ingresar un codigo para la carrera')
        ]
    )
    nombre = StringField(
        'Nombre',
        [
            validators.length(min=4, max=40, message='Ingrese un nombre valido'),
            validators.required(message="Debe ingresar un nombre para la carrera")
        ]
    )
    cod_facultad = StringField(
        'Codigo de facultad',
        [
            validators.length(min=4, max=10, message='Ingrese un codigo valido'),
            validators.required(message='Debe ingresar el codigo de la facultad a la que pertenece')
        ]
    )
