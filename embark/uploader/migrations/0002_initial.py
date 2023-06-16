# Generated by Django 4.1.5 on 2023-05-12 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('porter', '0002_initial'),
        ('uploader', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='firmwarefile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Fw_Upload_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='firmwareanalysis',
            name='device',
            field=models.ManyToManyField(blank=True, help_text='device/platform', max_length=127, related_query_name='device', to='uploader.device'),
        ),
        migrations.AddField(
            model_name='firmwareanalysis',
            name='firmware',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uploader.firmwarefile'),
        ),
        migrations.AddField(
            model_name='firmwareanalysis',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Fw_Analysis_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='firmwareanalysis',
            name='zip_file',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='porter.logzipfile'),
        ),
        migrations.AddField(
            model_name='device',
            name='device_label',
            field=models.ForeignKey(blank=True, help_text='label/tag', null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='label', to='uploader.label'),
        ),
        migrations.AddField(
            model_name='device',
            name='device_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Device_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='device',
            name='device_vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uploader.vendor'),
        ),
        migrations.AlterUniqueTogether(
            name='device',
            unique_together={('device_name', 'device_vendor')},
        ),
    ]
