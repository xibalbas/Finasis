# Generated by Django 4.1.2 on 2022-10-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signal_center', '0003_alter_newsignal_entry_point_alter_newsignal_tp1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsignal',
            name='position_status',
            field=models.CharField(choices=[('waiting', 'waiting'), ('open', 'open'), ('sl_triggered', 'sl_triggered'), ('tp1_triggered', 'tp1_triggered'), ('tp2_triggered', 'tp2_triggered'), ('tp3_triggered', 'tp3_triggered'), ('tp4_triggered', 'tp4_triggered'), ('tp5_triggered', 'tp5_triggered'), ('Done', 'Done')], default='waiting', max_length=50),
        ),
    ]