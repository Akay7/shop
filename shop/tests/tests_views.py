import json
from django.test import TestCase
from shop.models import Product, Tag, Order, PositionInOrder


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


class OrderViewTest(TestCase):
    def setUp(self):
        self.prod = Product.objects.create(title="Product")
        self.order_operations_url = '/order_operation/'

    def test_save_to_session_add_to_cart(self):
        self.client.post(self.order_operations_url,
                         {'product_id': self.prod.id, "operation": "add"})

        order_id = self.client.session["order_id"]
        pos_in_session = Order.objects.get(id=order_id).get_position(self.prod.id)
        self.assertEqual(pos_in_session.qty, 1)

        self.client.post(self.order_operations_url,
                         {'product_id': self.prod.id, "operation": "add"})
        pos_in_session = Order.objects.get(id=order_id).get_position(self.prod.id)
        self.assertEqual(pos_in_session.qty, 2)

    def test_save_to_session_set_qty_for_position_in_cart(self):
        self.client.post(self.order_operations_url,
                         {'product_id': self.prod.id, "operation": "set", "qty": "20"})

        order_id = self.client.session["order_id"]
        pos_in_session = Order.objects.get(id=order_id).get_position(self.prod.id)
        self.assertEqual(pos_in_session.qty, 20)


class CartViewTest(TestCase):
    def setUp(self):
        self.prod1 = Product.objects.create(title="Product", price=40)
        self.prod2 = Product.objects.create(title="Goods2", price=11.2)
        self.order_operations_url = '/order_operation/'

    def add_product_to_db_and_to_cart(self):
        self.client.post(
            self.order_operations_url,
            {'product_id': self.prod1.id, "operation": "set", "qty": "20"}
        )

    def test_showing_details_about_products_in_cart(self):
        self.add_product_to_db_and_to_cart()

        response = self.client.get('/cart/')
        self.assertContains(response, "Product")

    def test_show_empty_cart_view(self):
        response = self.client.get('/cart/')
        self.assertContains(response, 'EMPTY')

    def test_showing_empty_on_every_page_with_middleware(self):
        response = self.client.get('/')
        self.assertContains(response, 'empty')

    def test_showing_full_cart_on_every_page_with_middleware(self):
        self.add_product_to_db_and_to_cart()

        response = self.client.get('/1/')
        self.assertContains(response, 'Product')

        response = self.client.get('/2/')
        self.assertContains(response, 'Product')

    def test_add_to_cart_return_json_obj_with_added_product(self):
        response = self.client.post(
            self.order_operations_url,
            {'product_id': self.prod1.id, "operation": "add"}
        )

        #print(type(response.content))
        #print(response.content.decode())


        data = json.loads(response.content.decode())
        print(data)
        self.assertEqual(response.status_code, 200)

        #self.assertEqual(data, {"correct": "true"})
        self.assertEqual(data, {"id": self.prod1.id,
                                "title": self.prod1.title,
                                "qty": 20
                                })

