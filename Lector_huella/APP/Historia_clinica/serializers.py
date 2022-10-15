from rest_framework.serializers import ModelSerializer

from .models import historia


class HistoriaSerializer(ModelSerializer):
    class Meta:
        model = historia
        fields = (
            'id', 'Name', 'Surname','Cc','Phone','Direction',  'gender','Eps', 'email', 'Occupation', 'hour_entry_finish','Doctor_concept')




