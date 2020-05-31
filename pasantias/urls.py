from django.urls import path 
from . import views 

app_name = 'pasantias' 
urlpatterns = [
    path('', views.index, name='index'),
    
    path('coordinador/', views.coordinador, name= "coordinador"),
    path('estudiante/', views.estudiante, name= "estudiante"),

    #login
    path('ingresar/', views.form_Ing, name='form_Ing'),
    path('Ing_post/', views.post_Ing, name="post_Ing"),
    
    #logout
    path('logout/', views.view_logout, name='view_logout'),

    #registro
    path('registro/', views.form_Reg, name='form_Reg'),
    path('Reg_post/', views.post_Reg, name="post_Reg"),

    #crea convenio
    path('convenio_post/', views.post_crea_convenio, name="post_crea_convenio"),

    #crea solicitud
    path('solicitud_post/', views.post_crea_solicitud, name="post_crea_solicitud"),

    #cambiar estado
    path('c_estado_post/', views.post_cambia_solicitud, name='post_cambia_solicitud')

 
]