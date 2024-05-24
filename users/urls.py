from django.urls import path

from users.apps import UsersConfig
from users.views import (UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView,
                         PaymentsCreateAPIView, PaymentsListAPIView, PaymentsRetrieveAPIView, PaymentsUpdateAPIView,
                         PaymentsDestroyAPIView)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

urlpatterns = [
    path('user/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('user/', UserListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_get'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('payments/create/', PaymentsCreateAPIView.as_view(), name='payments_create'),
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
    path('payments/<int:pk>/', PaymentsRetrieveAPIView.as_view(), name='payments_get'),
    path('payments/update/<int:pk>/', PaymentsUpdateAPIView.as_view(), name='payments_update'),
    path('payments/delete/<int:pk>/', PaymentsDestroyAPIView.as_view(), name='payments_delete'),
]
