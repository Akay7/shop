from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(default='', max_length=200, unique=True)
    detail = models.TextField(default='')
    price = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    in_stock = models.BooleanField(default=False)
    show = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    detail = models.TextField(default='')

    def __str__(self):
        return self.name


class Order(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200)
    comment_from_client = models.TextField(default='')
    comment_from_admin = models.TextField(default='')

    def get_position(self, id_product):
        position, created = self.positioninorder_set.get_or_create(
            product=Product.objects.get(id=int(id_product)),
            defaults={
                "order": self,
            }
        )
        return position

    def add_one(self, id_product):
        position = self.get_position(id_product)
        position.qty += 1
        position.save()

    def del_one(self, id_product):
        position = self.get_position(id_product)
        position.qty -= 1
        position.save()

    def set_qty(self, id_product, qty):
        position = self.get_position(id_product)
        position.qty = qty
        position.save()

    def __str__(self):
        return "Order " + str(self.created_date)


class PositionInOrder(models.Model):
    order = models.ForeignKey(Order)
    product = models.OneToOneField(Product)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=15, decimal_places=2)

    def __str__(self):
        return "%s -- %d" % (self.product, self.qty)