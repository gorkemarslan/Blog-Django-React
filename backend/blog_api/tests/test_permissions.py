from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from ..models import Post, Tag


class PermissionTests(APITestCase):

    def setUp(self) -> None:
        self.url_post_list = reverse('post_list')
        self.response = self.client.get(self.url_post_list, format='json')
        self.tag = Tag.objects.create(name='Python')
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.test_user2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.test_post = Post.objects.create(title='Post Title', content='Test Post Content', slug='post-slug-field',
                                             author=self.test_user, status='published')

    def test_only_author_of_a_post_can_write(self):
        data = {"title": "Post Title", "author": 1,
                "content": "Test Post Content", "status": 'published'}
        self.client.login(username=self.test_user2.username, password='testpassword')
        url = reverse('post_detail', kwargs={'pk': 1})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        url = reverse('post_detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
