# Generated by Django 4.1.7 on 2023-06-23 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0001_initial'),
        ('users', '0003_alter_user_address_alter_user_cellphone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='purchases',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='purchases.purchase'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
