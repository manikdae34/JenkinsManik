# Generated by Django 4.1.7 on 2023-03-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_visitor_alter_about_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=255)),
                ('start_Date', models.DateField()),
                ('end_Date', models.DateField(blank=True)),
                ('institution', models.CharField(max_length=255)),
            ],
        ),
    ]
