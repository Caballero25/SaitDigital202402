from django.urls import path
from .views import signPDF

urlpatterns = [
    path('signPDF', signPDF, name="sign-pdf"),
]
