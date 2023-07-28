from .models import Pet

class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name', 'breed', 'sex', 'age', 'image')