# Generated by Django 3.2.4 on 2021-07-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro', '0002_auto_20210723_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followrelationship',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='privatemessagemodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='publicmessagemodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tagmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
