# Django - Registration and authentication endpoints with JSON Web token (JWT)
- Generate JWT tokens and make authenticated API calls using those JWT tokens 
- Generate access tokens using a refresh token
1. pip install djangorestframework-simplejwt
2. in installed apps
    `
        "rest_framework_simplejwt"
    `
3. ``` 
     REST_FRAMEWORK = {
       "DEFAULT_AUTHENTICATION_CLASSES" :[
         'rest_framework_simplejwt.authentication.JWTAuthentication',
        ]
    }


3. In project urls 
    `
    from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
   `
4. in project url patterns 
 ``` 
urlpatterns = [ 
    path('auth/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('auth/refresh/', TokenRefreshView.as_view(), name="token_refresh" )
]
```
5. To blacklist ...in installed apps ` 
    'rest_framework_simplejwt.token_blacklist'`
6. run migration 

7. In project urls `from rest_framework_simplejwt.views import TokenBlacklistView`

    ``` 
    urlpattern = [
        path('api/token/blacklist', TokenBlacklistView.as_view(), name="token_blacklist")
    ]


`

