from rest_framework import serializers
from .models import OneIDProfile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    reports_count = serializers.SerializerMethodField()
    class Meta:
        model = User 
        fields = (
            'id',
            'first_name',
            'last_name',
            'reports_count'
        )

    def get_reports_count(self, obj):
        #  done after meeting 
        # reports_count = User.objects.filter(reports=obj).count()
        return obj.reports.count()