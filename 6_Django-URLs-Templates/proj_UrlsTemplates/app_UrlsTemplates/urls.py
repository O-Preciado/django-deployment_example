#URLs App: "app_UrlsTemplates"
'''
Archivo para declarar las URLs utilizadas dentro de la aplicación "app_UrlsTemplates"
'''
from django.urls import path
from app_UrlsTemplates import views

#Template Tagging
app_name = 'app_UrlsTemplates'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]