from rest_framework import serializers
from quotedb.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Quote
        fields = ('body', 'owner', 'created')
