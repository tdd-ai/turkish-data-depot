# Generated by Django 3.1.7 on 2021-03-28 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create date')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='update date')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='dataset',
            name='format',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.format', verbose_name='format'),
        ),
    ]
