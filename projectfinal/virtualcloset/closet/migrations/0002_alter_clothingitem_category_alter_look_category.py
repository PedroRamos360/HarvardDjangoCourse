# Generated by Django 4.0.3 on 2022-04-08 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('closet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothingitem',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='closet.clothingcategory'),
        ),
        migrations.AlterField(
            model_name='look',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='closet.lookcategory'),
        ),
    ]
