from rest_framework import serializers
from .models import University, Student


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = ('id', 'univ_name')


class StudentSerializer(serializers.ModelSerializer):
    univ_name = serializers.CharField(source='University.univ_name', read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'rno', 'first_name', 'last_name', 'age', 'university', 'univ_name')


