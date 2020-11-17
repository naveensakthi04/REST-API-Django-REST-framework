
from rest_framework import serializers

from account.models import Account

# Serializers are used to package and unpackage data


class RegistraionSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'},
                                      write_only=True)


    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def save(self):
        print("checking availability")
        account = Account(
                    email=self.validated_data['email'],
                    username=self.validated_data['username'],
                )
        print("username, email available!")
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        print(password, password2)
        if password != password2:
            raise serializers.ValidationError({'password':'Passwords do not match'})
        account.set_password(password)
        account.save()
        return account


class AccountPropertiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['pk', 'email', 'username']
