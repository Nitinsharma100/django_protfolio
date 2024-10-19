from django.shortcuts import render

# Create your views here.
def edu(request):
    context={'skill':'active'}
    return render(request,'edu/edu.html',context)