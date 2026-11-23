from django.contrib import admin

from .models import Appointment, Artist, TattooDesign


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty", "is_accepting_bookings")
    list_filter = ("is_accepting_bookings",)
    search_fields = ("name", "specialty")


@admin.register(TattooDesign)
class TattooDesignAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "style", "starting_price", "is_available")
    list_filter = ("style", "is_available")
    search_fields = ("title", "artist__name")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name", "artist", "preferred_date", "status", "created_at")
    list_filter = ("status", "preferred_date", "artist")
    search_fields = ("name", "email", "phone")