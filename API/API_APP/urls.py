from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet

router = DefaultRouter()
router.register(r'std', StudentViewSet, basename='std')

#urlpatterns = [
#   path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

#]

urlpatterns = router.urls