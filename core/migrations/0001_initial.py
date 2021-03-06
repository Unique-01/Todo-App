# Generated by Django 3.2.12 on 2022-02-21 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateField(default='2022-02-21')),
                ('due_date', models.DateField(default='2022-02-21')),
                ('category', models.ForeignKey(default='General', on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
