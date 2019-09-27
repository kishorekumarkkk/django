from rest_framework import viewsets
from sample.models import University, Student
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UniversitySerializer, StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        data = self.serializer_class(queryset, many=True).data
        return Response(data)

    def create(self, request, *args, **kwargs):
        data = request.data
        s = Student.objects.create(rno=data['rno'], first_name=data['first_name'], last_name=data['last_name'],
                                   age=data['age'], university=University.objects.get(id=data['university']))
        s.save()

        return Response(True)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Student.objects.get(pk=pk)
        serializer = StudentSerializer(queryset).data
        return Response(serializer)

    def destroy(self, request,pk=None, *args, **kwargs):
        query = Student.objects.filter(id=pk).delete()
        return Response(True)


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    def university(self):
        u_data = self.serializer_class(self.queryset, many=True).data
        return Response(u_data)

    @action(methods=['get'], detail=False, url_path='uni')
    def uni_set(self, pk):
        count = self.queryset.count()
        return Response(count)


