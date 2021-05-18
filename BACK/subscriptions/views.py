from rest_framework.response import Response
from rest_framework import generics
from . models import Posts
from . serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated


class PostView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Posts.objects.all()

    def get(self, request, *args, **kwargs):
        querySet = self.get_queryset()
        serializer = PostSerializer(querySet, many=True)
        return Response(serializer.data)

class SalarieView():
    permission_classes = (IsAuthenticated,)
    def ajoutIdentification(request):
        print(request)
        