"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

# # Swagger Imports
# from rest_framework import permissions
# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# # Define the JWT Bearer security scheme for Swagger
# security_definition = {
#     'BearerAuth': {
#         'type': 'http',
#         'scheme': 'bearer',
#         'bearerFormat': 'JWT',
#     }
# }

# # Define the schema view (Swagger) for the API
# schema_view = get_schema_view(
#     openapi.Info(
#         title="API Documentation",
#         default_version="v1",
#         description="API documentation for my Django project",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="your-email@example.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),  # Anyone can view the docs
# )

# # Add the security schemes to the schema (manual modification of the schema)
# schema_view.schema = {
#     'components': {
#         'securitySchemes': security_definition,
#     },
#     'security': [{'BearerAuth': []}],
# }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # User API Endpoints
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),    
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('home/', include('books.urls')), 

    # Swagger API Documentation
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)