from django.shortcuts import render,redirect
from .models import Kunci,Jawaban,Bot_ai,Pengguna
from django.contrib import messages

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def chat(request):
    chat_bot = Bot_ai.objects.filter(user=request.user)
    pengguna = Pengguna.objects.filter(user=request.user)
    user = request.user
    maaf = "Mohon maaf kak saya tidak bisa memahami apa yang anda maksud?"
    combined_data = zip(Bot_ai.objects.all(), Pengguna.objects.all())
    if request.method == 'POST':
        key = request.POST['key']
        kunci2 = Kunci.objects.filter(kata_kunci = key)
        if kunci2.exists()  :
            kunci3 = Kunci.objects.get(id__in = kunci2)
            jawaban = Jawaban.objects.get(kunci__id__in = kunci2)
            Bot_ai(user=user,kunci = kunci3,penjelasan=jawaban.penjelasan).save()
            Pengguna(user=user,pertanyaan=key).save()
            messages.success(request,'Pesan anda telah berhasil terkirim ')

       
        else:
            messages.warning(request,'Mohon maaf, kak ray tidak mengerti dengan yang anda maksud :) ' )
           
            Bot_ai(user=user,kunci = None,penjelasan=str(maaf)).save()
            Pengguna(user=user,pertanyaan=key).save()
    
        
    context ={
        'chat_bot' : chat_bot,
        'pengguna': pengguna,
        'combined_data':combined_data
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

def cleaner(request):
    Bot_ai.objects.all().delete()
    Pengguna.objects.all().delete()
    messages.success(request,'Pesan telah berhasil di hapus ' )
    return redirect('chat')

