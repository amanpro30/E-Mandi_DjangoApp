from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cropName', models.CharField(max_length=50)),
                ('varietyName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PriceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('low', models.FloatField(default=None)),
                ('high', models.FloatField(default=None)),
                ('volume', models.IntegerField(default=0)),
                ('closing', models.FloatField(default=None)),
                ('opening', models.FloatField(default=None)),
                ('crop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crop.Crop')),
            ],
        ),
    ]
