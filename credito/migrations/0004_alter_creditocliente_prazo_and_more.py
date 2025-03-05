# Generated by Django 5.1.6 on 2025-03-05 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credito', '0003_alter_creditocliente_prazo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditocliente',
            name='prazo',
            field=models.CharField(choices=[('semanal', 'Semanal'), ('15dias', '15 dias'), ('45dias', '45 dias')], max_length=10),
        ),
        migrations.AlterField(
            model_name='creditocliente',
            name='status',
            field=models.CharField(default='por pagar', max_length=20),
        ),
    ]
