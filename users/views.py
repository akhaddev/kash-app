from .models import User
from rest_framework import generics
from .serializers import UserSerializer
from datetime import datetime



class UserPetrolSpyAPIView(generics.ListAPIView):
    today = datetime.now()
    last_month = today.month - 1 if today.month > 1 else 12
    queryset = User.objects.filter(reports__created_at__month=last_month)
    serializer_class = UserSerializer


user_pertol_spy_api_view = UserPetrolSpyAPIView.as_view()