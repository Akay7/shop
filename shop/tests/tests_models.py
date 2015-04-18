from django.test import TestCase
from shop.models import Product, Tag, Order, PositionInOrder


class ProductListModelTest(TestCase):
    def test_products_list_show_products_title(self):
        prod1 = Product.objects.create(title="first product")
        prod1.save()
        self.assertEquals(list(Product.objects.all()), [prod1])

    def test_product_have_correct_str(self):
        text = "First product"
        prod1 = Product.objects.create(title=text)
        prod1.save()
        self.assertEquals(text, prod1.title)

    def test_product_can_have_many_tags(self):
        tag1 = Tag.objects.create(name="green")
        tag2 = Tag.objects.create(name="big")
        product = Product.objects.create(title="bla")
        product.tags.add(tag1)
        product.tags.add(tag2)
        self.assertEqual([tag1, tag2], list(product.tags.all()))


class OrderModelTest(TestCase):
    def setUp(self):
        self.prod = Product.objects.create(title="Product1")
        self.order = Order.objects.create()
        PositionInOrder.objects.create(order=self.order, product=self.prod, qty=3)

    def test_position_in_order(self):
        self.assertEqual(self.prod, self.order.positioninorder_set.all()[0].product)

    def test_add_one_to_product(self):
        self.order.add_one(self.prod.id)
        self.assertEqual(self.order.positioninorder_set.all()[0].qty, 4)
        self.order.add_one(self.prod.id)
        self.assertEqual(self.order.positioninorder_set.all()[0].qty, 5)

    def test_del_one_from_product(self):
        self.order.del_one(self.prod.id)
        self.assertEqual(self.order.positioninorder_set.all()[0].qty, 2)

    def test_set_qty_to_product(self):
        self.order.set_qty(self.prod.id, 300)
        self.assertEqual(self.order.positioninorder_set.all()[0].qty, 300)

    def test_get_position(self):
        getted_product = self.order.get_position(self.prod.id).product
        self.assertEqual(getted_product, self.prod)
