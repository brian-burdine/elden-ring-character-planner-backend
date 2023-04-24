from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import (
    CustomUser,
    Character
)
from .serializers import (
    CustomUserSerializer,
    CharacterSerializer
)

# Create your views here.

# USERS
class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

#CHARACTERS
#TO-DO: Figure out if I need to filter queryset based on user/owner
class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    # Overwrites the default queryset by using the user attached to a request to filter the set on the user field in Character model
    def get_queryset(self):
        user = self.request.user
        return Character.objects.filter(owner=user)

    # Attaches the user to the character when the request comes through with the user that made the request
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)