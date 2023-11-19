from django.urls import path
from rest_framework import routers

from apps.user.views import (
    CreateUser, ListUserViewSet, UserViewSet,
    ChangePasswordView, DeleteUserAcount,
    VerityAccountView
)

router = routers.SimpleRouter()
router.register(r'users', ListUserViewSet)

urlpatterns = [
    path('signup/', CreateUser.as_view(), name='signup'),
    path('verify_email/', VerityAccountView.as_view(),
         name='verity_account'),
    path('change_password/<str:username>/',
         ChangePasswordView.as_view(),
         name='auth_change_password'),
    path('change_password/<str:username>/delete/',
         DeleteUserAcount.as_view(),
         name='delete_account'),
    path('user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve'}))
]

urlpatterns += router.urls
