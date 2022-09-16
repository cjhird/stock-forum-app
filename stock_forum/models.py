from django.db import models

# Create your models here.
class Thread(models.Model):

    STOCK_RATING_OPTIONS = [
      ('Sell', 'SELL'), 
      ('Underperform', 'UNDERPERFORM'),
      ('Hold', 'HOLD'),
      ('Outperform', 'OUTPERFORM'),
      ('Buy', 'BUY')
    ]

    STOCK_INDUSTRY_OPTIONS = [
      ('Technology', 'TECHNOLOGY'), 
      ('Healthcare', 'HEALTHCARE'),
      ('Financial', 'FINANCIAL'),
      ('Communication', 'COMMUNICATION'),
      ('Energy', 'ENERGY'),
      ('Utilities', 'UTILITIES'),
      ('Propety', 'PROPERTY'),
      ('Materials', 'MATERIALS'),
      ('Consumer', 'CONSUMER'),
    ]

    name = models.CharField(max_length=100, default=None)
    ticker = models.CharField(max_length=50, default=None)
    stock_sector = models.CharField(max_length=30, choices=STOCK_INDUSTRY_OPTIONS, default=None)
    text = models.TextField(max_length=3000, default=None)
    stock_rating = models.CharField(max_length=20, choices=STOCK_RATING_OPTIONS, default=None)
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='threads',
        on_delete=models.CASCADE
    )

    def __str__(self):
      return f"{self.title}"