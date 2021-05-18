# Generated by Django 3.1.4 on 2021-05-17 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordonnees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voie', models.TextField(max_length=50, null=True)),
                ('complement', models.TextField(max_length=50, null=True)),
                ('code_postale', models.TextField(max_length=50, null=True)),
                ('ville_salarie', models.TextField(max_length=50, null=True)),
                ('address_salarie', models.TextField(max_length=50, null=True)),
                ('hors_france_salarie', models.BooleanField(default=False)),
                ('pays_code_salarie', models.TextField(max_length=4, null=True)),
                ('pays_nom_salarie', models.TextField(max_length=50, null=True)),
                ('tel_bureau', models.TextField(max_length=20, null=True)),
                ('tel_portable', models.TextField(max_length=20, null=True)),
                ('tel_portable_pros', models.TextField(max_length=20, null=True)),
                ('tel_domicile', models.TextField(max_length=20, null=True)),
                ('email_salarie', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Emploi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature_emploi', models.CharField(max_length=50)),
                ('CDD', models.TextField(verbose_name='CDI')),
                ('duree_mois', models.SmallIntegerField(null=True)),
                ('duree_jours', models.SmallIntegerField(null=True)),
                ('date_debut_emploi', models.DateField()),
                ('motif_debut_emploi', models.TextField(max_length=250, null=True)),
                ('date_fin_emploi', models.DateField(null=True)),
                ('motif_fin_emploi', models.TextField(max_length=250, null=True)),
                ('code_metier', models.TextField(max_length=10, null=True)),
                ('salaire_brute', models.FloatField()),
                ('heure_normale', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='EtapeCreationSalarie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.BooleanField(default=False)),
                ('coordonnees', models.BooleanField(default=False)),
                ('bancaire', models.BooleanField(default=False)),
                ('emploi', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Identification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_salarie', models.CharField(max_length=50)),
                ('prenom_salarie', models.CharField(max_length=50)),
                ('nom_maritale', models.CharField(max_length=50, null=True)),
                ('matricule', models.CharField(max_length=50, null=True)),
                ('matricule_interne', models.CharField(max_length=50, null=True)),
                ('nir', models.CharField(max_length=15)),
                ('date_naissance', models.DateField()),
                ('pay_naissance', models.TextField(max_length=50, null=True)),
                ('commune_naissance', models.TextField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Societe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_societe', models.TextField(max_length=50)),
                ('locale', models.TextField(max_length=50)),
                ('siret', models.TextField(max_length=14)),
                ('activiter', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Salarie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('coordonnees', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='subscriptions.coordonnees')),
                ('empoi', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='subscriptions.emploi')),
                ('etape_creation', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='subscriptions.etapecreationsalarie')),
                ('identification', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='subscriptions.identification')),
                ('societe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.societe')),
            ],
        ),
        migrations.CreateModel(
            name='InformationBancaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rib', models.TextField(max_length=20)),
                ('iban', models.TextField(max_length=20)),
                ('bic', models.TextField(max_length=20)),
                ('virement', models.BooleanField(default=False)),
                ('plafond', models.FloatField(null=True)),
                ('salarie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.salarie')),
            ],
        ),
    ]