# Generated by Django 3.1.7 on 2021-04-17 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_delete_classification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentiment_analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_keys', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=200)),
                ('search_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]