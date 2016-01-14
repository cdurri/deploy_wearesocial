from django.test import TestCase
from accounts.views import register
from core.views import get_index
from django.core.urlresolvers import resolve
from django.shortcuts import  render_to_response

# Create your tests here.

class RegisterPageTest(TestCase):

    def test_register_page_resolves(self):

        register_page = resolve('/register/')

        self.assertEqual(register_page.func, register)



    def test_home_page_resolves(self):

        home_page = resolve('/')

        self.assertEqual(home_page.func, get_index)


    def test_home_page_status_code_is_ok(self):

        home_page = self.client.get('/')

        self.assertEquals(home_page.status_code, 200)


    def test_check_check_content_is_correct(self):

        home_page = self.client.get('/')

        self.assertTemplateUsed(home_page, "index.html")

        home_page_template_output = render_to_response("index.html").content

        self.assertEquals(home_page.content, home_page_template_output)




