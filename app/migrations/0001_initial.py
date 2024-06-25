# Generated by Django 4.2.6 on 2024-05-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(blank=True, max_length=10, null=True)),
                ('intensity', models.IntegerField(blank=True, default='', null=True)),
                ('sector', models.CharField(blank=True, max_length=100, null=True)),
                ('topic', models.CharField(max_length=100)),
                ('insight', models.TextField()),
                ('url', models.URLField()),
                ('region', models.CharField(max_length=100)),
                ('start_year', models.CharField(blank=True, max_length=10, null=True)),
                ('impact', models.CharField(blank=True, max_length=10, null=True)),
                ('added', models.DateTimeField()),
                ('published', models.DateTimeField(blank=True, default='', null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('relevance', models.IntegerField(blank=True, null=True)),
                ('pestle', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('likelihood', models.IntegerField(blank=True, default='', null=True)),
            ],
        ),
    ]