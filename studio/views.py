from django.shortcuts import redirect, render

from .forms import AppointmentForm
from .models import Artist, TattooDesign


def catalogue(request):
    designs = TattooDesign.objects.filter(is_available=True).select_related("artist")
    artists = Artist.objects.filter(is_accepting_bookings=True)
    return render(request, "studio/catalogue.html", {"designs": designs, "artists": artists})


def book_appointment(request):
    form = AppointmentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("booking-success")
    return render(request, "studio/booking.html", {"form": form})


def booking_success(request):
    return render(request, "studio/booking_success.html")