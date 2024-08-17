from rest_framework import serializers
from .models import HomePage_logo

class Home_page_serializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage_logo
        fields = '__all__' # it for all feilds of models

        # def to_representation(self, instance):
        #     representation = super().to_representation(instance)
        #     request = self.context.get('request')
        #     if request is not None:
        #         representation['image'] = request.build_absolute_uri(instance.image.url)
        #     return representation