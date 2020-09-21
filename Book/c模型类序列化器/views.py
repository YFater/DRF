
from Book.models import BookInfo
from Book.c模型类序列化器.serializers import BookModelSerializer
# 1.获取模型类对象
book = BookInfo.objects.get(pk=10)
# 2.创建序列化对象
serializer = BookModelSerializer(instance=book)
# 3.输出结果
print(serializer.data)

from Book.models import BookInfo
from Book.c模型类序列化器.serializers import BookModelSerializer
# 准备字典数据,书籍对象
book = BookInfo.objects.get(pk=11)
book_dict = {
    'btitle':'鹿鼎记2',
    'bpub_date':'2020-10-22',
    'bread':199,
    'bcomment':50
}
# 序列化器对象创建
serializer = BookModelSerializer(instance=book,data=book_dict)
# 校验，入库
serializer.is_valid(raise_exception=True)
serializer.save()