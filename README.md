# Django Tour & Travel Website - Production Ready

A complete, production-ready Django Tour & Travel company website with **multilingual support** (Uzbek, English, Russian) using django-modeltranslation.

## 🌟 Features

### Core Functionality
- ✅ **Multilingual Support**: Content in 3 languages (uz, en, ru)
- ✅ **Models**: Destination, Package, GalleryImage, Booking with translation support
- ✅ **Admin Panel**: Full-featured admin with inline editing and language tabs
- ✅ **Public Views**: List/detail views for destinations, packages, and gallery
- ✅ **Booking System**: Customer inquiry form with email notifications
- ✅ **CRUD Operations**: Authenticated users can create/edit/delete content
- ✅ **REST API**: JSON endpoints for destinations and packages
- ✅ **Responsive Design**: Bootstrap-compatible responsive templates
- ✅ **SEO Friendly**: Meta tags, slugs, and sitemap support
- ✅ **Language Switcher**: Dynamic UI language switching

### Technical Features
- Django 4.2+
- django-modeltranslation for database content translation
- django-crispy-forms with Bootstrap 5
- Pillow for image handling
- SQLite (development) / PostgreSQL-ready (production)
- Email backend (console for development)
- Pagination for all list views

---

## 🚀 Quick Start Guide

### 1. Installation Steps

```bash
# 1. Navigate to project directory
cd /home/user/travel-site

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create necessary directories
mkdir -p media/destinations media/packages media/gallery

# 6. Run migrations
python manage.py makemigrations
python manage.py migrate

# 7. Sync translation fields (CRITICAL!)
python manage.py sync_translation_fields --noinput

# 8. Create superuser
python manage.py createsuperuser

# 9. Load sample data (optional)
python manage.py load_sample_data

# 10. Run development server
python manage.py runserver
```

### 2. Access Points

- **Homepage**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/
- **Destinations**: http://localhost:8000/en/destinations/
- **Packages**: http://localhost:8000/en/packages/
- **Gallery**: http://localhost:8000/en/gallery/

---

## 🌐 Multilingual Configuration

### How Translation Works

**Database Content** (Models): Uses django-modeltranslation
- Fields become: `title_en`, `title_uz`, `title_ru`
- Admin shows language tabs for easy editing

**Static Strings** (UI Labels): Uses Django i18n
- Wrapped in `{% trans "Text" %}` in templates

### In Templates

```django
{% load i18n_tags %}
{{ destination|get_translated:'title' }}  {# Shows title in current language #}
```

### Language Switcher

Click UZ/EN/RU buttons in navbar to switch language. Updates both UI and content.

---

## 📝 Creating Content

### In Admin Panel

1. **Add Destination**:
   - Admin → Destinations → Add
   - Fill English tab, then Uzbek tab, then Russian tab
   - Upload image
   - Check "Published" and "Featured"
   - Save

2. **Add Package**:
   - Admin → Packages → Add
   - Select destination
   - Fill all 3 language tabs
   - Set price, duration
   - Save

3. **Add Gallery Images**:
   - Admin → Gallery Images → Add
   - Upload image
   - Add captions in 3 languages
   - Link to destination/package (optional)

---

## 🚀 Production Deployment

### Update Settings

```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

# Use PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'travel_db',
        ...
    }
}
```

### Collect Static Files

```bash
python manage.py collectstatic
```

### Run with Gunicorn

```bash
pip install gunicorn
gunicorn travel_site.wsgi:application --bind 0.0.0.0:8000
```

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location /static/ {
        alias /path/to/staticfiles/;
    }

    location /media/ {
        alias /path/to/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

---

## 🐛 Troubleshooting

### Translations Not Appearing
```bash
python manage.py sync_translation_fields --noinput
python manage.py migrate
```

### Media Files Not Showing

Check `travel_site/urls.py` includes:
```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Language Switcher Not Working

1. Ensure `LocaleMiddleware` in `MIDDLEWARE`
2. Check `/i18n/setlang/` URL exists
3. Clear browser cache

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `models.py` | Database schema |
| `translation.py` | Translation registration |
| `admin.py` | Admin configuration |
| `views.py` | Page logic |
| `urls.py` | URL routing |
| `forms.py` | Form definitions |
| `base.html` | Master template |
| `load_sample_data.py` | Sample data command |

---

## 📊 API Endpoints

```
GET /en/destinations/api/list/          # All destinations (JSON)
GET /en/destinations/api/{slug}/        # Single destination (JSON)
GET /en/packages/api/list/              # All packages (JSON)
GET /en/packages/api/{slug}/            # Single package (JSON)
```

---

## 💡 Best Practices

1. ✅ Fill all 3 languages for every content
2. ✅ Use `get_translated` filter in templates
3. ✅ Run `sync_translation_fields` after model changes
4. ✅ Test language switching on all pages
5. ✅ Backup database: `python manage.py dumpdata > backup.json`
6. ✅ Optimize images before upload (max 2MB)

---

## 🎯 Next Steps

1. Customize `templates/base.html` with your design
2. Add your logo and branding
3. Configure email settings for production
4. Add more destinations and packages
5. Set up SSL certificate for production
6. Configure backup strategy

---

**🎉 Your Django Tour & Travel website is ready!**

Homepage: http://localhost:8000/
Admin: http://localhost:8000/admin/
