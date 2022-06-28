from django.contrib.auth import get_user_model
from rest_framework import serializers
from server.auth_app.models import Profile


UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email', 'avatar', 'image')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = UserModel
        fields = ('username', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel.objects.create(
            username=validated_data['username'],
            password=password,
        )

        user.set_password(password)
        user.save()

        profile_data = validated_data.pop('profile')

        profile = Profile.objects.create(
            user=user,
            email=profile_data['email'],
            avatar=profile_data['avatar'],
        )

        profile.save()

        return user
