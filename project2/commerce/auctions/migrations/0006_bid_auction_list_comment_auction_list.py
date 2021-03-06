# Generated by Django 4.0.2 on 2022-03-17 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_watchlistitem_remove_user_watchlist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='auction_list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlist'),
        ),
        migrations.AddField(
            model_name='comment',
            name='auction_list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlist'),
        ),
    ]
