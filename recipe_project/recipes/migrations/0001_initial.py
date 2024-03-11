# Generated by Django 5.0.3 on 2024-03-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('ingredients', models.TextField()),
                ('description', models.TextField()),
                ('rating', models.FloatField(default=0)),
                ('reviews', models.ManyToManyField(blank=True, related_name='recipe_reviews', to='recipes.review')),
            ],
        ),
    ]