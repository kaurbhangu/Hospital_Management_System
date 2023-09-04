from rest_framework import serializers
from .import models




class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =models.Student
        #fields(exclude=fileds that don want to show)
        #exclude=['id]
        # exclude=['id']
        fields = "__all__"