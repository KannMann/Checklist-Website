
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    if request.method == 'POST':
            
            if 'step_1' in request.POST:
                    from automatedChecklist.automationPhases.step_1 import step1
                    step1()

            elif 'step_2' in request.POST:
                    from automatedChecklist.automationPhases.step_2 import step2
                    step2()

    return render(request, 'automatedChecklist/index.html')