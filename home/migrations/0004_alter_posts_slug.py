# Generated by Django 4.2.3 on 2023-09-21 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_posts_author_posts_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(blank=True, default='', null=True),
        ),
    ]
