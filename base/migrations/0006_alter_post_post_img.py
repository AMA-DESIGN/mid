# Generated by Django 4.2.1 on 2023-06-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_cources_img1_alter_cources_img2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(upload_to='media'),
        ),
    ]
