from rest_framework import serializers

from users.models import Payments


class PaymentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'

