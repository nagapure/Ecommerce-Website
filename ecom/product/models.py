from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

class Category(BaseModel):
    """
    Category
    """
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to='categories')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class ColorVariant(BaseModel):
    """
    Color Variant
    """
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.color_name


class SizeVariant(BaseModel):
    """
    Size Variant
    """
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.size_name


class Product(BaseModel):
    """
    Product
    """
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField(blank=True)
    color_variant = models.ManyToManyField(ColorVariant, blank=True)
    size_variant = models.ManyToManyField(SizeVariant, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name
    
    def get_product_price_by_size(self, size):
        return self.price + SizeVariant.objects.get(size_name=size).price

class ProductImage(BaseModel):
    """
    ProductImage
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product_image')

    def __str__(self):
        return self.product.product_name