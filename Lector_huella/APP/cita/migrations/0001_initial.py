# Generated by Django 4.1.1 on 2022-10-07 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Medico', '0001_initial'),
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time', models.DateTimeField()),
                ('eps', models.CharField(max_length=50)),
                ('specialty', models.CharField(max_length=50)),
                ('doctors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medico.medico')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.paciente')),
            ],
        ),
    ]