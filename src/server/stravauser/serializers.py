from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Athlete, TokenData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class AthleteSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)  # Make it non-required for updates

    class Meta:
        model = Athlete
        fields = '__all__'
        extra_kwargs = {
            'id': {'validators': []},  # To allow updates without unique id clashes
        }

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user, _ = User.objects.get_or_create(**user_data)
            validated_data['user'] = user
        athlete = Athlete.objects.create(**validated_data)
        return athlete

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if user_data:
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()
        instance.save()
        return instance

class TokenDataSerializer(serializers.ModelSerializer):
    athlete = AthleteSerializer()

    class Meta:
        model = TokenData
        fields = '__all__'

    def create(self, validated_data):
        athlete_data = validated_data.pop('athlete')
        athlete_serializer = AthleteSerializer(data=athlete_data)
        if athlete_serializer.is_valid(raise_exception=True):
            athlete = athlete_serializer.save()
            token_data = TokenData.objects.create(athlete=athlete, **validated_data)
            return token_data
        return super().create(validated_data)

    # Add update method if necessary