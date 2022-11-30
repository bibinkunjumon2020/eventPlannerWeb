# Generated by Django 4.1.3 on 2022-11-25 11:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=120)),
                ('event_date', models.DateField()),
                ('content', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('pic', models.ImageField(upload_to='events', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])])),
                ('download_file', models.FileField(blank=True, null=True, upload_to='event_pdf')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
