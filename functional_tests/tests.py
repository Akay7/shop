from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from shop.models import Product


class BaseFunctionalTest(LiveServerTestCase):
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


class MainPageTest(BaseFunctionalTest):
    def test_can_going_to_look_details_about_product_from_main_page(self):
        # user come to main page and click on title for looking more detail about product
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_tag_name("a").click()

        # user redirected to page with information about product
        info_about_product = self.browser.find_element_by_class_name("Detail").text
        self.assertEqual(info_about_product, self.product.detail)


class CartTest(BaseFunctionalTest):
    def test_can_send_product_to_cart_from_main_page(self):
        # user can add product to card from main page
        self.browser.get(self.live_server_url)

        elem = self.browser.find_element_by_class_name("add_to_cart")
        elem.click()

        # after that user come to cart page and looking for added product
        self.browser.get(self.live_server_url + "/cart/")
        self.browser.find_element_by_id("product_short_info_")
        self.browser.implicitly_wait(40)




