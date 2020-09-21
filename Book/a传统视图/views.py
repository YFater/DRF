import json

from django.http import JsonResponse, HttpResponse

# Create your views here.
from django.views import View

from Book.models import BookInfo
from Book.b序列化器.serializers import BookInfoSerializer


class BookInfoView(View):
    def get(self,requset):
        # 查询所有的书籍
        books = BookInfo.objects.all()
        # 数据转换
        # book_list=[]
        # for book in books:
        #     book_dict = {
        #         'id': book.id,
        #         'btitle':book.btitle,
        #         'bpub_date':book.bpub_date,
        #         'bread':book.bread,
        #         'bcomment':book.bcomment,
        #     }
        #     book_list.append(book_dict)
        #返回响应
        serializer = BookInfoSerializer(instance=books,many=True)
        return JsonResponse(serializer.data,safe=False)

    def post(self,request):
        '''创建单本书籍'''
        #1 获取参数
        dict_data = json.loads(request.body.decode())
        btitle = dict_data.get("btitle")
        bpub_date = dict_data.get("bpub_date")
        bread = dict_data.get("bread")
        bcomment = dict_data.get("bcomment")
        #2 校验参数
        #3 数据入库
        book = BookInfo.objects.create(**dict_data)
        #4 返回响应
        book_dict = {
            'btitle':book.btitle,
            'bpub_date':book.bpub_date,
            'bread':book.bread,
            'bcomment':book.bcomment,
        }
        return JsonResponse(book_dict)


class BookInfoDetailView(View):
    def get(self,requset,pk):
        #1 通过pk获取对象
        book = BookInfo.objects.get(pk=pk)
        #2 转换数据
        book_dict = {
            'id': book.id,
            'btitle':book.btitle,
            'bpub_date':book.bpub_date,
            'bread':book.bread,
            'bcomment':book.bcomment,
        }
        #3 返回响应
        return JsonResponse(book_dict,json_dumps_params={'ensure_ascii':False})
    def put(self,request,pk):
        # 获取参数
        dict_data = json.loads(request.body.decode())
        book = BookInfo.objects.get(pk=pk)
        #校验参数
        #数据入库
        BookInfo.objects.filter(pk=pk).update(**dict_data)
        book = BookInfo.objects.get(pk=pk)
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
        }
        #返回响应
        return JsonResponse(book_dict)
    def delete(self,request,pk):
        book = BookInfo.objects.get(id=pk)
        book.delete()
        return HttpResponse(status=204)