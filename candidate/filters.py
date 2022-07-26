import django_filters
from  employer.models import Jobs


class JobFilter(django_filters.FilterSet):
    salary=django_filters.NumberFilter(field_name='salary',lookup_expr='lt')
    job_titel=django_filters.CharFilter(lookup_expr='icontains')
    location=django_filters.CharFilter(lookup_expr='icontains')
    role=django_filters.CharFilter(lookup_expr='icontains')
    qualification=django_filters.CharFilter(lookup_expr='icontains')


    class Meta:

        fields=[
            'posted_by',
            'job_titel',
            'role',
            'location',
            'salary',

        ]