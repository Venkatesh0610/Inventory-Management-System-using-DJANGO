# Generated by Django 3.2.9 on 2021-12-31 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='issues',
            field=models.CharField(choices=[('NO ISSUES', 'no issues'), ('DISPLAY PROBLEM', 'Product display is not good'), ('HIGH PRICE', 'Price of the product is high'), ('BATTERY PROBLEM', 'Having problem with battery'), ('SLOW', 'Product is very slow and strucking')], default='any issues??', max_length=100),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='status',
            field=models.CharField(choices=[('RESTOCKING', 'Item restocking in few days'), ('SOLD', 'Item sold'), ('AVAILABLE', 'Item ready to be purchase')], default='SOLD', max_length=10),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='issues',
            field=models.CharField(choices=[('NO ISSUES', 'no issues'), ('DISPLAY PROBLEM', 'Product display is not good'), ('HIGH PRICE', 'Price of the product is high'), ('BATTERY PROBLEM', 'Having problem with battery'), ('SLOW', 'Product is very slow and strucking')], default='any issues??', max_length=100),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('RESTOCKING', 'Item restocking in few days'), ('SOLD', 'Item sold'), ('AVAILABLE', 'Item ready to be purchase')], default='SOLD', max_length=10),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='issues',
            field=models.CharField(choices=[('NO ISSUES', 'no issues'), ('DISPLAY PROBLEM', 'Product display is not good'), ('HIGH PRICE', 'Price of the product is high'), ('BATTERY PROBLEM', 'Having problem with battery'), ('SLOW', 'Product is very slow and strucking')], default='any issues??', max_length=100),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('RESTOCKING', 'Item restocking in few days'), ('SOLD', 'Item sold'), ('AVAILABLE', 'Item ready to be purchase')], default='SOLD', max_length=10),
        ),
    ]
