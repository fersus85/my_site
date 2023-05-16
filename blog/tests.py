from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from blog.models import Post


# Create your tests here.
class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@m.com',
            password='secret'
        )
        self.post = Post.objects.create(
            title='test_t',
            body='nice content',
            author=self.user
        )

    def test_string_representation(self):
        post = Post('A simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'test_t')
        self.assertEqual(f'{self.post.author}', 'test')
        self.assertEqual(f'{self.post.body}', 'nice content')

    def test_post_list_view(self):
        response = self.client.get(reverse('blog_home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'nice')
        self.assertTemplateUsed(response, 'blog/blog_home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        print(response)
        no_response = self.client.get('/post/19999/')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
