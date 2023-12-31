# Generated by Django 4.2.2 on 2023-07-03 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libdeck', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.CharField(max_length=200, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_pages',
            field=models.IntegerField(default=0, verbose_name='Pages'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_pub_date',
            field=models.DateTimeField(verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='libraryspace',
            name='lib_address',
            field=models.CharField(max_length=400, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='libraryspace',
            name='lib_book_count',
            field=models.IntegerField(default=0, verbose_name='Book count'),
        ),
        migrations.AlterField(
            model_name='libraryspace',
            name='lib_date_opened',
            field=models.DateTimeField(verbose_name='Date opened'),
        ),
        migrations.AlterField(
            model_name='libraryspace',
            name='lib_name',
            field=models.CharField(max_length=300, verbose_name='Library name'),
        ),
    ]
