# Generated by Django 3.2.3 on 2021-05-19 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_identification_situation_familiale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salarie',
            name='societe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subscriptions.societe'),
        ),
    ]
