from django.shortcuts import render
from django import http
from django.contrib import messages

from .models import Feedback
from .forms import FeedbackForm

# Create your views here.
def home(request):
    # return render(request, "main/home.html")
    if request.method == "POST":
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            feedback_form.save()
            messages.success(request, "Відгук успішно збережено.")
            # return http.HttpResponseRedirect("")
        else:
            messages.error(request, "Помилка при заповненні форми.")
        return http.HttpResponseRedirect("")

    # if a GET (or any other method) we'll create a blank form
    else:
        feedback_form = FeedbackForm()

    return render(
        request,
        "index.html",
        context={
            "feedbacks": Feedback.objects.all()[:2],
            "feedback_form": feedback_form
        }
    )
