# Generated by Django 3.2.9 on 2021-12-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='desktop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchase'), ('SOLD', 'Item sold'), ('RESTOcking', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchase'), ('SOLD', 'Item sold'), ('RESTOcking', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchase'), ('SOLD', 'Item sold'), ('RESTOcking', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
