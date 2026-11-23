from django.urls import path

from . import views


urlpatterns = [
    path("", views.catalogue, name="catalogue"),
    path("book/", views.book_appointment, name="book-appointment"),
    path("booked/", views.booking_success, name="booking-success"),
]