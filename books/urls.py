from django.urls import path,include
from .views import home
from .views import (BooksModelViewSet, 
                    BooksListCreateAPIView, 
                    BooksRetrieveUpdateDestroyAPIView,
                    BooksAPIView,
                    BooksFBAPIView)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('api', BooksModelViewSet, basename='BooksAPI' )

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
    # ListCreateAPIView and RetrieveUpdateDestroyAPIView
    path('api/v1', BooksListCreateAPIView.as_view(), name='BooksListCreateAPIView'),
    path('api/v1/<int:pk>/', BooksRetrieveUpdateDestroyAPIView.as_view(), name='BooksRetrieveUpdateDestroyAPIView'),
    # Class Based APIView
    path('apivewcbv/v1/',BooksAPIView.as_view(), name='Class_basedAPIView'),
    path('apivewcbv/v1/<int:pk>/',BooksAPIView.as_view(), name='Class_basedAPIView_pk'),
    # Fucntion Based APIView
    path('apifb/v1/', BooksFBAPIView, name='BooksFBAPIView_FB'),
    path('apifb/v1/<int:pk>/', BooksFBAPIView, name='BooksFBAPIView_FB'),
    # For Jwt Authentication purpose, getting jwt token kind of thing
    path('get_token/', TokenObtainPairView.as_view(), name='get_token'),
    path('ref_token/',TokenRefreshView.as_view(), name='ref_token'),
    path('ver_token/',TokenVerifyView.as_view()),
]