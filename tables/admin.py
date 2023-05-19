from django.contrib import admin
from tables.models import Subject, SubjectApplicationCondition


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'modified_datetime', 'created_datetime')
    search_fields = ('id', 'code')


@admin.register(SubjectApplicationCondition)
class SubjectApplicationConditionAdmin(admin.ModelAdmin):
    list_display = ('link_subject', 'document_fields_in_type_doc')
