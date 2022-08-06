from django.db import models
from base.models import BaseModel

class Category(BaseModel):
    """
    Category
    """
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to='categories')
    # category_description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(BaseModel):
    """
    Product
    """
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class ProductImage(BaseModel):
    """
    ProductImage
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product_image')

    def __str__(self):
        return self.name