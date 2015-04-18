from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from shop.models import Product


class MainPageTest(LiveServerTestCase):
    def setUp(self):

        self.product = Product.objects.create(
            title="Product",
            detail="Very beautiful product. Buy it faster"
        )

        Product.objects.create(title="Product2")
        Product.objects.create(title="Product3")

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_going_to_look_details_about_product_from_main_page(self):
        # user come to main page and click on title for looking more detail about product
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id("product_short_info_1").find_element_by_tag_name("a").click()

        # user redirected to page with information about product
        info_about_product = self.browser.find_element_by_class_name("Detail").text
        self.assertEqual(info_about_product, self.product.detail)


class CartTest(LiveServerTestCase):
    def test_can_send_product_to_cart_from_main_page(self):
        self.product = Product.objects.create(
            title="Product",
            detail="Very beautiful product. Buy it faster"
        )

        # user can add product to card from main page
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

        #product = self.browser.find_element_by_id("product_short_info_1")
        #print(product.text)
        elem = self.browser.find_element_by_class_name("add_to_cart")
        #print(elem.text)
        elem.click()

        self.fail("Write test!!!")
