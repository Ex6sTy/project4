from rest_framework import serializers

from vehicle.models import Car, Moto, Milage


class MilageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):

    last_milage = serializers.IntegerField(source='milage_set.all.first.milage')
    milage = MilageSerializer(many=True)

    class Meta:
        model = Car
        fields = '__all__'


class MotoSerializer(serializers.ModelSerializer):

    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    @staticmethod
    def get_last_milage(instance):
        if instance.milage.all.first():
            return instance.milage.all().first().milage
        return 0


class MotoMilageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = ('milage', 'year', 'moto')


class MotoCreateSerializer(serializers.ModelSerializer):
    milage = MilageSerializer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'

    def create(self, validated_data):
        milage = validated_data.pop('milage')

        moto_item = Moto.objects.create(**validated_data)

        for n in milage:
            Milage.objects.create(**n, moto=moto_item)
        return moto_item


