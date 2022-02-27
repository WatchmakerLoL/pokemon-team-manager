# Generated by Django 4.0.2 on 2022-02-26 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_alter_team_name'),
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='data',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='nickname',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='team',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='team.team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='national_number',
            field=models.IntegerField(null=True),
        ),
    ]
