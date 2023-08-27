from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from apps.accounts import models as m_accounts


class UserSimplesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_accounts.User
        fields = [
            'name',
            'email',
            'is_active',
        ]
        read_only_fields = [
            'name',
            'email',
            'is_active',
        ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = m_accounts.User
        fields = [
            'name', 'email', 'password',
            'is_active', 'is_staff', 'last_login'
        ]
        read_only_fields = ['is_active', 'is_staff', 'last_login']

    def validate_password(self, value):
        password = value
        if password != self.instance.password:
            self.instance.set_password(password)
            password = self.instance.password

        if not password:
            raise serializers.ValidationError('Password is required')

        return password

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)

        return instance


class TokenSerializer(serializers.ModelSerializer):

    user = UserSimplesDetailSerializer()

    class Meta:
        model = Token
        fields = ['user', 'key']
        read_only_fields = ['user', 'key']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        return token
