from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

def show_home(request):
    return render(request, "intro.html", {})
def about(request):
    return render(request,'about.html',{})

def view_contact(request):
    form = view_contact(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(instance)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(request.path)

    context = {
        'form': form,
    }
    return render(request, "contact.html", context)


