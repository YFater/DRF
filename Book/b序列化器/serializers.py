

from rest_framework import serializers


from Book.models import BookInfo
# 自定义校验方法
def check_bpub_date(value):
    if value.year < 2019:
        raise serializers.ValidationError('书籍的年份需要大于19年的')
    return value

# 1定义书籍序列化器
class BookInfoSerializer(serializers.Serializer):
    # read_only=True: 只读；  label:字段说明信息
    id = serializers.IntegerField(read_only=True,label='书籍编号')
    btitle = serializers.CharField(max_length=20,min_length=3,label='名称')
    bpub_date = serializers.DateField(label='发布日期',validators=[check_bpub_date])
    bread = serializers.IntegerField(default=0,min_value=0,label='阅读量')
    bcomment = serializers.IntegerField(default=0,max_value=50,label='评论量')
    is_delete = serializers.BooleanField(default=False,label='逻辑删除')

    # # 1.单字段校验
    # def validate_btitle(self, value):
    #     '''
    #     :param value: 就是传入的btitle
    #     :return:
    #     '''
    #     # 校验value中的内容
    #     if '金瓶' not in value:
    #         raise serializers.ValidationError('书籍名不包含金瓶')
    #     return value

    # 2.多字段校验
    def validate(self, attrs):
        '''
        :param attrs: 就是外界传进来的，book_dict
        :return:
        '''
        # 获取阅读量，评论量
        bread = attrs['bread']
        bcomment = attrs['bcomment']
        # 判断
        if bcomment > bread:
            raise serializers.ValidationError('评论量大于了阅读量')
        # 返回
        return attrs

    # 3.实现create方法
    def create(self, validated_data):
        '''
        :param validated_data: 校验成功之后的数据
        :return:
        '''
        # 创建book对象，设置属性，入库
        book = BookInfo.objects.create(**validated_data)
        # 返回
        return book

    # 实现update方法
    def update(self, instance, validated_data):
        '''
        :param instance: 外界传入的book对象
        :param validated_data: 校验成功之后的book_dict数据
        :return:
        '''
        # 更新数据
        instance.btitle = validated_data['btitle']
        instance.bpub_date = validated_data['bpub_date']
        instance.bread = validated_data['bread']
        instance.bcomment = validated_data['bcomment']
        # 入库
        instance.save()
        # 返回
        return instance
    # 1.关联英雄，主键，many=True：一方序列化多方需要加上
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    # 2.关联英雄，__str__返回值
    # heroinfo_set = serializers.StringRelatedField(read_only=True,many=True)

# 2定义英雄序列化器
class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)

    # 1.关联书籍，主键,read_only=True:表示只读，或者设置queryset
    # hbook = serializers.PrimaryKeyRelatedField(read_only=True)
    # hbook = serializers.PrimaryKeyRelatedField(queryset=BookInfo.objects.all())
    # 2.关联书籍，使用模型类，__str__方法返回值
    # hbook = serializers.StringRelatedField(read_only=True)
    # 3.关联，书籍序列化器
    hbook = BookInfoSerializer()
