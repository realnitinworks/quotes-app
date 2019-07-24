from django.test import TestCase
from django.urls import reverse

from quotes.models import Quote


class QuotesTestCases(TestCase):
    def setUp(self) -> None:
        self.quote = Quote.objects.create(
            text="Test Quote",
            author="Test Author",
            cover="http://www.cover-url.com",
            source="http://www.source-url.com",
        )

    def test_string_representation(self):
        expected = "Test Quote by Test Author"
        self.assertEqual(str(self.quote), expected)

    def test_get_absolute_url(self):
        expected = "/quote/1/"
        self.assertEqual(self.quote.get_absolute_url(), expected)

    def test_quote_content(self):
        self.assertEqual(self.quote.text, "Test Quote")
        self.assertEqual(self.quote.author, "Test Author")
        self.assertEqual(self.quote.cover, "http://www.cover-url.com")
        self.assertEqual(self.quote.source, "http://www.source-url.com")

    def test_quotes_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Quote")
        self.assertTemplateUsed(response, template_name='home.html')

    def test_quotes_detail_view(self):
        response = self.client.get(reverse('quote_detail', args="1"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Quote")
        self.assertTemplateUsed(response, template_name='quote_detail.html')

    def test_quotes_create_view(self):
        response = self.client.post(path=reverse('quote_new'), data={
            'text': "New Quote",
            'author': "New Author"
        })
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New Quote")
        self.assertContains(response, "New Author")
        self.assertTemplateUsed(response, template_name='home.html')

    def test_quotes_edit_view(self):
        response = self.client.post(path=reverse('quote_edit', args="1"), data={
            'text': "Update Quote",
            'author': "Update Author"
        })
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Update Quote")
        self.assertContains(response, "Update Author")
        self.assertTemplateUsed(response, template_name='home.html')

    def test_quotes_delete_view(self):
        response = self.client.post(path=reverse('quote_delete', args="1"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Test Quote")
        self.assertNotContains(response, "Test Author")
        self.assertTemplateUsed(response, template_name='home.html')





