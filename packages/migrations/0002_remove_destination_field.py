# Generated manually on 2025-12-07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='destination',
        ),
    ]
