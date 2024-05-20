from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserLoginView, PaymentsCreateAPIView, PaymentsListAPIView, PaymentsRetrieveAPIView, \
    PaymentsUpdateAPIView, PaymentsDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),

    path('payments/create/', PaymentsCreateAPIView.as_view(), name='payments_create'),
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
    path('payments/<int:pk>/', PaymentsRetrieveAPIView.as_view(), name='payments_get'),
    path('payments/update/<int:pk>/', PaymentsUpdateAPIView.as_view(), name='payments_update'),
    path('payments/delete/<int:pk>/', PaymentsDestroyAPIView.as_view(), name='payments_delete'),
]
