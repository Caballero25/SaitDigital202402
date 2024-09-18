from django.urls import path
from .views import sendEmailContact

urlpatterns = [
    path("sendEmailContact/", sendEmailContact, name="EmailFormSubmit")
]