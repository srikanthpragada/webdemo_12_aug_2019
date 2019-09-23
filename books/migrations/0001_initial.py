# Generated by Django 2.2.2 on 2019-09-23 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=10)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
    ]
