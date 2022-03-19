from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class Positiondata(models.Model):
    CRYNAME = (
        ('Cardano (ADA)','Cardano (ADA)'),
        ('Binance Coin (BNB)','Binance Coin (BNB)'),
        ('Bitcoin (BTC)','Bitcoin (BTC)'),
        ('Celsius (CEL)','Celsius (CEL)'),
        ('Dash (DASH)','Dash (DASH)'),
        ('Dogecoin (DOGE)','Dogecoin (DOGE)'),
        ('Polkadot (DOT)','Polkadot (DOT)'),
        ('EOS (EOS)','EOS (EOS)'),
        ('Ethereum (ETH)', 'Ethereum (ETH)'),
        ('Chainlink (LINK)','Chainlink (LINK)'),
        ('Litecoin (LTC)','Litecoin (LTC)'),
        ('Nano (NANO)','Nano (NANO)'),
        ('Neo (NEO)','Neo (NEO)'),
        ('Tether (USDT)','Tether (USDT)'),
        ('TRON (TRX)','TRON (TRX)'),
        ('NEM (XEM)','NEM (XEM)'),
        ('Stellar (XLM)','Stellar (XLM)'),
        ('Monero (XMR)','Monero (XMR)'),
        ('XRP (XRP)','XRP (XRP)'),
        ('Zcash (ZEC)','Zcash (ZEC)'),        
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    cryname = models.CharField(max_length=200, null=True, choices=CRYNAME)
    price = models.FloatField(null=True)
    amount = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.customer.name