from django.shortcuts import render
from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


# Create your views here.



def home(request):
    if request.method == 'POST':
        text=request.POST.get('text')
        summary_ans=summarizer(text, max_length=130, min_length=30, do_sample=False)
        return render(request,'index.html',{'SUMMARY_ANS':summary_ans})
    return render(request,'index.html')