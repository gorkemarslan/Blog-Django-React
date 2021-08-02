from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Post, Tag


class TagModelTests(TestCase):
    def setUp(self) -> None:
        self.tag = Tag.objects.create(name='Python')

    def test_tag(self):
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.first().name, 'Python')
        self.assertEqual(str(Tag.objects.first()), 'Python')


class PostModelTests(TestCase):
    def setUp(self) -> None:
        self.tag = Tag.objects.create(name='Python')
        self.test_user = get_user_model().objects.create_user(email='testuser@email.com', password='testpassword',
                                                              first_name='first_name', last_name='last_name')
        self.test_post = Post.objects.create(title='Post Title', content='Test Post Content', slug='post-slug-field',
                                             author=self.test_user, status='published')

    def test_post(self):
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(self.test_post.author.email, 'testuser@email.com')
        self.assertEqual(self.test_post.title, 'Post Title')
        self.assertEqual(self.test_post.content, 'Test Post Content')
        self.assertEqual(self.test_post.status, 'published')
        self.assertEqual(str(self.test_post), 'Post Title')
