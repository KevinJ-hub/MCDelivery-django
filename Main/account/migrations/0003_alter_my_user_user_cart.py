# Generated by Django 3.2 on 2021-04-14 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210414_0556'),
        ('account', '0002_alter_my_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_user',
            name='user_cart',
            field=models.ManyToManyField(to='products.Food'),
        ),
    ]