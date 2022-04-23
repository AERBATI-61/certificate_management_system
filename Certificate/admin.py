from django.contrib import admin
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe

from .models import *
from django.contrib import messages


class BlogAdmin(admin.ModelAdmin):
    list_display = ('activity_name', 'starttime', 'endtime')


class HostAdmin(admin.ModelAdmin):


    def response_change(self, request, obj, post_url_continue=None):
        activity = request.POST.getlist('activity_name')
        selected = Activity.objects.filter(id__in=activity)
        print('selected', selected)



        a = len(selected)
        today = date.today()

        def hata(i, b):
            messages.add_message(request, messages.ERROR, f'you can select only one of {selected[i]} or {selected[b]}')
            return HttpResponseRedirect(request.path_info)

        if a > 1 and selected:
            for i in range(a - 1):
                for b in range(i + 1, a):
                    if selected[i].starttime.date() == today:

                        if selected[i].starttime.time() == selected[b].starttime.time() and selected[
                            i].endtime.time() == selected[b].endtime.time():
                            hata(i, b)

                        if selected[i].starttime.time() >= selected[b].starttime.time() \
                                and selected[i].endtime.time() >= selected[b].endtime.time() \
                                and selected[i].starttime.time() <= selected[b].endtime.time():
                            hata(i, b)

                        if selected[b].starttime.time() >= selected[i].starttime.time() and \
                                selected[b].endtime.time() >= selected[i].endtime.time() \
                                and selected[b].starttime.time() <= selected[i].endtime.time():
                            hata(b, i)

                        if selected[i].starttime.time() <= selected[b].starttime.time() \
                                and selected[i].endtime.time() <= selected[b].endtime.time() \
                                and selected[b].starttime.time() <= selected[i].endtime.time():
                            hata(i, b)

                        if selected[b].starttime.time() <= selected[i].starttime.time() \
                                and selected[b].endtime.time() <= selected[i].endtime.time() \
                                and selected[i].starttime.time() <= selected[b].endtime.time():
                            hata(i, b)

                        if selected[b].starttime.time() <= selected[i].starttime.time() \
                                and selected[b].endtime.time() >= selected[i].endtime.time():
                            hata(i, b)

                        elif selected[i].starttime.time() <= selected[b].starttime.time() \
                                and selected[i].endtime.time() >= selected[b].endtime.time():
                            hata(i, b)

                        if selected[i].starttime.time() >= selected[b].starttime.time() \
                                and selected[i].endtime.time() <= selected[b].endtime.time()\
                                and selected[b].starttime.time() <= selected[i].endtime.time():
                            hata(i, b)

                        elif selected[b].starttime.time() >= selected[i].starttime.time() \
                                and selected[b].endtime.time() <= selected[i].endtime.time()\
                                and selected[i].starttime.time() <= selected[b].endtime.time():
                            hata(i, b)

                        else:
                            messages.add_message(request, messages.SUCCESS, f'successfully saved')
                            return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/host/')

                    elif selected[i].starttime.date() > today:
                        messages.add_message(request, messages.WARNING, f'start time is {selected[i].starttime.date()}')
                        return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/host/')
                    else:
                        messages.add_message(request, messages.WARNING,
                                             f'This activity is end at {selected[i].starttime.date()}')
                        return HttpResponseRedirect(request.path_info)

        else:
            messages.add_message(request, messages.SUCCESS, f'successfully saved')
            return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/host/')
        return HttpResponseRedirect(request.path_info)


admin.site.register(Host, HostAdmin)


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    def response_change(self, request, obj, post_url_continue=None):
        activity = request.POST.getlist('activity_name')
        selected = Activity.objects.filter(id__in=activity)
        print('selected', selected)

        a = len(selected)
        print(a)
        today = date.today()

        def hata(i, b):
            messages.add_message(request, messages.ERROR, f'you can select only one of {selected[i]} or {selected[b]}')
            return HttpResponseRedirect(request.path_info)

        if a > 1 and selected:
            for i in range(a - 1):
                for b in range(i + 1, a):
                    if selected[i].starttime.date() == today:

                        if selected[i].starttime.time() == selected[b].starttime.time() and selected[
                            i].endtime.time() == selected[b].endtime.time():
                            hata(i, b)

                        if selected[i].starttime.time() >= selected[b].starttime.time() \
                                and selected[i].endtime.time() >= selected[b].endtime.time() \
                                and selected[i].starttime.time() <= selected[b].endtime.time():
                            hata(i, b)

                        elif selected[b].starttime.time() >= selected[i].starttime.time() and \
                                selected[b].endtime.time() >= selected[i].endtime.time() \
                                and selected[b].starttime.time() <= selected[i].endtime.time():
                            hata(b, i)

                        if selected[i].starttime.time() <= selected[b].starttime.time() \
                                and selected[i].endtime.time() <= selected[b].endtime.time() \
                                and selected[b].starttime.time() <= selected[i].endtime.time():
                            hata(i, b)

                        elif selected[b].starttime.time() <= selected[i].starttime.time() \
                                and selected[b].endtime.time() <= selected[i].endtime.time() \
                                and selected[i].starttime.time() <= selected[b].endtime.time():
                            hata(i, b)

                        if selected[b].starttime.time() <= selected[i].starttime.time() \
                                and selected[b].endtime.time() >= selected[i].endtime.time():
                            hata(i, b)

                        elif selected[i].starttime.time() <= selected[b].starttime.time() \
                                and selected[i].endtime.time() >= selected[b].endtime.time():
                            hata(i, b)

                        if selected[i].starttime.time() >= selected[b].starttime.time() \
                                and selected[i].endtime.time() <= selected[b].endtime.time() \
                                and selected[b].starttime.time() <= selected[i].endtime.time():
                            hata(i, b)

                        elif selected[b].starttime.time() >= selected[i].starttime.time() \
                                and selected[b].endtime.time() <= selected[i].endtime.time() \
                                and selected[i].starttime.time() <= selected[b].endtime.time():
                            hata(i, b)

                        else:
                            messages.add_message(request, messages.SUCCESS, f'successfully saved')
                            return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/host/')

                    elif selected[i].starttime.date() > today:
                        messages.add_message(request, messages.WARNING, f'start time is {selected[i].starttime.date()}')
                        return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/participant/')
                    else:
                        messages.add_message(request, messages.WARNING,
                                             f'This activity is end at {selected[i].starttime.date()}')
                        return HttpResponseRedirect(request.path_info)

        else:
            messages.add_message(request, messages.SUCCESS, f'successfully saved')
            return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/participant/')
        return HttpResponseRedirect(request.path_info)


admin.site.register(Participant, ParticipantAdmin)


class OrgAdmin(admin.ModelAdmin):
    list_display = ('org_name', 'authorized', 'slug')


admin.site.register(Organization, OrgAdmin)

admin.site.register(Activity, BlogAdmin)
admin.site.register(Certificate)
admin.site.register(ContactUs)









