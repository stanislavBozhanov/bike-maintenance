from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
      required=True,
      validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(write_only=True)
  password2 = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = ('password', 'password2', 'email', 'first_name', 'last_name')

  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
        raise serializers.ValidationError({"password": "Password fields didn't match."})
    return attrs

  def create(self, validated_data):
    print(validated_data)
    validated_data.pop('password2', None)
    try:
      user = User.objects.create_user(
        username=validated_data['email'],
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
      )
      user.set_password(validated_data['password'])
      user.save()
    except Exception as e:
      raise serializers.ValidationError({"error": "An error occurred while creating the user. " + str(e)})
    return user
