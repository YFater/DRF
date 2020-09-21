from Book.models import BookInfo
from Book.b序列化器.serializers import BookInfoSerializer

# 1.先获取书籍对象
book = BookInfo.objects.get(id=3)
# 2.创建序列化器，instance:表示要序列化的对象
serializer = BookInfoSerializer(instance=book)
# 3.转换数据
print(serializer.data)

# # 1.先获取书籍对象
# book = BookInfo.objects.all()
# # 2.创建序列化器，instance:表示要序列化的对象,many=True:表示序列化多个对象
# serializer = BookInfoSerializer(instance=book,many=True)
# # 3.转换数据
# print(serializer.data)


from Book.models import HeroInfo
from Book.b序列化器.serializers import HeroInfoSerializer

# 1.先获取英雄对象
hero = HeroInfo.objects.get(id=6)
# 2.创建序列化器，instance:表示要序列化的对象
serializer = HeroInfoSerializer(instance=hero)
# 3.转换数据
print(serializer.data)

from Book.models import BookInfo
from Book.b序列化器.serializers import BookInfoSerializer
# 1.准备数据
book_dict = {
    "btitle":"源自传2",
    "bpub_date":"2020-03-22",
    "bread":100,
    "bcomment":50
}
book = BookInfo.objects.get(pk=10)
# 2.创建序列化器，校验
serializer = BookInfoSerializer(instance=book,data=book_dict)
# raise_exception=True:校验不通过时，会报错
serializer.is_valid(raise_exception=True)
# 3.入库(保存数据)
serializer.save()










