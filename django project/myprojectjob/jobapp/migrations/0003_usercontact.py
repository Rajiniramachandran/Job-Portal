# Generated by Django 5.0.6 on 2024-07-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_userlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('useremail', models.EmailField(max_length=100)),
                ('Usermessages', models.CharField(max_length=5000)),
            ],
        ),
    ]