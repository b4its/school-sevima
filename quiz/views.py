from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Pertanyaan,Kategori,Hasil

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def quiz(request):
    kategori = Kategori.objects.all()
    context = {
        'kategori':kategori
    }
    return render(request, 'quiz.html',context)

def question(request,id):
    category = Kategori.objects.get(pk = id)
    quiz = Pertanyaan.objects.filter(kategori = category)
    context = {
        'quiz':quiz,
        'kategori':category
    }
    return render(request, 'question.html', context)

def proses(request):
    if request.method == 'POST':
        user = request.user
        ambil_id = request.POST['ambil_id']
        tanya = Pertanyaan.objects.filter(kategori=ambil_id)
        data = Pertanyaan.objects.filter(kategori=ambil_id).count()
        nilai = 0
        for pertanyaan in tanya:
            benar = pertanyaan.jawaban_benar
            answer = request.POST['answer' + str(pertanyaan.id)]
            
            if answer == benar:
                nilai += 1
            else:
                nilai = nilai
        nilai_sementara = 100 / data
        nilai_akhir = nilai_sementara * nilai
        print(nilai_akhir)
        messages.info(request,'Anda mendapatkan Nilai ' + str(nilai_akhir) )

            
        return redirect('quiz')
    else:
        return redirect('quiz')
