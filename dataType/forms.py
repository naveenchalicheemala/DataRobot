
from django import forms



class HomeForm(forms.Form):

    sheetUrl = forms.URLField(label='Google Sheet url', required=True,
                              error_messages={'Required': 'Please enter the google sheet url'},
                              widget=forms.TextInput(attrs={"placeholder": "Enter the google sheet url",
                                                            'class': 'form-control'}))

    sheetName = forms.CharField(label='Sheet Name', required=True,
                                error_messages={'Required': 'Please enter the sheet name'},
                                widget=forms.TextInput(attrs={"placeholder": "Enter the sheet name",
                                                              'class': 'form-control'}))
