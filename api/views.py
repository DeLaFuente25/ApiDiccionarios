from api import app
from flask import request, session, flash
from flask import render_template, redirect, url_for
from models import db, User
import forms


@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        return render_template('home.html', username=username)
    else:
        return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        session['username'] = login_form.username.data

        success_message = 'El usuario ha sido autenticado con exito'
        flash(success_message)
        return redirect(url_for('home'))

    return render_template('login.html', form=login_form)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('home'))


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    create_form = forms.CreateUserForm(request.form)
    if request.method == 'POST' and create_form.validate():
        user = User(
            username=create_form.username.data,
            password=create_form.password.data,
            email=create_form.email.data
        )
        db.session.add(user)
        db.session.commit()

        success_message = 'Usuario registrado en la base de datos'
        flash(success_message)

        return redirect(url_for('home'))

    return render_template('create.html', form=create_form)
