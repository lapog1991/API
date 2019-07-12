from rest_framework.viewsets import ModelViewSet


from .models import Student
from .Serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
