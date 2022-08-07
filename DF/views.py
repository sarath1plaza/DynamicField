from django.shortcuts import render
from django.views.generic.edit import CreateView

from DF.models import Student

class StudentCreation(CreateView):
    model = Student
    fields = ['name','subject']
    template_name = 'Index.html'

    def post(self, request, *args):
        data = request.POST
        Student.objects.create(name=data['name'],subject=data['subject'])
        return render(request, 'Index.html')
