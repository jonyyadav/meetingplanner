from django.shortcuts import render, get_object_or_404, redirect
# from django.forms import modelform_factory
# Create your views here.
from .forms import MeetingForm
from meeting.models import Meeting, Room
from django.contrib import messages


def detail(request, id):
    # meeting = Meeting.objects.get(pk=id),
    return render(request, "meetings/detail.html",
                  {"meeting": get_object_or_404(Meeting, pk=id), "room": Room.objects.get(pk=id)})


def room(request):
    return render(request, "meetings/room.html", {"rooms": Room.objects.all()})


# MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
