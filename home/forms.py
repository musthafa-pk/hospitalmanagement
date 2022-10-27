from dataclasses import field, fields
from datetime import date
from tkinter import Widget
from django import forms
from.models import Booking

class DateInput(forms.Form):
    input_type : 'date'

class BookingForm (forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        Widgets = {
            'date': DateInput() 
        }
        labels = {
            'p_name' : "Patient Name",
            'p_phone': "Patient Phone",
            'p_email': "Patient Email",
            'doc_name' :"Doctors Name", 
            'booking_date' :"Booking Date",
        }

