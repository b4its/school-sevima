from django.shortcuts import render,redirect
from .models import Kunci,Jawaban
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def chat(request):
    jawaban = None
    if request.method == 'POST':
        key = request.POST['key']
        kunci = Kunci.objects.filter(kata_kunci = key)
        jawaban = Jawaban.objects.get(kunci__id__in = kunci)
        print(key + jawaban.penjelasan)
    
        
    return render(request, "chat.html",{'prompt':jawaban})

def proses_chat(request):
    if request.method == 'POST':
        key = request.POST['key']
        kunci = Kunci.objects.get(kata_kunci = key)
        jawaban = Jawaban.objects.get(kunci__id__in = kunci)
        print(key + jawaban.penjelasan)
    
        return redirect('chat')
    else:
        return redirect('chat')

