# Generated by Django 4.2.3 on 2023-09-21 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_posts_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.author'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='tag',
            field=models.ManyToManyField(blank=True, to='home.tag'),
        ),
    ]
