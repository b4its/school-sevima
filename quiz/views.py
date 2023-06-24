from django.shortcuts import render,redirect
from .models import Pertanyaan,Kategori,Hasil

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def quiz(request):
    return render(request, 'quiz.html')

def question(request):
    quiz = Pertanyaan.objects.all()
    context = {
        'quiz':quiz
    }
    return render(request, 'question.html', context)

def proses(request):
    if request.method == 'POST':
        user = request.user
        tanya = Pertanyaan.objects.all()
        data = Pertanyaan.objects.count()
        total = 0
       
        for pertanyaan in tanya:
            benar = pertanyaan.jawaban_benar
            answer = request.POST['answer' + str(pertanyaan.id)]  # Ambil jawaban berdasarkan id pertanyaan
            
            if answer == benar:
                total += 1
            else:
                total = total
        nilai_sementara = 100 / data
        nilai_akhir = nilai_sementara * total
        print(nilai_akhir)
            

            
        return redirect('question')
    else:
        return redirect('question')
