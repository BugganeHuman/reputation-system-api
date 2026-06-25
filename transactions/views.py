from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser, IsAuthenticated
from .models import Transaction
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .serializers import TransactionSerializer
from django.db import transaction


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Transaction.objects.all()

        sender_profile = user.profile
        return Transaction.objects.filter(sender=sender_profile) | Transaction.objects.filter(receiver=sender_profile)

    def perform_create(self, serializer):
        sender_profile = self.request.user.profile
        receiver_profile = serializer.validated_data['receiver']
        amount = serializer.validated_data['amount']

        with transaction.atomic():
            sender_profile.reputation -= amount
            receiver_profile.reputation += amount

            sender_profile.save()
            receiver_profile.save()

            serializer.save(sender=sender_profile)