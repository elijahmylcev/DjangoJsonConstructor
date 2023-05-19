from django.db import models

# Create your models here.


class Subject(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_datetime = models.DateTimeField(auto_now=True, verbose_name='Дата модификации')
    code = models.CharField(verbose_name='code')

    class Meta:
        verbose_name = 'Какие-то сущности'


class SubjectApplicationCondition(models.Model):
    link_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='ID чего-то')
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_datetime = models.DateTimeField(auto_now=True, verbose_name='Дата модификации')
    document_fields_in_type_doc = models.JSONField(verbose_name='Объект настроек')

    class Meta:
        verbose_name = 'Правила для каких-то правил'

    def __str__(self):
        return f'Правила для {self.link_subject.code} #{self.link_subject.id}'
