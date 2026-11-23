from django import forms

from .models import Appointment, Artist, TattooDesign


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = (
            "name",
            "email",
            "phone",
            "placement",
            "preferred_date",
            "artist",
            "design",
            "notes",
        )
        widgets = {"preferred_date": forms.DateInput(attrs={"type": "date"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["artist"].queryset = Artist.objects.filter(is_accepting_bookings=True)
        self.fields["design"].queryset = TattooDesign.objects.filter(is_available=True)
        self.fields["design"].required = False

    def clean(self):
        cleaned_data = super().clean()
        artist = cleaned_data.get("artist")
        design = cleaned_data.get("design")
        if artist and design and design.artist_id != artist.id:
            self.add_error("design", "Choose a design by the selected artist.")
        return cleaned_data