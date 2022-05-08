from datetime import date
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import DetailView
from django.views import View
from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q


def indexView(request):
    organization = Organization.objects.all()[:3],
    activities = Activity.objects.all()[:3],
    participants = Participant.objects.all()[:3]
    context = {
        'participants': participants,
        'activities': activities,
        'organization': organization,
    }
    return render(request, 'index.html', context)


def activityView(request):
    paginator = Paginator(Activity.objects.filter(active=True), 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'activities': Activity.objects.all(),
        'organizations': Organization.objects.all(),
        'participants': Participant.objects.all(),
        'host': Host.objects.all(),
        'page_obj': page_obj
    }
    return render(request, 'activities.html', context)


def activity_view_with_category(request, slug, *args, **kwargs):
    activity = Organization.objects.get(slug=slug)
    activities = activity.activity_set.filter(active=True)
    context = {
        'activities': activities,
        'host': Host.objects.all()
    }
    return render(request, 'activities_slog.html', context)




def activityDetail(request, slug):
    activity = Activity.objects.get(slug=slug)
    activities = Activity.objects.all()
    context = {
        'activity': activity,
        'activities': activities
    }
    return render(request, 'activity_detail.html', context)


class Contactview(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': ContactForm()
        }
        return render(request, 'basarili.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            c_form = form.save(commit=False)
            c_form.save()
            return render(request, 'basarili.html', context={'form': ContactForm()})


def participantsView(request):
    participants = Participant.objects.all()
    participantss = Participant.objects.all()
    activities = Activity.objects.all()
    context = {
        'participants': participants,
        'participantss': participantss,
        'activities': activities
    }
    return render(request, 'participant.html', context)





def participantView(request, id, *args, **kwargs):
    certificate = Certificate.objects.filter(active=True, activity_name=id)
    participant = Participant.objects.filter(activity_name=id)
    activities = Activity.objects.all()
    participants = Participant.objects.all()
    context = {
        'participants': participant,
        'activities': activities,
        'participantss': participants,
        'certificates': certificate,
    }
    return render(request, 'participant.html', context)


def hostView(request):
    context = {
        'hosts': Host.objects.all()
    }
    return render(request, 'host.html', context)


def organizationView(request):
    context = {
        'organizations': Organization.objects.all()
    }
    return render(request, 'organization.html', context)















def certificateView(request, id, *args, **kwargs):

    certificate = Certificate.objects.filter(active=True, cer_code=id)
    context = {
        'participants': Participant.objects.filter(activity_name=id),
        'certificates': certificate,
    }
    return render(request, 'certificates.html', context)


def certificatesView(request):

    certificates = Certificate.objects.all()
    context = {
        'certificates': certificates
    }
    return render(request, 'certificates.html', context)





def certificalar(request):
    context = {}
    activities = Activity.objects.all()
    participants = Participant.objects.all()
    certificate = Certificate.objects.all()
    keyword = request.GET.get("keyword")
    print(keyword)
    if keyword:
        # participant_name__phone_number__contains = keyword,
        participants = Participant.objects.filter(Q(name__contains=keyword) | Q(phone_number = keyword))
        print(participants)
        return render(request, "certificalar.html", {'participants': participants, 'activities': activities, 'certificates': certificate})





    context = {
        'certificates': certificate,
        'activities': activities,
        'participants': participants
    }
    return render(request, 'certificalar.html', context)

