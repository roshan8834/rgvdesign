# Generated by Django 4.2.4 on 2023-08-30 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_interiorprojects_cover_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcategory',
            name='filter_name',
            field=models.CharField(default='filter-res', max_length=50),
        ),
    ]
