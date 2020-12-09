# Generated by Django 3.1.4 on 2020-12-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, default='', max_length=80, null=True)),
                ('product_id', models.IntegerField()),
                ('owner_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('owner_id', models.IntegerField()),
            ],
        ),
    ]