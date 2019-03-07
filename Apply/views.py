from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
from django.urls import reverse
from Apply.models import Evaluation, Apply
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ApplyForm
from .forms import EvaluationForm
from django.db.models import Count

@staff_member_required
def evaluation(request, apply_id):
    if request.method == 'POST':
        evaluation = Evaluation()
        form = EvaluationForm(request.POST)

        if form.is_valid():
            point1 = form.cleaned_data['apply_point1']
            point2 = form.cleaned_data['apply_point2']
            point3 = form.cleaned_data['apply_point3']
            total = int(point1) + int(point2) + int(point3)
            avg = float(total) / 3.0
            avg = round(avg, 2)

            evaluation.apply_point1 = form.cleaned_data['apply_point1']
            evaluation.apply_point2 = form.cleaned_data['apply_point2']
            evaluation.apply_point3 = form.cleaned_data['apply_point3']
            evaluation.apply_point_comment = form.cleaned_data['apply_point_comment']
            evaluation.apply_point_total = total
            evaluation.apply_point_avg = avg
            evaluation.user_id = request.user
            evaluation.apply_id = Apply(apply_id)
            evaluation.save()

            apply = get_object_or_404(Apply, pk=apply_id)
            eval_count = Evaluation.objects.filter(apply_id = apply).count()
            apply.apply_total += total
            apply.apply_avg = apply.apply_total / eval_count
            apply.save()
            
            return HttpResponseRedirect(reverse('Apply:list'))
        return HttpResponseRedirect(reverse('Apply:list'))

    else:
        form = EvaluationForm()
        return render(request, 'Evaluation/evaluation.html', {'apply_id':apply_id, 'form':form})

def submit(request):
    if request.method == 'POST':
        apply = Apply()

        form = ApplyForm(request.POST)
        if form.is_valid():
            apply.apply_name =  form.cleaned_data['apply_name']
            apply.apply_schoolNum = form.cleaned_data['apply_schoolNum']
            apply.apply_phone = form.cleaned_data['apply_phone']
            apply.apply_department = form.cleaned_data['apply_department']
            apply.apply_location = form.cleaned_data['apply_location']
            apply.apply_email = form.cleaned_data['apply_email']
            apply.apply_question1 = form.cleaned_data['apply_question1']
            apply.apply_question2 = form.cleaned_data['apply_question2']
            apply.apply_question3 = form.cleaned_data['apply_question3']
            apply.save()
            
            return HttpResponseRedirect(reverse('Home:index'))

    else:
        form = ApplyForm()
        return render(request, 'Submit/submit.html', {'form':form})

    return render(request, 'Submit/submit.html')
        
def apply_list(request):
    applys = Apply.objects
    return render(request,'List/list.html', {'applys':applys})

def detail(request, apply_id):
    details = get_object_or_404(Apply, pk=apply_id)
    return render(request, 'Details/detail.html', {'details':details})


        
    


# Create your views here.
