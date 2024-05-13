from django.shortcuts import render
from django import http
from django.contrib import messages
from django.views import View

from .models import Feedback
from .forms import FeedbackForm, ContactForm

# Create your views here.


class HomeView(View):
    model_class = Feedback
    form_class = FeedbackForm
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {
                "feedbacks": self.model_class.objects.all()[:4],
                "feedback_form": FeedbackForm(),
                "contact_form": ContactForm(),
            }
        )

    def post(self, request, *args, **kwargs):
        feedback_form = FeedbackForm(request.POST)

        if feedback_form.is_valid():
            feedback_form.save()
            messages.success(request, "Відгук успішно збережено.")
        else:
            messages.error(request, "Помилка при заповненні форми.")

            if not "rating" in feedback_form.cleaned_data.keys():
                messages.error(
                    request, "Оцінка не вказана або вона не в межах між 1 і 5."
                )
            if not "text" in feedback_form.cleaned_data.keys():
                messages.error(request, "Текст не вказаний або він задовгий.")
            if not "user_name" in feedback_form.cleaned_data.keys():
                messages.error(request, "Ім'я не вказане або воно задовге.")

        return http.HttpResponseRedirect("")


def feedbacks(request):
    return render(
        request, "feedbacks.html", context={"feedbacks": Feedback.objects.all()}
    )


def about_page(request):
    return render(request, "about.html")


def lawyer_info(request):
    return render(request, "services_particulars/lawyer.html")


def licenses_info(request):
    return render(request, "services_particulars/licenses.html")


def registration_info(request):
    return render(request, "services_particulars/registration.html")
