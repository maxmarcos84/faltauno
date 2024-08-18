
from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView, RequestPasswordReset, ResetPassword, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserView.as_view(), name="register"),
    path('api/user/request_reset_password/', RequestPasswordReset.as_view(), name='request_reset_password'),
    path('api/user/reset_password/<str:token>', ResetPassword.as_view(), name='reset_password'),

    #path('api/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
]
