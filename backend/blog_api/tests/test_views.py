from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from ..models import Post, Tag


class BlogAPIViewTests(APITestCase):

    def setUp(self) -> None:
        self.url_post_list = reverse('post_list')
        self.response = self.client.get(self.url_post_list, format='json')
        self.tag = Tag.objects.create(name='Python')
        self.test_user = get_user_model().objects.create_user(email='email@email.com', first_name='first_name',
                                                              last_name='last_name', password='testpassword')
        self.test_post = Post.objects.create(title='Post Title', content='Test Post Content', slug='post-slug-field',
                                             author=self.test_user, status='published')

    def test_view_posts(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        data = {"title": "Post Title", "author": 1,
                "content": "Test Post Content", "status": 'published'}
        self.client.login(email=self.test_user.email, password='testpassword')
        response = self.client.post(self.url_post_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        url = reverse('post_detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
