from rest_framework import serializers

from SerialLearn.models import Book, Game


class BookSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    b_name = serializers.CharField(max_length=32)

    b_price = serializers.FloatField(default=1)

    def update(self, instance, validated_data):

        instance.b_name = validated_data.get("b_name", instance.b_name)
        instance.b_price = validated_data.get("b_price", instance.b_price)
        instance.save()

        return instance

    def create(self, validated_data):
        return Book.objects.create(**validated_data)


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ("id", "g_name", "g_price")