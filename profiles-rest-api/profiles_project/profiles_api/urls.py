from django.urls import path, include

from rest_framework.routers import DefaultRouter


from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewset, base_name = 'hello-views')


urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('', include(router.urls))
]