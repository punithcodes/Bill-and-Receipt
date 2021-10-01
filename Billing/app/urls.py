from django.urls import path
from . import views

# Here I have defined the endpoint of the api
urlpatterns = [
    path('billing/', views.billing_api)
]
