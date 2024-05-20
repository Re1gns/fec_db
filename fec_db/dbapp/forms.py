from django import forms
from .models import MemberInformation
from bootstrap_datepicker_plus.widgets import DatePickerInput

class MemberInformationForm(forms.ModelForm):
    class Meta:
        model = MemberInformation
        fields = '__all__'
        widgets = {
            'date_of_birth': DatePickerInput(),
            'w_year': DatePickerInput(),
            's_year': DatePickerInput(),
            'year1': DatePickerInput(),
            'year2': DatePickerInput(),
            'year3': DatePickerInput(),
            'year4': DatePickerInput(),
            'year5': DatePickerInput(),
            'current_class_year': DatePickerInput(),
            'current_school_year': DatePickerInput(),
        }