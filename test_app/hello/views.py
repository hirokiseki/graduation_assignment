from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
from django.views.generic import TemplateView
from .models import MathFormulas
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

# Create your views here.

class InputView(TemplateView):

    def __init__(self):
        alldata = MathFormulas.objects.all()
        self.params = {
            'title':'逆ポーランド計算機',
            'msg':'式を入力してください',
            'form':InputForm(),
            'pastData':alldata,
        }
    
    def get(self, request):
        logger.debug('====================get')

        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        logger.debug(request)
        self.params['form'] = InputForm(request.POST)
        self.params['answer'] = "計算結果:ダミー"
        return render(request, 'hello/index.html', self.params)


    # def index(request):
    #     alldata = MathFormulas.objects.all()
    #     params = {
    #         'title':'逆ポーランド計算機',
    #         'msg':'式を入力してください',
    #         'form':InputForm(),
    #         'pastData':alldata,
    #     }
    #     return render(request, 'hello/index.html', params)