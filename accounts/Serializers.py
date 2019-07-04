from rest_framework import serializers

from accounts.models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    phone = serializers.SerializerMethodField()
    credit = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    black_list = serializers.SerializerMethodField()

    def get_name(self, profile):
        return self.name

    def get_credit(self, profile):
        return self.credit

    def get_black_list(self, profile):
        return self.black_list

    def get_phone(self, profile):
        self.credit = 8500
        self.name = "حسن فراهانی"
        self.black_list = True
        return profile.user.phone

    class Meta:
            model = Profile
            fields = ['phone', 'name', 'credit', 'black_list']
