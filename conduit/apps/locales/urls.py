from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import (
    LocalViewSet, CommentsListCreateAPIView, 
    CommentsDestroyAPIView, ProductsListCreateAPIView, ProductsDestroyAPIView
)

router = DefaultRouter(trailing_slash=False)
router.register(r'locales', LocalViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

#    url(r'^locales/feed/?$', ArticlesFeedAPIView.as_view()),

    url(r'^locales/(?P<local_id>[-\w]+)/comments/?$', 
        CommentsListCreateAPIView.as_view()),

    url(r'^locales/(?P<local_id>[-\w]+)/comments/(?P<comment_pk>[\d]+)/?$',
        CommentsDestroyAPIView.as_view()),

    url(r'^locales/(?P<local_id>[-\w]+)/productos/?$', 
        ProductsListCreateAPIView.as_view()),

    url(r'^locales/(?P<local_id>[-\w]+)/productos/(?P<producto_pk>[\d]+)/?$',
        ProductsDestroyAPIView.as_view()),

]