# Generated by Django 2.0.1 on 2018-02-05 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0002_inscricao_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscricao',
            old_name='owner',
            new_name='cadastrador',
        ),
    ]
