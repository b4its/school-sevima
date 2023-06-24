from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Pertanyaan,Kategori,Hasil

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def quiz(request):
    nilai = Hasil.objects.filter(user=request.user).values_list('kategori', flat=True)
    kategori = Kategori.objects.exclude(id__in=nilai)
    cek = Hasil.objects.filter(user=request.user).exists()
    print(nilai)
    context = {
        'kategori':kategori,
        'nilai':nilai,
        'cek':cek
    }
    return render(request, 'quiz.html',context)

def nilai_quiz(request):
    nilai_sementara = Hasil.objects.filter(user=request.user)
    nilai_ = Hasil.objects.filter(user=request.user).count()
    for i in nilai_sementara:
        total_nilai = float(i.total_nilai) * nilai_
    
    context = {
        'nilai':nilai_sementara,
        'total_nilai': float(total_nilai)
    }
    return render(request, 'show/nilai_quiz.html',context)

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
        kategori_id = request.POST['ambil_id']
        category = Kategori.objects.get(id = kategori_id)
        tanya = Pertanyaan.objects.filter(kategori=kategori_id)
        data = Pertanyaan.objects.filter(kategori=kategori_id).count()
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
   
        Hasil(user = user,kategori=category,total_nilai = nilai_akhir).save()
        messages.info(request,'Anda mendapatkan Nilai ' + str(nilai_akhir) )

            
        return redirect('quiz')
    else:
        return redirect('quiz')
