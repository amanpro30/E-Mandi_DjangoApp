# Generated by Django 2.2.6 on 2019-11-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_remove_marketorder_ordername'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='orderid',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='userid',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='marketorder',
            name='ClosingDate',
            field=models.DateField(),
        ),
    ]
