from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("usersProfile/", views.usersProfile, name = 'usersProfile'),
    path("basicQuestion/", views.basicQuestions, name = 'basicQuestions'),
    path("diccionario/", views.diccionario, name = 'diccionario'),
    path("verDatos/", views.verDatos, name = 'verDatos'),
    path("crearDatos/", views.crearDatos, name = 'crearDatos'),
    path("modificarDatos/", views.modificarDatos, name = 'modificarDatos'),
    path("eliminarDatos/", views.eliminarDatos, name = 'eliminarDatos'),
    #KNearestNeighbors
    path("modificarDatosForm/", views.modificarDatosForm, name = 'modificarDatosForm'),
    path("KNearestNeighborsGravedad/", views.KNearestNeighborsGravedad, name = 'KNearestNeighborsGravedad'),
    path("KNearestNeighborsClaseSiniestro/", views.KNearestNeighborsClaseSiniestro, name = 'KNearestNeighborsClaseSiniestro'),
    path("KNearestNeighborsEstado/", views.KNearestNeighborsEstado, name = 'KNearestNeighborsEstado'),
    #RandomForestClassifier
    path("RandomForestClassifierGravedad/", views.RandomForestClassifierGravedad, name = 'RandomForestClassifierGravedad'),
    path("RandomForestClassifierClaseSiniestro/", views.RandomForestClassifierClaseSiniestro, name = 'RandomForestClassifierClaseSiniestro'),
    path("RandomForestClassifierEstado/", views.RandomForestClassifierEstado, name = 'RandomForestClassifierEstado'),
    #LogisticRegression
    path("LogisticRegressionGravedad/", views.LogisticRegressionGravedad, name = 'LogisticRegressionGravedad'),
    path("LogisticRegressionClaseSiniestro/", views.LogisticRegressionClaseSiniestro, name = 'LogisticRegressionClaseSiniestro'),
    path("LogisticRegressionEstado/", views.LogisticRegressionEstado, name = 'LogisticRegressionEstado')
]