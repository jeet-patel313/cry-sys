# Generated by Django 3.2.6 on 2021-09-19 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Positiondata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cryname', models.CharField(choices=[('Cardano (ADA)', 'Cardano (ADA)'), ('Binance Coin (BNB)', 'Binance Coin (BNB)'), ('Bitcoin (BTC)', 'Bitcoin (BTC)'), ('Celsius (CEL)', 'Celsius (CEL)'), ('Dash (DASH)', 'Dash (DASH)'), ('Dogecoin (DOGE)', 'Dogecoin (DOGE)'), ('Polkadot (DOT)', 'Polkadot (DOT)'), ('EOS (EOS)', 'EOS (EOS)'), ('Ethereum (ETH)', 'Ethereum (ETH)'), ('Chainlink (LINK)', 'Chainlink (LINK)'), ('Litecoin (LTC)', 'Litecoin (LTC)'), ('Nano (NANO)', 'Nano (NANO)'), ('Neo (NEO)', 'Neo (NEO)'), ('Tether (USDT)', 'Tether (USDT)'), ('TRON (TRX)', 'TRON (TRX)'), ('NEM (XEM)', 'NEM (XEM)'), ('Stellar (XLM)', 'Stellar (XLM)'), ('Monero (XMR)', 'Monero (XMR)'), ('XRP (XRP)', 'XRP (XRP)'), ('Zcash (ZEC)', 'Zcash (ZEC)')], max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('amount', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cryptosgp.customer')),
            ],
        ),
    ]
