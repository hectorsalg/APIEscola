# Generated by Django 3.1.3 on 2023-09-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_alter_aluno_cpf_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
