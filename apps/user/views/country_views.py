# Django
# from django.shortcuts import get_object_or_404
from django.http import Http404

# Django Rest Framework
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

# apps
from apps.user.serializers import CountryMultilanguageSerializer
from apps.user.models import CountryMultilanguage


class ListCountryView(ListAPIView):
    """view for list all countries"""

    queryset = CountryMultilanguage.objects.all()
    serializer_class = CountryMultilanguageSerializer
