# Generated by Django 4.2 on 2023-04-18 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0003_rename_carga_horario_evento_carga_horaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='criador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_termino',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='logo',
            field=models.FileField(upload_to='logos'),
        ),
    ]
