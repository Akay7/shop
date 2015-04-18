from django.test import TestCase
from .models import Product, Tag, Order, PositionInOrder


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


class ProductListViewTest(TestCase):
    def test_products_view(self):
        prod1 = Product.objects.create(title="Product")
        response = self.client.get('/%d/' % (prod1.id,))
        self.assertContains(response, "Product")

    def test_teg_view_work(self):
        Tag.objects.create(name="green", slug='boom')
        response = self.client.get('/boom/')
        self.assertContains(response, "green")

    def test_tag_show_its_product(self):
        prod1 = Product.objects.create(title="Product")
        tag1 = Tag.objects.create(slug="green")
        prod1.tags.add(tag1)

        prod2 = Product.objects.create(title="Product2")
        tag2 = Tag.objects.create(slug="red")
        prod2.tags.add(tag2)

        response = self.client.get('/%s/' % (tag1.slug,))
        self.assertContains(response, prod1)
        self.assertNotContains(response, prod2)

    def test_tag_show_detail(self):
        tag1 = Tag.objects.create(slug="green", detail="Super-Duper")
        response = self.client.get('/%s/' % (tag1.slug,))
        self.assertContains(response, "Super-Duper")


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


class OrderViewTest(TestCase):
    def setUp(self):
        self.prod = Product.objects.create(title="Product")
        self.url = '/order_operation/'

    def test_save_to_session_add_to_cart(self):
        self.client.post(self.url,
                         {'product_id': self.prod.id, "operation": "add"})

        order_id = self.client.session["order_id"]
        pos_in_session = Order.objects.get(id=order_id).get_position(self.prod.id)
        self.assertEqual(pos_in_session.qty, 1)

        self.client.post(self.url,
                         {'product_id': self.prod.id, "operation": "add"})
        pos_in_session = Order.objects.get(id=order_id).get_position(self.prod.id)
        self.assertEqual(pos_in_session.qty, 2)

    def test_save_to_session_set_qty_for_position_in_cart(self):
        self.client.post(self.url,
                         {'product_id': self.prod.id, "operation": "set", "qty": "20"})

        order_id = self.client.session["order_id"]
        pos_in_session = Order.objects.get(id=order_id).get_position(self.prod.id)
        self.assertEqual(pos_in_session.qty, 20)
