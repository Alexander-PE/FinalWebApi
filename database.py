from peewee import *
from modelo import *

db = SqliteDatabase('Peliculas.db')

class t_Peliculas(Model):
    Nombre = TextField()
    Fecha = TextField()
    Comentario = TextField()
    Director = TextField()
    Actores = TextField()
    Trailer = TextField()
    Imagen = TextField()

    class Meta:
        database = db

db.connect()
db.create_tables([t_Peliculas])       


# Funcion para guardar los datos de las Películas

def GuardarPeliculas(p:Peliculas):
    tp = t_Peliculas()
    tp.Nombre = p.Nombre
    tp.Fecha = p.Fecha
    tp.Comentario = p.Comentario
    tp.Director = p.Director
    tp.Actores = p.Actores
    tp.Trailer = p.Trailer
    tp.Imagen = p.Imagen
    tp.save()


def CargarPeliculas():
    tp = []

    for p in t_Peliculas.select().dicts():
        tp.append(p)
    return tp


def ActualizarPeliculas(p:Peliculas):
    tp = t_Peliculas().get(t_Peliculas.id == p.id)
    tp.Nombre = p.Nombre
    tp.Fecha = p.Fecha
    tp.Comentario = p.Comentario
    tp.Director = p.Director
    tp.Actores = p.Actores
    tp.Trailer = p.Trailer
    tp.Imagen = p.Imagen
    tp.save()

def EliminarPeliculas(p:Peliculas):
    tp = t_Peliculas().get(t_Peliculas.id == p.id)
    tp.delete_instance(p.id)
    tp.save()