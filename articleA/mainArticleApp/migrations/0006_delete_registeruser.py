# Generated by Django 4.0.4 on 2022-04-21 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainArticleApp', '0005_remove_registeruser_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegisterUser',
        ),
    ]
