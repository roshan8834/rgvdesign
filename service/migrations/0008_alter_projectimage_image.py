# Generated by Django 4.2.4 on 2023-09-10 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_rename_contactus_enquirydata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(default=None, max_length=250, null=True, upload_to=None),
        ),
    ]
