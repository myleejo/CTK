# Generated by Django 4.2.4 on 2023-08-28 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscore',
            name='crypto_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userscore',
            name='linux_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userscore',
            name='system_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userscore',
            name='web_score',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='TotalScore',
        ),
    ]
