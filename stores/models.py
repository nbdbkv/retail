from django.db import models


class CommonInfo(models.Model):
    count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    class Meta:
        abstract = True


class Store(models.Model):
    """Model for creating a Store object."""
    name = models.CharField(max_length=120, unique=True,)

    def __str__(self):
        return self.name


class Product(CommonInfo):
    """Model for creating a Product object."""
    name = models.CharField(max_length=120, null=True, blank=True,)
    in_stock = models.BooleanField(default=True,)
    store = models.ForeignKey(
        to='Store', on_delete=models.CASCADE, related_name='products',
    )

    def __str__(self):
        return self.name


class ProductBuy(CommonInfo):
    """Model for creating a ProductBuy object."""
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE,  related_name='product_buy',
    )

    def __str__(self):
        return self.product.name


class ProductAdd(CommonInfo):
    """Model for creating a ProductAdd object."""
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE,  related_name='product_add',
    )

    def __str__(self):
        return self.product.name
