from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def result_page(request):
    return render(request, 'result.html')

@csrf_exempt
def average(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        num3 = request.POST.get('num3')
        num4 = request.POST.get('num4')
        print(f'num1: {num1}, num2: {num2}, num3: {num3}, num4: {num4}')

        if num1 is not None and num2 is not None:
            try:
                num1 = int(num1)
                num2 = int(num2)
                num3 = int(num3)
                num4 = int(num4)
                result = (num1 + num2 + num3 + num4) / 4
                return render(request, 'result.html', {'num1': num1, 'num2': num2, 'num3': num3, 'num4': num4, 'result': result})
            except ValueError:
                error_message = 'Os valores informados não são números válidos.'
                return render(request, 'result.html', {'error': error_message})
        else: 
            error_message = 'Por favor, forneça quatro notas.'
            return render(request, 'result.html', {'error': error_message})
    else:
        error_message = 'Método não permitido.'
        return render(request, 'result.html', {'error': error_message})
