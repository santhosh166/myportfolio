# Generated by Django 4.0.1 on 2022-01-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_remove_certifications_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='skill',
            new_name='skill_title',
        ),
        migrations.AddField(
            model_name='certifications',
            name='logo',
            field=models.ImageField(default='san.jpg', upload_to='pics'),
        ),
    ]
