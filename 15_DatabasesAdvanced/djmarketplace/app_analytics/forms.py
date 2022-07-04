from tkinter import Widget
from django import forms
from datetime import date


class SalesReportDateFiterForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'value': date.today()}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'value': date.today()}))