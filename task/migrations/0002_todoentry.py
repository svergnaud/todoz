# Generated by Django 2.0.6 on 2018-06-06 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('done', models.BooleanField(default=False)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Category')),
            ],
            options={
                'ordering': ['creation_date'],
                'verbose_name': 'Elément de la todo',
                'verbose_name_plural': 'Eléments de la todo',
            },
        ),
    ]
