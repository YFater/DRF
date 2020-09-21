from rest_framework import serializers
from Book.models import BookInfo


# 定义书籍模型序列化器
class BookInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'
        extra_kwargs = {
            'bread': {
                'required': True,
                'help_text': '阅读量'
            }
        }
