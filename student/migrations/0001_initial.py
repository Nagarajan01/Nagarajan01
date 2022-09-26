# Generated by Django 4.1.1 on 2022-09-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('roll_no', models.TextField()),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]