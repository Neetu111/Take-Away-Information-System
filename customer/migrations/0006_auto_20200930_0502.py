# Generated by Django 2.1 on 2020-09-30 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20200930_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='business_owner',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, default='1', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business_owner',
            name='PID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Person'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='PID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Person'),
        ),
    ]
