
from apis.base_model import BaseModel
from tortoise import fields


class HealthCheck(BaseModel):
    status = fields.CharField(max_length=50, default="healthy")
    message = fields.CharField(
        max_length=50, default="Service is running smoothly.")

    class Meta:
        table = "health_check"
        table_description = "Health check status of the service"
