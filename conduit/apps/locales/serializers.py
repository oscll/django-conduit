from rest_framework import serializers
from .models import Local, Producto, Comment
from conduit.apps.profiles.serializers import ProfileSerializer

class LocalSerializer(serializers.ModelSerializer):
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')
    author = ProfileSerializer(read_only=True)

    class Meta:
        model = Local
        fields = (
            'id',
            'nombre',
            'telefono',
            'createdAt',
            'direccion',
            'poblacion',
            'provincia',
            'latitud',
            'longitud',
            'foto',
            'updatedAt',
            'categoria',
            'author',
        )

    def create(self, validated_data):
        author = self.context.get('author', None)
        local = Local.objects.create(author=author, **validated_data)
        return local

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()

class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(required=False)
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'body',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        local = self.context['local']
        author = self.context['author']

        return Comment.objects.create(
            author=author, local=local, **validated_data
        )

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class ProductoSerializer(serializers.ModelSerializer):
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Producto
        fields = (
            'id',
            'nombre',
            'foto',
            'descripcion',
            'price',
            'createdAt',
            'updatedAt',
            )
    
    def create(self, validated_data):
        local = self.context['local'] 
       
        return Producto.objects.create(
            local=local, **validated_data
        )

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()
