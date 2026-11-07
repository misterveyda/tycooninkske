from django.core.management.base import BaseCommand

from studio.models import Artist, TattooDesign


class Command(BaseCommand):
    help = "Add starter artists and tattoo designs for local development."

    def handle(self, *args, **options):
        artists = [
            ("Wanjiku M.", "Fine line · botanical", "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=700&q=85"),
            ("Brian K.", "Blackwork · geometry", "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=700&q=85"),
            ("Amani N.", "Illustrative · colour", "https://images.unsplash.com/photo-1531123897727-8f129e1688ce?auto=format&fit=crop&w=700&q=85"),
        ]
        artist_records = {}
        for name, specialty, portrait_url in artists:
            artist_records[name], _ = Artist.objects.update_or_create(
                name=name,
                defaults={"specialty": specialty, "portrait_url": portrait_url, "is_accepting_bookings": True},
            )

        designs = [
            ("Wildflower study", "Wanjiku M.", "Fine line", "photo-1611501275019-9b5cda994e8d", 8500),
            ("The quiet eye", "Brian K.", "Blackwork", "photo-1565058379802-bbe93b2f703a", 12000),
            ("Sunbound", "Amani N.", "Illustrative", "photo-1598373182133-52452f7691ef", 15000),
            ("Little talisman", "Wanjiku M.", "Fine line", "photo-1590246814883-57c511e08bd5", 6500),
        ]
        for title, artist_name, style, image_id, price in designs:
            TattooDesign.objects.update_or_create(
                title=title,
                defaults={
                    "artist": artist_records[artist_name],
                    "style": style,
                    "image_url": f"https://images.unsplash.com/{image_id}?auto=format&fit=crop&w=900&q=85",
                    "starting_price": price,
                    "is_available": True,
                },
            )

        self.stdout.write(self.style.SUCCESS("Demo artists and designs are ready."))
