# Generated by Django 3.0.5 on 2020-04-22 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasantias', '0003_auto_20200422_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
