# Generated by Django 4.1.5 on 2023-01-26 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_scrap_city_scrap_pin_scrap_scrap_image_scrap_state_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrap',
            old_name='city',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='scrap',
            old_name='pin',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='scrap',
            old_name='state',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='scrap',
            old_name='user_address',
            new_name='Phone_number',
        ),
        migrations.RenameField(
            model_name='scrap',
            old_name='user_email',
            new_name='Pin_code',
        ),
        migrations.RenameField(
            model_name='scrap',
            old_name='scrap_image',
            new_name='Scrap_Image',
        ),
        migrations.RenameField(
            model_name='scrap',
            old_name='user_phone',
            new_name='State',
        ),
        migrations.RenameField(
            model_name='scrap',
            old_name='username',
            new_name='Username',
        ),
    ]
