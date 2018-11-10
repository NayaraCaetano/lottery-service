from rest_framework import serializers

from raffle.models import RaffleExecution


class RaffleSerializer(serializers.ModelSerializer):

    class Meta:
        model = RaffleExecution
        fields = '__all__'
        read_only_fields = ('id', 'executed_at', 'result')

    def create(self, validated_data):
        return RaffleExecution.objects.create_from_raffle(validated_data['items'])
