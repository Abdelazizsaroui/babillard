# Generated by Django 3.0.8 on 2020-07-18 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='abonn',
            field=models.ManyToManyField(related_name='abonn', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='page',
            name='code',
            field=models.CharField(default='0000000000', max_length=10),
        ),
        migrations.AddField(
            model_name='page',
            name='login_req',
            field=models.BooleanField(default=False, help_text='Cochez cette case si les utilisateurs annonymes ne sont pas autorisés à visiter la page et voir ses annonces', verbose_name='Authentification requise'),
        ),
        migrations.AddField(
            model_name='page',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='page',
            name='organisme',
            field=models.CharField(blank=True, max_length=150, verbose_name="Nom de l'organisme"),
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nom de la page'),
        ),
        migrations.AlterField(
            model_name='page',
            name='private',
            field=models.BooleanField(default=False, help_text='Seuls les utilisateurs autorisés peuvent visiter la page et voir ses annonces', verbose_name='Page privé'),
        ),
        migrations.DeleteModel(
            name='Paper',
        ),
        migrations.AddField(
            model_name='annonce',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Page'),
        ),
    ]
