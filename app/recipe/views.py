from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag

from recipe import serializers

import recipe

def attrs_and_types(mod_name):

    print('Attributes and their types for module {}:'.format(mod_name))
    print()
    for num, attr in enumerate(dir(eval(mod_name))):
        print("{idx}: {nam:30}  {typ}".format(
            idx=str(num + 1).rjust(4),
            nam=(mod_name + '.' + attr).ljust(30), 
            typ=type(eval(mod_name + '.' + attr))))

attrs_and_types(recipe.__name__)

class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
