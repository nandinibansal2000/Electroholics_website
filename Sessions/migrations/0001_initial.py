# Generated by Django 2.2.2 on 2019-06-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PRP', 'PROPOSED'), ('CMP', 'COMPLETED'), ('CNC', 'CANCELLED'), ('CNF', 'CONFIRMED')], default='PRP', max_length=3)),
                ('link', models.TextField(blank=True)),
            ],
        ),
    ]
