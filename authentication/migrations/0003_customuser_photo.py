# Generated by Django 4.2.2 on 2023-06-25 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_customuser_first_name_customuser_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(null=True, upload_to='customer_photo'),
        ),
    ]
