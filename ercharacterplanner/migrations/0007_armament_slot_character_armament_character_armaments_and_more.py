# Generated by Django 4.2 on 2023-04-28 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ercharacterplanner', '0006_character_attribute_character_leveled_attributes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Armament_Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Character_Armament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ercharacterplanner.armament')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ercharacterplanner.character')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ercharacterplanner.armament_slot')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='armaments',
            field=models.ManyToManyField(through='ercharacterplanner.Character_Armament', to='ercharacterplanner.armament'),
        ),
        migrations.AddConstraint(
            model_name='character_armament',
            constraint=models.UniqueConstraint(fields=('character', 'slot'), name='character_armament_slot_unique'),
        ),
    ]
