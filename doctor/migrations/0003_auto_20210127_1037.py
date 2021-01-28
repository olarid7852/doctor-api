# Generated by Django 3.1.5 on 2021-01-27 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20210127_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorblockedoffperiod',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='doctorblockedoffperiod',
            name='end',
        ),
        migrations.RemoveField(
            model_name='doctorblockedoffperiod',
            name='id',
        ),
        migrations.RemoveField(
            model_name='doctorblockedoffperiod',
            name='start',
        ),
        migrations.AddField(
            model_name='doctorblockedoffperiod',
            name='details',
            field=models.CharField(default='Desc', max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DoctorBusyPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(help_text='Blocked period start time', verbose_name='Start')),
                ('end', models.DateTimeField(help_text='Blocked period end time', verbose_name='End')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor', verbose_name='Doctor')),
            ],
        ),
        migrations.AddField(
            model_name='doctorblockedoffperiod',
            name='doctorbusyperiod_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='doctor.doctorbusyperiod'),
            preserve_default=False,
        ),
    ]