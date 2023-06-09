from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http.response import JsonResponse
import sys
from io import StringIO
class IndexView(View):
    template_name = 'index.html'

    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)

    def post(self,request,*args, **kwargs):
        action = request.POST.get('action','')
        if action:
            try:
                exception = ""
                output = StringIO()
                sys.stdout = output
                code = request.POST.get('code')
                input_values = request.POST.get('input','')
                input_values = [inp.strip() for inp in input_values.split('\n')]
                input_index = 0

                def mock_input(*args, **kwargs):
                    nonlocal input_index
                    value = input_values[input_index]
                    input_index += 1
                    return value

                builtins = __import__('builtins')
                builtins.input = mock_input
            
                exec(code)
            except Exception as error:
                exception = error
            sys.stdout = output
            sys.stdout = sys.__stdout__
            captured_output = output.getvalue().strip()
            return JsonResponse({'output':f"{captured_output}{exception}"})
        else:
            return JsonResponse({'output':'No code entered'})
        



