from django.test import TestCase
from .models import Product, Tag


# Create your tests here.
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

    def test_tag_show_its_product(self):
        prod1 = Product.objects.create(title="Product")
        tag1 = Tag.objects.create(name="green")
        prod1.tags.add(tag1)
        response = self.client.get('/%s/' % (tag1.slug,))
        self.assertContains(response, prod1)
