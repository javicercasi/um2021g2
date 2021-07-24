from .models import CompanyModel, FollowRelationship, UserModel
from django.contrib import admin

# Register your models here.
admin.site.register(UserModel)
admin.site.register(CompanyModel)
admin.site.register(FollowRelationship)
