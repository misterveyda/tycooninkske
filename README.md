# tycooninkske

Tycoon Inks Ke online tattoo shop, built with Django and PostgreSQL.

## Run locally

Requirements: Python 3.14 or compatible, Docker, and Docker Compose.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
docker compose up -d db
python manage.py migrate
python manage.py seed_demo
python manage.py test
python manage.py runserver
```

Open <http://127.0.0.1:8000/> for the catalogue and <http://127.0.0.1:8000/admin/> for studio administration. Create an admin login with `python manage.py createsuperuser`.

Stop PostgreSQL with `docker compose down`. The database volume is retained between starts.

The local database credentials in `docker-compose.yml` are for development only. Set the `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, and `POSTGRES_PORT` environment variables for other environments. Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, and `DJANGO_ALLOWED_HOSTS` appropriately before deployment.
