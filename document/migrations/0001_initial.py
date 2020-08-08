# Generated by Django 3.1 on 2020-08-08 20:35

from django.db import migrations, models
import django.db.models.deletion
import document.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('cabinet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='document_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='preparator_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('event_date', models.DateField()),
                ('published', models.DateField(auto_now_add=True)),
                ('boss_name', models.CharField(max_length=150)),
                ('meeting_type', models.CharField(max_length=150)),
                ('management_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabinet.cabinet')),
                ('tags', models.ManyToManyField(to='tags.Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file_uploded', models.FileField(upload_to=document.models.Management_path)),
                ('employee_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabinet.employee')),
                ('select_cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabinet.cabinet')),
            ],
        ),
    ]