# Generated by Django 5.1.3 on 2024-12-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/')),
            ],
        ),
    ]
