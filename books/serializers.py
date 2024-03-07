from rest_framework.serializers import ModelSerializer
from .models import BookModel

class BooksModelSerializer(ModelSerializer):
    class Meta:
        model = BookModel
        # fields = ['author','genre','published_date']
        fields = '__all__'