# Generated by Django 4.2.2 on 2023-07-05 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libdeck', '0003_alter_book_libdeck_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_pub_date',
            field=models.DateField(verbose_name='Date published'),
        ),
    ]
