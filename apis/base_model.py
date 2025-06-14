from tortoise.models import Model
from tortoise import fields


class BaseModel(Model):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        abstract = True
