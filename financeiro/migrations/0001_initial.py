# Generated by Django 5.1.6 on 2025-03-04 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateField()),
                ('categoria', models.CharField(choices=[('fixa', 'Fixa'), ('variavel', 'Variável')], default='variavel', max_length=10)),
            ],
        ),
    ]
