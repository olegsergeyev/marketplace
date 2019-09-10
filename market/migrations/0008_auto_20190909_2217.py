# Generated by Django 2.2.5 on 2019-09-09 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_auto_20190909_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_r',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=18, verbose_name='Логин')),
                ('name', models.CharField(max_length=15, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=64, verbose_name='Пароль')),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
    ]
