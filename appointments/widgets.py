from django.forms import DateInput

class FengyuanChenDatePickerInput(DateInput):
    template_name = 'template/fengyuanchen_datepicker.html'
