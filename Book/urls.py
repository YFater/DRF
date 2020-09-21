from django.conf.urls import url
from . import views

urlpatterns = [
    # # url(r'^books/$',views.BookAPIView.as_view()),
    # # url(r'^books/$',views.BookListAPIView.as_view()),
    # # url(r'^books/(?P<book_id>\d+)/$',views.BookDetailAPIView.as_view()),
    # # url(r'^generic_apiview_books/$', views.BookListGenericAPIView.as_view()),
    # # url(r'^generic_apiview_books/(?P<id>\d+)/$', views.BookDetailGenericAPIView.as_view()),
    # # url(r'^mixin_generic_apiview_books/$', views.BookListMixinGenericAPIView.as_view()),
    # # url(r'^mixin_generic_apiview_books/(?P<id>\d+)/$', views.BookDetailMixinGenericAPIView.as_view()),
    # url(r'^third_view_books/$', views.BookListThirdView.as_view()),
    # url(r'^third_view_books/(?P<id>\d+)/$', views.BookDetailThirdView.as_view()),
    # url(r'^viewset/$', views.BooksViewSet.as_view({'get': 'list'})),
    # url(r'^viewset/(?P<pk>\d+)/$', views.BooksViewSet.as_view({'get': 'retrieve'})),
    # url(r'^readonly_viewset/$', views.BooksReadOnlyModelViewSet.as_view({'get': 'list'})),
    # url(r'^readonly_viewset/(?P<pk>\d+)/$', views.BooksReadOnlyModelViewSet.as_view({'get': 'retrieve'})),
    # url(r'^model_viewset/$', views.BookModelViewSet.as_view({'get': 'list', "post": "create"})),
    # url(r'^model_viewset/(?P<pk>\d+)/$',
    #     views.BookModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # url(r'^books/bread/$', views.BookModelViewSet.as_view({'get': 'bread_book'})),
    # url(r'^books/bread/(?P<pk>\d+)/$', views.BookModelViewSet.as_view({'put': 'update_book_bread'})),
    url(r'^test/$', views.Testview.as_view())
]
from rest_framework.routers import SimpleRouter, DefaultRouter

# 创建路由对象
router = SimpleRouter()
# 注册视图表
router.register('books', views.BookModelViewSet, basename='test1')
urlpatterns += router.urls
# 输出结果：
print(urlpatterns)
