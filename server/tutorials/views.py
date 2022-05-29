from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from tutorials.models import ContentType, Tutorial
from tutorials.serializers import ContentTypeSerializer, TutorialSerializer

# Create your views here.

class TutorialProfileAPI(APIView):

    def get(self, request):
        tutorials_objs = Tutorial.objects.all()
        serializer = TutorialSerializer(tutorials_objs , many=True)
        print(request.user)
        return Response({'Response' : serializer.data})
       
    def post(self, request):
        serializer = TutorialSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status' : 403 ,'errors' : serializer.errors , 'messge' : 'Something went wrong'})
            
        serializer.save()   
        return Response({'status' : 200 , 'response' : serializer.data})

    
    def patch(self,request):
        try:
            user_obj = Tutorial.objects.get(uuid = request.data['uuid'])
            serializer = TutorialSerializer(user_obj , data = request.data , partial =True)
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
            uuid = request.GET.get('uuid')
            # user_obj = UserProfile.objects.get(id = request.data['id'])
            user_obj = Tutorial.objects.get(uuid = uuid)    
            user_obj.delete()
            return Response({'status' : 200, 'message' : 'deleted'})
    
        except Exception as e:
            print(e)
            return Response({'status' :403 , 'message' : 'invalid id'})
        

class ContentTypeAPI(APIView):

    def get(self, request):
        content_type_objs = ContentType.objects.all()
        serializer = ContentTypeSerializer(content_type_objs , many=True)
        print(request.user)
        return Response({'Response' : serializer.data})
       
    def post(self, request):
        serializer = ContentTypeSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status' : 403 ,'errors' : serializer.errors , 'messge' : 'Something went wrong'})
            
        serializer.save()   
        return Response({'status' : 200 , 'response' : serializer.data})

    
    def patch(self,request):
        try:
            user_obj = ContentType.objects.get(id = request.data['id'])
            serializer = ContentTypeSerializer(user_obj , data = request.data , partial =True)
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
            user_obj = Tutorial.objects.get(id = id)    
            user_obj.delete()
            return Response({'status' : 200, 'message' : 'deleted'})
    
        except Exception as e:
            print(e)
            return Response({'status' :403 , 'message' : 'invalid id'})
        

