# 定义类，集成APIView
from django.db import DatabaseError
from django.http import HttpResponse

from rest_framework import status, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action

from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from rest_framework.views import APIView

from Book.models import BookInfo
from Book.serializers import BookInfoModelSerializer


class BookAPIView(APIView):

    def get(self, request):
        # 获取APIView中的get请求参数
        # print(request.query_params)
        # return HttpResponse('get')
        return Response([{'name': 'YFater', 'age': 18}], status=status.HTTP_200_OK)

    def post(self, request):
        # 获取APIView中的post请求参数
        print(request.data)
        return HttpResponse('post')


# 序列化器和APIView实现列表视图
class BookListAPIView(APIView):
    def get(self, request):
        # 查询所有的书籍
        books = BookInfo.objects.all()
        # 将对象列表转换成字典列表
        serializer = BookInfoModelSerializer(instance=books, many=True)
        # 返回响应
        return Response(serializer.data)

    def post(self, request):
        # 获取参数
        data_dict = request.data
        # 创建序列化器
        serializer = BookInfoModelSerializer(data=data_dict)
        # 校验
        serializer.is_valid(raise_exception=True)
        # 入库
        serializer.save()
        # 返回响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 序列化器和APIView实现详情视图
class BookDetailAPIView(APIView):
    def get(self, request, book_id):
        # 1 获取书籍
        book = BookInfo.objects.get(pk=book_id)
        # 2 创建序列化对象
        serializer = BookInfoModelSerializer(instance=book)
        # 3 返回响应
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, book_id):
        # 获取数据，获取对象
        dict_data = request.data
        book = BookInfo.objects.get(pk=book_id)
        # 创建序列化对象
        serializer = BookInfoModelSerializer(instance=book, data=dict_data)
        # 校验，入库
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 返回响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, book_id):
        BookInfo.objects.get(pk=book_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 使用二级视图GenericAPIView实现列表视图
class BookListGenericAPIView(GenericAPIView):
    # 提供公共的属性
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    def get(self, request):
        # 查询所有的书籍
        # books = self.queryset
        books = self.get_queryset()
        # 将对象列表转换成字典列表(3种方法)
        # serializer = self.serializer_class(instance=books, many=True)
        # serializer = self.get_serializer_class()(instance=books, many=True)
        serializer = self.get_serializer(instance=books, many=True)
        # 返回响应
        return Response(serializer.data)

    def post(self, request):
        # 获取参数
        data_dict = request.data
        # 创建序列化器
        serializer = self.get_serializer(data=data_dict)
        # 校验
        serializer.is_valid(raise_exception=True)
        # 入库
        serializer.save()
        # 返回响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 使用二级视图GenericAPIView实现详情视图
class BookDetailGenericAPIView(GenericAPIView):
    # 提供通用的属性
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
    lookup_field = 'id'

    # lookup_url_kwarg = 'book_id'

    def get(self, request, id):
        # 1 获取书籍
        # get_object()根据pk到queryset中取出书籍对象
        book = self.get_object()
        # 2 创建序列化对象
        serializer = self.get_serializer(instance=book)
        # 3 返回响应
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        # 获取数据，获取对象
        dict_data = request.data
        book = self.get_object()
        # 创建序列化对象
        serializer = self.get_serializer(instance=book, data=dict_data)
        # 校验，入库
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 返回响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin


# mixin和二级视图GenericAPIView,实现列表视图
class BookListMixinGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    # 提供公共的属性
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# mixin和二级视图GenericAPIView,实现详情视图
class BookDetailMixinGenericAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    # 提供通用的属性
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
    lookup_field = 'id'

    # lookup_url_kwarg = 'book_id'

    def get(self, request, id):
        return self.retrieve(request)

    def put(self, request, id):
        return self.update(request)

    def delete(self, request, id):
        return self.destroy(request)


# 三级视图实现列表视图
class BookListThirdView(ListAPIView, CreateAPIView):
    # 提供公共的属性
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer


# 三级视图实现详情视图
class BookDetailThirdView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    # 提供通用的属性
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
    lookup_field = 'id'


from django.shortcuts import get_object_or_404
from rest_framework import viewsets


# 使用viewset实现获取所有和单个
class BooksViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving books.
    """

    def list(self, request):
        queryset = BookInfo.objects.all()
        serializer = BookInfoModelSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = BookInfo.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookInfoModelSerializer(instance=book)
        return Response(serializer.data)


# 使用ReadOnlyModelViewSet实现获取单个和所有
from rest_framework.viewsets import ReadOnlyModelViewSet


class BooksReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer


# ModelViewSet实现列表视图，详情视图功能
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend


# 自定义分页对象
class MyPageNumberPagination(PageNumberPagination):
    # 默认的大小
    page_size = 3
    # 前端可以指定页面大小
    page_size_query_param = 'page_size'
    # 页面的最大大小
    max_page_size = 5


class BookModelViewSet(ModelViewSet):
    '''
    list:获取所有数据
    create:创建单个对象
    '''
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    # 局部认证
    # authentication_classes = (SessionAuthentication, BasicAuthentication)

    # 局部权限
    # permission_classes = [AllowAny]

    # 局部限流
    # throttle_classes = [AnonRateThrottle]
    # 局部分页
    # pagination_class = LimitOffsetPagination  #

    # pagination_class = PageNumberPagination  # ?page=4
    # pagination_class = MyPageNumberPagination  # ?page=2&page_size=1
    # 局部过滤
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id', 'btitle', "is_delete"]

    # 8,局部排序
    filter_backends = [filters.OrderingFilter]  # 导包路径: from rest_framework import filters
    ordering_fields = ['id', 'btitle', 'bread']  # 查询格式: ?ordering=-bread,id

    @action(methods=['get'], detail=False)
    # 需求：获取阅读量大于111的书籍
    def bread_book(self, request):
        # 获取指定书籍
        books = BookInfo.objects.filter(bread__gt=111)
        # 创建序列化器对象
        serializer = self.get_serializer(instance=books, many=True)
        # 返回响应
        return Response(serializer.data)

    @action(methods=['put'], detail=True)
    # 需求：修改书籍编号为13的，阅读量为222
    def update_book_bread(self, request, pk):
        # 获取参数
        book = self.get_object()
        data = request.data
        # 创建序列化器对象
        serializer = self.get_serializer(instance=book, data=data, partial=True)
        # 校验，入库
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 返回响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)


from rest_framework.exceptions import APIException, ValidationError


# 可选限流
class Testview(APIView):
    # throttle_scope = 'uploads'

    def get(self, request):
        # raise DatabaseError("DatabaseError!!!")
        # raise Exception('报错了！！！！')
        raise APIException('APIException')
        # raise ValidationError("报错了!!!")
        # 测试pycharm连接git推送到远程仓库....

        return Response('testing...')
