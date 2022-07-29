# Generated by Django 4.0.6 on 2022-07-29 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0006_remove_productvariation_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('quantity', models.PositiveIntegerField()),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='narxi', to='product.product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nomi', to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('region', models.CharField(choices=[('Toshkent shahri', 'Toshkent shahri'), ('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Surxondaryo viloyati', 'Surxondaryo viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati'), ('Farg`ona viloyati', 'Farg`ona viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Qoraqalpog`iston Respublikasi', 'Qoraqalpog`iston Respublikasi')], max_length=32)),
                ('job_location', models.TextField(max_length=256, null=True)),
                ('note', models.TextField(max_length=256, null=True)),
                ('billing_method', models.CharField(choices=[('Naqd', 'Naqd'), ('Karta', 'Orqali')], max_length=32)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.basket')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FISH', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefon_raqami', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]