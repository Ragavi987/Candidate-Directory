from django.db.models import fields
from rest_framework import serializers
from .models import *
from rest_framework import status
import re
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class CandidatedirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatedirectory
        fields = '__all__'

    def validate(self, attrs):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if attrs.get('contact_no_primary') is not None:
            primary_no = attrs.get('contact_no_primary')

            qs = Candidatedirectory.objects.filter(Q(contact_no_primary__iexact=primary_no) | Q(contact_no_primary__icontains=primary_no))
            if len(str(primary_no)) > 10 or len(str(primary_no)) < 10 or str(primary_no).isdigit==False:
                raise serializers.ValidationError(_('Invalid primary contact number'))

            if qs.count() > 0:
                raise serializers.ValidationError(_('Primary contact number number already exist'))

        if attrs.get('contact_no_alternate') is not None:
            alternate_no = attrs.get('contact_no_alternate')

            if len(str(alternate_no)) > 10 or len(str(alternate_no)) < 10 or str(alternate_no).isdigit==False:
                raise serializers.ValidationError(_('Invalid alternate contact number'))

        if attrs.get('email') is not None:
            email = attrs.get('email')
            qs = Candidatedirectory.objects.filter(Q(email__iexact=email) | Q(email__icontains=email))
            if qs.count() > 0:
                raise serializers.ValidationError(_('Email already exist'))

            if not (re.fullmatch(regex, email)):
                raise serializers.ValidationError(_('Invalid Email'))

        return attrs


class CandidatedirectoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatedirectory
        fields = '__all__'

    def validate(self, attrs):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if attrs.get('contact_no_primary') is not None:
            primary_no = attrs.get('contact_no_primary')

            if len(str(primary_no)) > 10 or len(str(primary_no)) < 10 or str(primary_no).isdigit==False:
                raise serializers.ValidationError(_('Invalid primary contact number'))

        if attrs.get('contact_no_alternate') is not None:
            alternate_no = attrs.get('contact_no_alternate')

            if len(str(alternate_no)) > 10 or len(str(alternate_no)) < 10 or str(alternate_no).isdigit==False:
                raise serializers.ValidationError(_('Invalid alternate contact number'))

        if attrs.get('email') is not None:
            email = attrs.get('email')

            if not (re.fullmatch(regex, email)):
                raise serializers.ValidationError(_('Invalid Email'))

        return attrs