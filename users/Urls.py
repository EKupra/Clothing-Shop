from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from .views import CodeGenerationView

urlpatterns += [
    path('generate-code/', CodeGenerationView.as_view(), name='generate_code'),
]
