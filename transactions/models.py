from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

class Transaction(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True,
                                related_name='sent_transaction')
    receiver = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True,
                                related_name='received_transaction')
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return (f"{self.sender.first_name} {self.sender.last_name} ->"
                f" {self.receiver.first_name} {self.receiver.last_name}: {self.amount}")