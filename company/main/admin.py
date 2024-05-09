from django.contrib import admin, messages


from .models import Feedback
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    NUM_OF_LAST_FEEDBACKS = 10

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        if obj in Feedback.objects.all()[:FeedbackAdmin.NUM_OF_LAST_FEEDBACKS]:
            messages.error(request, f"You cannot delete one of the {FeedbackAdmin.NUM_OF_LAST_FEEDBACKS} last feedbacks")
            return False
        return True

admin.site.register(Feedback, FeedbackAdmin)
