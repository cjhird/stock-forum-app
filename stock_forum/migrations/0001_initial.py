# Generated by Django 4.0.5 on 2022-09-15 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('ticker', models.CharField(default=None, max_length=50)),
                ('stock_sector', models.CharField(choices=[('Technology', 'TECHNOLOGY'), ('Healthcare', 'HEALTHCARE'), ('Financial', 'FINANCIAL'), ('Communication', 'COMMUNICATION'), ('Energy', 'ENERGY'), ('Utilities', 'UTILITIES'), ('Propety', 'PROPERTY'), ('Materials', 'MATERIALS'), ('Consumer', 'CONSUMER')], default=None, max_length=30)),
                ('text', models.TextField(default=None, max_length=3000)),
                ('stock_rating', models.CharField(choices=[('Sell', 'SELL'), ('Underperform', 'UNDERPERFORM'), ('Hold', 'HOLD'), ('Outperform', 'OUTPERFORM'), ('Buy', 'BUY')], default=None, max_length=20)),
                ('image', models.CharField(default=None, max_length=300)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
