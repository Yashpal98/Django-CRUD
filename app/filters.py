import django_filters
from django import forms
from .models import Person, hobby_choice


class ListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    hobby = django_filters.MultipleChoiceFilter(field_name='hobby', choices=hobby_choice, widget=forms.CheckboxSelectMultiple, lookup_expr='icontains')
    
    class Meta:
        model = Person
        fields = ['name', 'gender','hobby']

        # fields = {
        #     'name': ['icontains'],
        #     'gender': ['exact'],
        #     'hobby': ['icontains']
        # }

        # fields = '__all__'
        # widgets = {
        #     'gender': forms.RadioSelect
        #    }

        # def filter_hobby(self, queryset, hobby):
        #     return queryset.filter(hobby__contains=hobby.split(','))