# Generated by Django 2.1 on 2020-09-30 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20200930_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_your_own_food',
            name='id',
            field=models.AutoField(auto_created=True, default='1', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drink',
            name='id',
            field=models.AutoField(auto_created=True, default='1', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='id',
            field=models.AutoField(auto_created=True, default='1', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='create_your_own_food',
            name='OID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Order'),
        ),
        migrations.AlterField(
            model_name='customize',
            name='MID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Menu'),
        ),
        migrations.AlterField(
            model_name='customize',
            name='OID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Order'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='MID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Menu'),
        ),
        migrations.AlterField(
            model_name='food',
            name='MID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Menu'),
        ),
        migrations.AlterField(
            model_name='menu_prepare',
            name='MID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Menu'),
        ),
        migrations.AlterField(
            model_name='menu_prepare',
            name='PID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Person'),
        ),
        migrations.AlterField(
            model_name='order_feedback',
            name='OID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Order'),
        ),
        migrations.AlterField(
            model_name='order_feedback',
            name='PID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Person'),
        ),
        migrations.AlterField(
            model_name='pick',
            name='MID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Menu'),
        ),
        migrations.AlterField(
            model_name='pick',
            name='OID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Order'),
        ),
    ]
