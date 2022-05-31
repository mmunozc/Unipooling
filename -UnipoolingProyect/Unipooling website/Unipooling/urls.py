from django.contrib import admin
from django.urls import path
from app import views as appViews
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appViews.principal, name="principal"),
    path('register/', appViews.register, name="register"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('rutas/', appViews.rutas, name="rutas"),
    path('registroRuta/', appViews.registrarRutaView, name="registroRuta"),
    path('horario/', appViews.horario, name="horario"),
    path('vehiculo/', appViews.vehiculo, name="vehiculo"),
    path('datos/', appViews.datos, name="cuenta"),
    path('datosVehiculo/<pk>/', appViews.datosVehiculo, name="Datos Vehiculo"),
    path('contacto/<pk>/', appViews.contacto, name="contacto"),
]
