# Generated by Django 3.0.2 on 2020-01-18 20:03

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200115_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contents',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
