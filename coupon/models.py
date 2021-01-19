from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    use_from = models.DateTimeField()
    use_to = models.DateTimeField()
    amount = models.IntegerField(validators=[MinLengthValidator(0), MaxLengthValidator(100000)])
    active = models.BooleanField()

    def __str__(self):
        return self.code