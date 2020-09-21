# 定义书籍模型类序列化器
from rest_framework import serializers
from Book.models import BookInfo

class BookModelSerializer(serializers.ModelSerializer):
    # mobile = serializers.CharField(max_length=11,min_length=11,label='手机号',write_only=True)
    class Meta:
        model = BookInfo  # 参考模型类生成字段
        fields = '__all__'  # 生成所有字段
        # 生成指定的字段
        # fields = ['id','btitle','bpub_date']
        # 排除指定的字段
        # exclude = ['btitle']
        # # 设置只读字段
        # read_only_fields = ['btitle']
        # 添加额外参数
        extra_kwargs = {
            'bread':{
                'max_value':999999,
                'min_value':0
            },
            'bcomment':{
                'max_value':999999,
                'min_value':0
            }
        }