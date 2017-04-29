from rest_framework.serializers import (
    ModelSerializer,
)
from .models import Foco


class FocoSerializer(ModelSerializer):

    class Meta:
        model = Foco
        fields = ('id', 'latitude', 'longitude', 'category', 'city')