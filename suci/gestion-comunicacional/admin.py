from django.contrib import admin
from .models import (
    SocialMediaAccount,
    SocialMediaPost,
    SocialActivity,
    Equipment,
    EquipmentLoan,
)

admin.site.register(SocialMediaAccount)
admin.site.register(SocialMediaPost)
admin.site.register(SocialActivity)
admin.site.register(Equipment)
admin.site.register(EquipmentLoan)
