# Generated by Django 2.1.2 on 2018-10-25 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['pub_date', 'question_text']},
        ),
    ]