from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(66))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)


class Carrera(db.Model):
    __tablename__ = 'carreras'
    id = db.Column(db.Integer, primary_key=True)
    cod_carrera = db.Column(db.String(10), unique=True)
    nombre = db.Column(db.String(100))
    cod_facultad = db.Column(db.String(10))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)


class PlanEstudio(db.Model):
    __tablename__ = 'planes_estudio'
    id = db.Column(db.Integer, primary_key=True)
    cod_plan = db.Column(db.String(10), unique=True)
    nombre = db.Column(db.String(100))
    anio_inscripcion = db.Column(db.Integer)
    cod_periodo_inscripcion = db.Column(db.String(10))
    programa = db.Column(db.String(40))
    grado = db.Column(db.String(40))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)


class Materia(db.Model):
    __tablename__ = 'materias'
    id = db.Column(db.Integer, primary_key=True)
    cod_materia = db.Column(db.String(10), unique=True)
    nombre = db.Column(db.String(100))
    clasificacion = db.Column(db.String(40))
    orden = db.Column(db.Integer)
    anio = db.Column(db.Integer)
    descripcion_anio = db.Column(db.String(40))
    periodo_academico = db.Column(db.String(40))
    descripcion_periodo_academico = db.Column(db.String(40))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
