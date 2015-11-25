from aasemble.django.apps.api.v2 import serializers as v2_serializers


class aaSembleAPIv3Serializers(v2_serializers.aaSembleAPIv2Serializers):
    view_prefix = 'v3'
    builds_nest_source = True