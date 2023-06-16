# Generated by Django 4.1.5 on 2023-05-12 08:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cve', models.CharField(help_text='CVE-XXXX-XXXXXXX', max_length=13, validators=[django.core.validators.MinLengthValidator(17)])),
                ('info', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('firmware_analysis', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='uploader.firmwareanalysis')),
                ('emba_command', models.CharField(blank=True, max_length=762, null=True)),
                ('restricted', models.BooleanField(default=False)),
                ('os_verified', models.CharField(blank=True, max_length=256, null=True)),
                ('architecture_verified', models.CharField(blank=True, max_length=100, null=True)),
                ('architecture_unverified', models.CharField(blank=True, max_length=100, null=True)),
                ('files', models.IntegerField(default=0)),
                ('directories', models.IntegerField(default=0)),
                ('entropy_value', models.FloatField(default=0.0)),
                ('cve_high', models.IntegerField(default=0)),
                ('cve_medium', models.IntegerField(default=0)),
                ('cve_low', models.IntegerField(default=0)),
                ('exploits', models.IntegerField(default=0)),
                ('metasploit_modules', models.IntegerField(default=0)),
                ('canary', models.IntegerField(default=0)),
                ('canary_per', models.IntegerField(default=0)),
                ('relro', models.IntegerField(default=0)),
                ('relro_per', models.IntegerField(default=0)),
                ('no_exec', models.IntegerField(default=0)),
                ('no_exec_per', models.IntegerField(default=0)),
                ('pie', models.IntegerField(default=0)),
                ('pie_per', models.IntegerField(default=0)),
                ('stripped', models.IntegerField(default=0)),
                ('stripped_per', models.IntegerField(default=0)),
                ('certificates', models.IntegerField(default=0)),
                ('certificates_outdated', models.IntegerField(default=0)),
                ('shell_scripts', models.IntegerField(default=0)),
                ('shell_script_vulns', models.IntegerField(default=0)),
                ('yara_rules_match', models.IntegerField(default=0)),
                ('kernel_modules', models.IntegerField(default=0)),
                ('kernel_modules_lic', models.IntegerField(default=0)),
                ('interesting_files', models.IntegerField(default=0)),
                ('post_files', models.IntegerField(default=0)),
                ('strcpy', models.IntegerField(default=0)),
                ('versions_identified', models.IntegerField(default=0)),
                ('bins_checked', models.IntegerField(default=0)),
                ('strcpy_bin', models.TextField(default='{}')),
                ('vulnerability', models.ManyToManyField(blank=True, help_text='CVE/Vulnerability', related_query_name='CVE', to='dashboard.vulnerability')),
            ],
        ),
    ]
