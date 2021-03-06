# Generated by Django 3.1.1 on 2020-10-18 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('subject', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='lecture',
            fields=[
                ('lecture_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('date', models.DateField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='assignment',
            fields=[
                ('assignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('due_date', models.DateField()),
                ('publish_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.lecture')),
            ],
        ),
    ]
