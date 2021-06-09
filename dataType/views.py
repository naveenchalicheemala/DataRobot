from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from dataType.processors.urlprocessing import UrlProcessing
from .forms import HomeForm

urlProcessing = UrlProcessing()

# Home page view
def home(request):

    if request.method == 'POST':
        form = HomeForm(request.POST)

        # Check if the form is valid and assign the user input
        if form.is_valid():
            sheetUrl = form.cleaned_data['sheetUrl']
            sheetName = form.cleaned_data['sheetName']

            # Process url and get data in the sheet to find data type
            result = urlProcessing.processurl(sheetUrl, sheetName)
        else:

            # Raise exception when url or sheet name is not valid
            raise ValidationError(_('Please check whether the input url and sheet name are valid'))

        context = {
            'result': result,
            'form': form
        }

    else:
        form = HomeForm()
        context = {'form': form}

    return render(request, 'dataType/home.html', context)


