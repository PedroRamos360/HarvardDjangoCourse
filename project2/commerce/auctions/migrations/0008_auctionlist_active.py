# Generated by Django 4.0.2 on 2022-03-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_user_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlist',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
