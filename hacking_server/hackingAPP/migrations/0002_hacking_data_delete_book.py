# Generated by Django 4.2.4 on 2023-08-21 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackingAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hacking_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
