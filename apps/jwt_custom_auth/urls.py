from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .views import TokenObtainExtraDetailsView, CustomTokenVerifyView

urlpatterns = [
    path('api/token/', TokenObtainExtraDetailsView.as_view(),
         name='token_obtain_pair-extra'),
    path('api/token-simple/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
#     path('api/token/verify/', TokenVerifyView.as_view(),
#          name='token_verify'),
    path('api/token/verify/', CustomTokenVerifyView.as_view(),
         name='token_verify'),

]
