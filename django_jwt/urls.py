"""django_jwt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myAPI.urls')), 
    path('auth/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('auth/refresh/', TokenRefreshView.as_view(), name="token_refresh" )
]


# "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NzIxMjEyNCwianRpIjoiZDFjOTdmOTI2MzY0NDlkYzgzNDRlMjVjZmMwYmU5ZDUiLCJ1c2VyX2lkIjozfQ.FR-FZZ4WmhmgWDckcczzSkDa0Oj1SYc9OXMkyhX2lG4",

	# "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3MTI2MDI0LCJqdGkiOiI1ZTcxMDQzZjkwNmQ0ZTBiYWJjMDg0YTQ1Y2NlYTYyMiIsInVzZXJfaWQiOjN9.nS62sVf40nu1BI0-wy8NAqvfU_r04Dr_soEA6OEURbs"
