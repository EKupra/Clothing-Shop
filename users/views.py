
import random
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CodeGenerationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        code = random.randint(1000, 9999)
        cache.set(f"code_{request.user.id}", code, timeout=3600)

        return Response({"code": code})
