# Generated by Django 4.0.2 on 2022-02-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
