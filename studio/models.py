from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=120)
    portrait_url = models.URLField(blank=True)
    is_accepting_bookings = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class TattooDesign(models.Model):
    title = models.CharField(max_length=120)
    style = models.CharField(max_length=80)
    image_url = models.URLField()
    starting_price = models.PositiveIntegerField(help_text="Price in Kenyan shillings")
    is_available = models.BooleanField(default=True)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, related_name="designs")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        DECLINED = "declined", "Declined"

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    placement = models.CharField(max_length=120)
    preferred_date = models.DateField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, related_name="appointments")
    design = models.ForeignKey(
        TattooDesign,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="appointments",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.preferred_date}"