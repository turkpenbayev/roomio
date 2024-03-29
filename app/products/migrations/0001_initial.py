# Generated by Django 4.2.7 on 2024-03-18 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hrc_ip', models.CharField(max_length=100)),
                ('hrc_port', models.IntegerField()),
                ('unitId', models.IntegerField()),
                ('deviceName', models.CharField(max_length=100)),
                ('deviceTemplateID', models.IntegerField()),
                ('room', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DeviceScene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scenes', to='products.device')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modbusId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DeviceSceneTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('device_scene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags_and_values', to='products.devicescene')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_scenes', to='products.tag')),
            ],
        ),
        migrations.AddField(
            model_name='devicescene',
            name='scene',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='products.scene'),
        ),
        migrations.CreateModel(
            name='DeviceLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_locations', to='products.device')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_locations', to='products.location')),
                ('tags', models.ManyToManyField(to='products.tag')),
            ],
        ),
    ]
