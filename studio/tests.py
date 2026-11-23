from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Appointment, Artist, TattooDesign


class BookingFlowTests(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name="Amani", specialty="Fine line")
        self.design = TattooDesign.objects.create(
            title="Wildflower",
            style="Fine line",
            image_url="https://example.com/wildflower.jpg",
            starting_price=8500,
            artist=self.artist,
        )

    def test_catalogue_shows_available_designs(self):
        response = self.client.get(reverse("catalogue"))

        self.assertContains(response, "Wildflower")

    def test_booking_request_creates_pending_appointment(self):
        response = self.client.post(
            reverse("book-appointment"),
            {
                "name": "Maya N.",
                "email": "maya@example.com",
                "phone": "+254700000000",
                "placement": "Forearm",
                "preferred_date": date(2027, 1, 15).isoformat(),
                "artist": self.artist.pk,
                "design": self.design.pk,
                "notes": "Small size",
            },
        )

        self.assertRedirects(response, reverse("booking-success"))
        appointment = Appointment.objects.get(email="maya@example.com")
        self.assertEqual(appointment.status, Appointment.Status.PENDING)

    def test_booking_rejects_design_from_another_artist(self):
        other_artist = Artist.objects.create(name="Brian", specialty="Blackwork")
        response = self.client.post(
            reverse("book-appointment"),
            {
                "name": "Maya N.",
                "email": "maya@example.com",
                "phone": "+254700000000",
                "placement": "Forearm",
                "preferred_date": date(2027, 1, 15).isoformat(),
                "artist": other_artist.pk,
                "design": self.design.pk,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Appointment.objects.count(), 0)
        self.assertContains(response, "Choose a design by the selected artist.")