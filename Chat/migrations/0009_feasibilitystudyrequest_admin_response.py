# Generated by Django 5.0.1 on 2024-06-02 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0008_feasibilitystudyrequest_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feasibilitystudyrequest',
            name='admin_response',
            field=models.TextField(blank=True, null=True),
        ),
    ]
