from django.shortcuts import render

# Create your views here.
def contacts(request):
    context = {'phone': '+375 (29) 123-45-67'}
    return render(request, 'contacts.html', context)
