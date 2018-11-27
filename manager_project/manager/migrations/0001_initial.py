# Generated by Django 2.1.3 on 2018-11-27 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.IntegerField()),
                ('joined_at', models.DateTimeField()),
                ('quited_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('birthday', models.DateTimeField()),
                ('sex', models.IntegerField(editable=False)),
                ('address_from', models.IntegerField()),
                ('current_address', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateTimeField()),
                ('quited_at', models.DateTimeField(blank=True, null=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Manager')),
                ('persoon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Person')),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='persoon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Person'),
        ),
    ]
