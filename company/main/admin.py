from django.contrib import admin, messages


from .models import Feedback, ContactInfo

# Register your models here.


class FeedbackAdmin(admin.ModelAdmin):
    NUM_OF_LAST_FEEDBACKS = 10

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of N last recent feedbacks."""
        if obj in Feedback.objects.all()[: FeedbackAdmin.NUM_OF_LAST_FEEDBACKS]:
            messages.error(
                request,
                f"You cannot delete one of the {FeedbackAdmin.NUM_OF_LAST_FEEDBACKS} last recent feedbacks",
            )
            return False
        return True


class ContactsInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(ContactInfo, ContactsInfoAdmin)
