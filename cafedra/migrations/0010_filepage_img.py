# Generated by Django 4.2.5 on 2024-02-24 11:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafedra', '0009_infopage_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='filepage',
            name='img',
            field=models.FileField(default='static/cafedra/header_img/bg.jpg', upload_to='static/cafedra/header_img/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]