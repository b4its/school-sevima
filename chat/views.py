from django.shortcuts import render,redirect
from .models import Kunci,Jawaban,Bot_ai,Pengguna
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def chat(request):
    chat_bot = Bot_ai.objects.filter(user=request.user)
    pengguna = Pengguna.objects.filter(user=request.user)
    user = request.user
    if request.method == 'POST':
        key = request.POST['key']
        kunci2 = Kunci.objects.filter(kata_kunci = key)
        kunci3 = Kunci.objects.get(id__in = kunci2)
        jawaban = Jawaban.objects.get(kunci__id__in = kunci2)
        Bot_ai(user=user,kunci = kunci3,penjelasan=jawaban.penjelasan).save()

        Pengguna(user=user,pertanyaan=key).save()
    context ={
        'chat_bot' : chat_bot,
        'pengguna': pengguna
    }
        
    return render(request, "chat.html", context)

def proses_chat(request):
    if request.method == 'POST':
        key = request.POST['key']
        kunci = Kunci.objects.get(kata_kunci = key)
        jawaban = Jawaban.objects.get(kunci__id__in = kunci)
        print(key + jawaban.penjelasan)
    
        return redirect('chat')
    else:
        return redirect('chat')

