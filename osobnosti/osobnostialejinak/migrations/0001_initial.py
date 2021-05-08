# Generated by Django 3.2.1 on 2021-05-08 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Druh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oznaceni_druhu', models.CharField(help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný', max_length=50, unique=True, verbose_name='Označení druhu zboží')),
                ('oblast', models.CharField(blank=True, choices=[('herec', 'Herec'), ('politik', 'Politik'), ('sportovec', 'Sportovec'), ('zpěvák', 'Zpěvák'), ('celebrita', 'Celebrita')], default='celebrita', help_text='Vyberte označení oblasti', max_length=20, verbose_name='Oblast')),
            ],
            options={
                'verbose_name': 'Druh zaměření',
                'verbose_name_plural': 'Druh zaměření',
                'ordering': ['oznaceni_druhu'],
            },
        ),
        migrations.CreateModel(
            name='Osobnosti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(help_text='Zadejte jméno o maximální délce 50 znaků', max_length=50, verbose_name='Jméno osobnosti')),
                ('prijmeni', models.CharField(help_text='Zadejte přijmení o maximální délce 50 znaků', max_length=50, verbose_name='Přijmení osobnosti')),
                ('popis', models.TextField(blank=True, null=True, verbose_name='Popis osobnosti')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='osobnosti/%Y/%m/%d/', verbose_name='Fotka osobnosti')),
                ('druh', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='osobnostialejinak.druh')),
            ],
            options={
                'verbose_name': 'Osobnost',
                'verbose_name_plural': 'Osobnosti',
                'ordering': ['prijmeni'],
            },
        ),
    ]