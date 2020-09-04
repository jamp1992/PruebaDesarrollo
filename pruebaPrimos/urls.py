from django.urls import path
from pruebaPrimos import views

urlpatterns = [
    path('numeros_primos/<pk>', views.numeros_primos),
    path('numeros_primos_gemelos/<pk>', views.numeros_primos_gemelos)
]