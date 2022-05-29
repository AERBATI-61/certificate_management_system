from datetime import date

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views import View
from .models import *
from .forms import *
from django.db.models import Q
import random
# from utils.pdf import render_to_pdf
from .decorators import allowed_users


# pdf
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render, get_object_or_404





@login_required(login_url='login')
def render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    certificate = get_object_or_404(Certificate, pk=pk)
    activities = Activity.objects.all()
    template_path = '../templates/pdf.html'
    context = {
        'certificate': certificate,
        'activities': activities,

    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response












@login_required(login_url='login')
def indexView(request):
    organizations = Organization.objects.all()
    hosts = Host.objects.all()
    activities = Activity.objects.all()
    participants = Participant.objects.all()


    selected_activities = []
    while len(selected_activities) < 3:
        activity = random.choice(activities)
        if activity not in selected_activities:
            selected_activities.append(activity)



    selected_hosts = []
    while len(selected_hosts) < 3:
        host = random.choice(hosts)
        if host not in selected_hosts:
            selected_hosts.append(host)

    selected_participants = []
    while len(selected_participants) < 3:
        participant = random.choice(participants)
        if participant not in selected_participants:
            selected_participants.append(participant)

    selected_organizations = []
    while len(selected_organizations) < 3:
        organization = random.choice(organizations)
        if organization not in selected_organizations:
            selected_organizations.append(organization)





    context = {
        'participants': participants,
        'activities': activities,
        'selected_activities': selected_activities,
        'selected_hosts': selected_hosts,
        'selected_participants': selected_participants,
        'organizations': organizations,
        'selected_organizations': selected_organizations,
        'hosts': hosts,
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def activity_view_with_category(request, slug, *args, **kwargs):
    activity = Organization.objects.get(slug=slug)
    activities = activity.activity_set.filter(active=True)
    context = {
        'activities': activities,
        'host': Host.objects.all()
    }
    return render(request, 'activities_slog.html', context)



@login_required(login_url='login')
def activityDetail(request, slug):
    activity = Activity.objects.get(slug=slug)
    activities = Activity.objects.all()
    context = {
        'activity': activity,
        'activities': activities
    }
    return render(request, 'activity_detail.html', context)





@login_required(login_url='login')
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


@login_required(login_url='login')
def decoratorView(request):
    return render(request, 'decorators.html')


@login_required(login_url='login')
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




@login_required(login_url='login')
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

@login_required(login_url='login')
def hostView(request):
    context = {
        'hosts': Host.objects.all()
    }
    return render(request, 'host.html', context)

@login_required(login_url='login')
def organizationView(request):
    context = {
        'organizations': Organization.objects.all()
    }
    return render(request, 'organization.html', context)














@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def certificateView(request, id, *args, **kwargs):

    certificate = Certificate.objects.filter(active=True, cer_code=id)
    context = {
        'participants': Participant.objects.filter(activity_name=id),
        'certificates': certificate,
    }
    return render(request, 'certificates.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def certificatesView(request):

    certificates = Certificate.objects.all()
    context = {
        'certificates': certificates
    }
    return render(request, 'certificates.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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







