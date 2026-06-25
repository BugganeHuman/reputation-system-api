from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'sender', 'receiver', 'amount', 'created_at']

    def validate(self, attrs):
        request = self.context.get('request')
        if not request or not hasattr(request.user, 'profile'):
            raise serializers.ValidationError("User does not have a profile ")

        sender_profile = request.user.profile
        receiver_profile = attrs['receiver']
        amount = attrs['amount']

        if sender_profile == receiver_profile:
            raise serializers.ValidationError({
                "You can't transfer your reputation to yourself"
            })

        if amount < 1:
            raise serializers.ValidationError({
                "The transfer amount must be a positive integer not less than 1"
            })

        if sender_profile.reputation < amount:
            raise serializers.ValidationError({
                "amount error"
            })

        return attrs