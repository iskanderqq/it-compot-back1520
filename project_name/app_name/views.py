from django.shortcuts import render

# Create your views here.
def example(request):
    return render(request, 'app_name/some_template_name.html')