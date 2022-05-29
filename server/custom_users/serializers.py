from custom_users.models import UserProfile
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'

    # def validate(self,data):
    #         if not data['mobile'].isdigit():
    #             raise serializers.ValidationError({"Error":"Numbers should only be numeric."})
            












#                 from snippets.serializers import SnippetSerializer
# serializer = SnippetSerializer()
# print(repr(serializer)from 