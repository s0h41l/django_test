# Generated by Django 2.1 on 2018-08-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventsBanners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=260, unique=True)),
                ('event_banner', models.ImageField(upload_to='banners')),
            ],
        ),
    ]