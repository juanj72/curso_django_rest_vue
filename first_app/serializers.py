from rest_framework import serializers

from .models import post


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model=post
        #fields=('id','title','thumnail','excerpt','content','slug','published','status','objects','postobjects')
        fields='__all__'



