# Generated by Django 4.2.7 on 2023-11-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogWebsiteDRF', '0002_remove_blog_id_alter_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='about',
            field=models.TextField(default='', max_length=500),
        ),
    ]
