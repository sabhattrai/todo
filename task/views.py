from django.shortcuts import render, HttpResponseRedirect
from django import forms
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


# Create your views here.

tasks = ["foo", "bar", "baz"]


def index(request):
    return render(request, "task/index.html", {"tasks": tasks})


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "task/index.html", {"form": form})

    return render(request, "task/add.html", {"form": NewTaskForm()})
