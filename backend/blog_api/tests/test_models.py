from django.test import TestCase
from django.contrib.auth.models import User
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
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.test_post = Post.objects.create(title='Post Title', content='Test Post Content', slug='post-slug-field',
                                             author=self.test_user, status='published')

    def test_post(self):
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(self.test_post.author.username, 'testuser')
        self.assertEqual(self.test_post.title, 'Post Title')
        self.assertEqual(self.test_post.content, 'Test Post Content')
        self.assertEqual(self.test_post.status, 'published')
        self.assertEqual(str(self.test_post), 'Post Title')
