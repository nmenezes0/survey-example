from django.contrib import admin

from pulse_survey.survey.models import Result, Feedback


class ResultAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]  # Order by created_at in descending order


admin.site.register(Result)
admin.site.register(Feedback)
