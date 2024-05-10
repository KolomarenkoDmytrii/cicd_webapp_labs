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
            feedback_form.save()
            messages.success(request, "Відгук успішно збережено.")
            # return http.HttpResponseRedirect("")
        else:
            error_message = ""
            messages.error(request, "Помилка при заповненні форми.")

            if not "rating" in feedback_form.cleaned_data.keys():
                messages.error(request, "Оцінка не вказана або вона не в межах між 1 і 5.")
            if not "text" in feedback_form.cleaned_data.keys():
                messages.error(request, "Текст не вказаний або він задовгий.")
            if not "user_name" in feedback_form.cleaned_data.keys():
                messages.error(request, "Ім'я не вказане або воно задовге.")

        return http.HttpResponseRedirect("")

    # if a GET (or any other method) we'll create a blank form
    else:
        feedback_form = FeedbackForm()

    return render(
        request,
        "index.html",
        context={
            "feedbacks": Feedback.objects.all()[:4],
            "feedback_form": feedback_form
        }
    )

def feedbacks(request):
    return render(
        request,
        "feedbacks.html",
        context={
            "feedbacks": Feedback.objects.all()
        }
    )

def about_page(request):
    return render(
        request,
        "about.html"
    )

def lawyer_info(request):
    return render(
        request,
        "services_particulars/lawyer.html"
    )

def licenses_info(request):
    return render(
        request,
        "services_particulars/licenses.html"
    )

def registration_info(request):
    return render(
        request,
        "services_particulars/registration.html"
    )
