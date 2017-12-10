from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.routers import SimpleRouter

from . import models, serializers


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


router = SimpleRouter()
router.register(r'book', BookViewSet, base_name='book')
router.register(r'tag', TagViewSet, base_name='tag')
router.register(r'user', UserViewSet, base_name='user')
urlpatterns = router.urls
