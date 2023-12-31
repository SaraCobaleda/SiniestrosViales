# Generated by Django 4.1 on 2023-08-24 03:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analiticaSiniestros", "0004_alter_choque_descchoque_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="choque",
            name="idChoque",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="clasesiniestro",
            name="idClaseSiniestro",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="clasevehiculo",
            name="idClaseVehiculo",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="codigocausa",
            name="idCodigoCausa",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="codigolocalidad",
            name="idCodigoLocalidad",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="condicion",
            name="idCondicion",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="disenolugar",
            name="idDisenoLugar",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="enfuga",
            name="idEnfuga",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="estado",
            name="idEstado",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="gravedad",
            name="idGravedad",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="servicio",
            name="idServicio",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="sexo",
            name="idSexo",
            field=models.IntegerField(),
        ),
    ]
