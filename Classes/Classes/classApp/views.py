from django.shortcuts import render
from .models import DjangoClasses

def home(request):
    class1 = DjangoClasses(title="Math", name="Math201", courseNumber=201, duration=2.5)
    class1.save()
    class2 = DjangoClasses(title="History", name="History101", courseNumber=101, duration=1.5)
    class2.save()
    class3 = DjangoClasses(title="Anatomy", name="Bio401", courseNumber=401, duration=3.5)
    class3.save()
    classes = [class1,class2,class3]
    context = {
        'Classes': classes
    }

    return render(request, "home.html", context)