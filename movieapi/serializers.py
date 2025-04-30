
from rest_framework import serializers
from rec_organ.models import user_Details, student,Admin_details,requests_made,organ


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ('name','branch','year','sem','internship','project')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_Details
        fields = ('Username','Password')


class Admin_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_details
        fields = ('Username','Password')




class organSerializer(serializers.ModelSerializer):
    class Meta:
        model = organ
        fields = ('name','location','availa','price')



class requests_madeSerializer(serializers.ModelSerializer):
    class Meta:
        model = requests_made
        fields = ('name','thing','status')

        