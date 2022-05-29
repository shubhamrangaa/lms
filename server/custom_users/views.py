from distutils.sysconfig import customize_compiler
import uuid
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from custom_users.models import UserProfile
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from custom_users.models import UserProfile
from custom_users.serializers import CustomUserSerializer
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your views here.
# @api_view(['GET'])
# def user_list(request,format=None):
#     users = UserProfile.objects.all()
#     serializers = CustomUserSerializer(data=users,many=True)
#     return Response(serializers.data)
# @api_view(['GET', 'PATCH', 'DELETE'])
# def new_snippet_list(request):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = UserProfile.objects.all()
#     except UserProfile.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         print("!!!!!get method!!!!!")
#         serializer = CustomUserSerializer(snippet,many=True)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CustomUserSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view
# def snippet_list(request,pk):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     try :
#         snippet = UserProfile.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         print("get method")
#         serializer = CustomUserSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         print("get method")
#         data = JSONParser().parse(request)
#         serializer = CustomUserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class UserProfileAPI(APIView):

    def get(self, request):
        user_objs = UserProfile.objects.all()
        serializer = CustomUserSerializer(user_objs , many=True)
        print(request.user)
        return Response({'Response' : serializer.data})
       
    def post(self, request):
        serializer = CustomUserSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status' : 403 ,'errors' : serializer.errors , 'messge' : 'Something went wrong'})
            
        serializer.save()   
        return Response({'status' : 200 , 'response' : serializer.data})

    
    def patch(self,request):
        try:
            user_obj = UserProfile.objects.get(id = request.data['id'])
            serializer = CustomUserSerializer(user_obj , data = request.data , partial =True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status' : 403 ,'errors' : serializer.errors , 'messge' : 'Something went wrong'})
                
            serializer.save()   
            return Response({'status' : 200 , 'payload' : serializer.data , 'messge' : 'your data is updated'})

        except Exception as e:
            print(e)
            return Response({'status' :403 , 'message' : 'invalid id'})
   
    def delete(self, request):
        try:
            id = request.GET.get('id')
            # user_obj = UserProfile.objects.get(id = request.data['id'])
            user_obj = UserProfile.objects.get(id = id)    
            user_obj.delete()
            return Response({'status' : 200, 'message' : 'deleted'})
    
        except Exception as e:
            print(e)
            return Response({'status' :403 , 'message' : 'invalid id'})
        
    
@api_view(['GET'])
def user_details(request,id):
    print("RTYU")
    user_objs = UserProfile.objects.get(id = id)
    serializer = CustomUserSerializer(user_objs)
    print(request.user)
    return Response({'Response' : serializer.data})
        




# @api_view(['POST'])
# def create_user(request,format=None):
#     return Response("Create new user")


# @api_view(['GET'])
# def user_detail(request,format=None):
#     return Response("Single User Detail")


# @api_view(['GET'])
# def user_list(request,format=None):
#     users = UserProfile.objects.all()
#     serializers = CustomUserSerializer(users,many=True)
#     return Response(serializers.data)


# @api_view(['PUT','PATCH'])
# def update_user(request,format=None):
#     return HttpResponse("update users")


# @api_view(['GET'])
# def delete_user(request,format=None):
#     return HttpResponse("delete user")