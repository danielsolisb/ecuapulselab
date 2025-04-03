from django.db import models
import uuid

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # WhatsApp Business via Twilio
    twilio_account_sid = models.CharField(max_length=255, blank=True, null=True)
    twilio_auth_token = models.CharField(max_length=255, blank=True, null=True)
    twilio_phone_number = models.CharField(max_length=20, blank=True, null=True)

    # Webhook token único por empresa
    webhook_token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    # JSON de flujo conversacional inicial
    flow_config = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name
