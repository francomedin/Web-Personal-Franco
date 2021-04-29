from .views import ContactCreate
from django.urls import path

urlpatterns = [
    path('', ContactCreate.as_view(), name='contact'),
]
