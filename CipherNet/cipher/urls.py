from django.urls import path

from . import views

app_name = "cipher"

urlpatterns = [
    path("", views.index, name="index"),
    path("hill_encryption", views.hill_encryption, name="hill_encryption"),
    path("hill_decryption", views.hill_decryption, name="hill_decryption"),
    path("blowfish_encryption", views.blowfish_encryption, name="blowfish_encryption"),
    path("blowfish_decryption", views.blowfish_decryption, name="blowfish_decryption")
    
]