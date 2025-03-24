from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Post, Comment


class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='password')
        self.client.login(username='tester', password='password')
        self.post = Post.objects.create(
            author=self.user,
            title='Test Post',
            content='Test Content'
        )

    def test_create_post(self):
        url = reverse('post-list')  # Имя маршрута, генерируется роутером
        data = {'title': 'New Post', 'content': 'New Content'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_post(self):
        url = reverse('post-detail', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        url = reverse('post-detail', args=[self.post.id])
        data = {'title': 'Updated Title', 'content': 'Updated Content'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        url = reverse('post-detail', args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CommentAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester2', password='password')
        self.client.login(username='tester2', password='password')
        self.post = Post.objects.create(
            author=self.user,
            title='Post for comment',
            content='Content'
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Test Comment'
        )

    def test_create_comment(self):
        url = reverse('comment-list')
        data = {'post': self.post.id, 'content': 'New Comment'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_comment(self):
        url = reverse('comment-detail', args=[self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_comment(self):
        url = reverse('comment-detail', args=[self.comment.id])
        data = {'post': self.post.id, 'content': 'Updated Comment'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment(self):
        url = reverse('comment-detail', args=[self.comment.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
