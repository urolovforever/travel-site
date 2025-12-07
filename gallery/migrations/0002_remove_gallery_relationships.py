# Generated manually on 2025-12-07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        # Remove indexes first
        migrations.RemoveIndex(
            model_name='galleryimage',
            name='gallery_gal_destina_e4eeed_idx',
        ),
        migrations.RemoveIndex(
            model_name='galleryimage',
            name='gallery_gal_package_766d0a_idx',
        ),
        # Remove fields
        migrations.RemoveField(
            model_name='galleryimage',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='package',
        ),
    ]
