# Generated by Django 4.2.7 on 2024-01-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=100)),
                ('Sprincipal', models.CharField(max_length=100)),
                ('Slocation', models.CharField(max_length=100)),
                ('email', models.EmailField(default='hai@gmail.com', max_length=254)),
                ('renteremail', models.EmailField(default='hai@gmail.com', max_length=254)),
            ],
        ),
    ]
