from django.contrib import admin
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe

from .models import *
from django.contrib import messages


class BlogAdmin(admin.ModelAdmin):
    list_display = ('activity_name', 'starttime', 'endtime')

admin.site.register(Activity, BlogAdmin)

class HostAdmin(admin.ModelAdmin):

    def response_change(self, request, obj, post_url_continue=None):
        activity = request.POST.getlist('activity_name')

        selected = Activity.objects.filter(id__in=activity)


        a = len(selected)

        # for t in selected:
        #     if t.Is_Past == "Past":
        #         messages.add_message(request, messages.WARNING,
        #                              f'{t} activity has finished at {t.endtime.date()}')
        #         return HttpResponseRedirect(request.path_info)





        today = date.today()

        def hata(i, b):
            messages.add_message(request, messages.ERROR, f'you can select only one of {selected[i]} or {selected[b]}')
            return HttpResponseRedirect(request.path_info)

        if a > 1 and selected:
            for i in range(a - 1):

                for b in range(i + 1, a):
                    if selected[i].starttime.date() == selected[b].starttime.date():

                        if selected[i].starttime.time() == selected[b].starttime.time() and selected[
                            i].endtime.time() == selected[b].endtime.time():
                            hata(i, b)
                            break

                        if selected[i].starttime.time() >= selected[b].starttime.time() \
                                and selected[i].endtime.time() >= selected[b].endtime.time() \
                                and selected[i].starttime.time() <= selected[b].endtime.time():
                            hata(i, b)
                            break

                        if selected[b].starttime.time() >= selected[i].starttime.time() and \
                                selected[b].endtime.time() >= selected[i].endtime.time() \
                                and selected[b].starttime.time() <= selected[i].endtime.time():
                            hata(b, i)
                            break

                        if selected[i].starttime.time() <= selected[b].starttime.time() \
                                and selected[i].endtime.time() <= selected[b].endtime.time() \
                                and selected[b].starttime.time() <= selected[i].endtime.time():
                            hata(i, b)
                            break

                        if selected[b].starttime.time() <= selected[i].starttime.time() \
                                and selected[b].endtime.time() <= selected[i].endtime.time() \
                                and selected[i].starttime.time() <= selected[b].endtime.time():
                            hata(i, b)
                            break

                        if selected[b].starttime.time() <= selected[i].starttime.time() \
                                and selected[b].endtime.time() >= selected[i].endtime.time():
                            hata(i, b)
                            break

                        elif selected[i].starttime.time() <= selected[b].starttime.time() \
                                and selected[i].endtime.time() >= selected[b].endtime.time():
                            hata(i, b)
                            break

                        if selected[i].starttime.time() >= selected[b].starttime.time() \
                                and selected[i].endtime.time() <= selected[b].endtime.time() \
                                and selected[b].starttime.time() <= selected[i].endtime.time():
                            hata(i, b)
                            break

                        elif selected[b].starttime.time() >= selected[i].starttime.time() \
                                and selected[b].endtime.time() <= selected[i].endtime.time() \
                                and selected[i].starttime.time() <= selected[b].endtime.time():
                            hata(i, b)
                            break


                        else:
                            if selected[i].starttime.date() >= today or selected[b].starttime.date() >= today:
                                messages.add_message(request, messages.SUCCESS, f'{selected[b]} starts at {selected[b].starttime.date()}.  {selected[i]} starts at {selected[i].starttime.date()}')
                                return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/host/')

                            elif selected[i].starttime.date() <= today or selected[b].starttime.date() <= today:
                                messages.add_message(request, messages.WARNING, f'{selected[b]} finished at {selected[b].starttime.date()}.  {selected[i]} finished at {selected[i].starttime.date()}')
                                return HttpResponseRedirect(request.path_info)


                            else:
                                messages.add_message(request, messages.SUCCESS, f'successfully saved')
                                return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/host/')



                    elif selected[i].starttime.date() >= selected[b].starttime.date() and selected[b].starttime.date() <= today:
                        messages.add_message(request, messages.WARNING, f'this {selected[i]} start time is {selected[i].starttime.date()}  this {selected[b]} finished {selected[b].starttime.date()}')
                        # return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/host/')
                        return HttpResponseRedirect(request.path_info)

                    elif selected[b].starttime.date() >= selected[i].starttime.date() and selected[i].starttime.date() <= today:
                        messages.add_message(request, messages.WARNING, f'this {selected[b]} start time is {selected[b].starttime.date()}.  this {selected[i]} finished {selected[i].starttime.date()}')
                        # return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/host/')
                        return HttpResponseRedirect(request.path_info)

                    elif selected[b].starttime.date() >= today or selected[i].starttime.date() >= today:
                        messages.add_message(request, messages.SUCCESS,f'this {selected[b]} start time is {selected[b].starttime.date()}.  this {selected[i]} start time is {selected[i].starttime.date()}')
                        return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/host/')

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

        # for t in selected:
        #     if t.Is_Past == "Past":
        #         messages.add_message(request, messages.WARNING,
        #                              f'{t} activity has finished at {t.endtime.date()}')
        #         return HttpResponseRedirect(request.path_info)

        a = len(selected)
        print(a)
        today = date.today()

        def hata(i, b):
            messages.add_message(request, messages.ERROR, f'you can select only one of {selected[i]} or {selected[b]}')
            return HttpResponseRedirect(request.path_info)

        if a > 1 and selected:
            for i in range(a - 1):
                for b in range(i + 1, a):
                    if selected[i].starttime.date() == selected[b].starttime.date():

                        if selected[i].starttime.time() == selected[b].starttime.time() and selected[
                            i].endtime.time() == selected[b].endtime.time():
                            hata(i, b)
                            break

                        if selected[i].starttime.time() >= selected[b].starttime.time() \
                                and selected[i].endtime.time() >= selected[b].endtime.time() \
                                and selected[i].starttime.time() <= selected[b].endtime.time():
                            hata(i, b)
                            break

                        elif selected[b].starttime.time() >= selected[i].starttime.time() and \
                                selected[b].endtime.time() >= selected[i].endtime.time() \
                                and selected[b].starttime.time() <= selected[i].endtime.time():
                            hata(b, i)
                            break

                        if selected[i].starttime.time() <= selected[b].starttime.time() \
                                and selected[i].endtime.time() <= selected[b].endtime.time() \
                                and selected[b].starttime.time() <= selected[i].endtime.time():
                            hata(i, b)
                            break

                        elif selected[b].starttime.time() <= selected[i].starttime.time() \
                                and selected[b].endtime.time() <= selected[i].endtime.time() \
                                and selected[i].starttime.time() <= selected[b].endtime.time():
                            hata(i, b)
                            break

                        if selected[b].starttime.time() <= selected[i].starttime.time() \
                                and selected[b].endtime.time() >= selected[i].endtime.time():
                            hata(i, b)
                            break

                        elif selected[i].starttime.time() <= selected[b].starttime.time() \
                                and selected[i].endtime.time() >= selected[b].endtime.time():
                            hata(i, b)
                            break

                        if selected[i].starttime.time() >= selected[b].starttime.time() \
                                and selected[i].endtime.time() <= selected[b].endtime.time() \
                                and selected[b].starttime.time() <= selected[i].endtime.time():
                            hata(i, b)
                            break

                        elif selected[b].starttime.time() >= selected[i].starttime.time() \
                                and selected[b].endtime.time() <= selected[i].endtime.time() \
                                and selected[i].starttime.time() <= selected[b].endtime.time():
                            hata(i, b)
                            break

                        else:
                            if selected[i].starttime.date() >= today or selected[b].starttime.date() >= today:
                                messages.add_message(request, messages.SUCCESS,
                                                     f'{selected[b]} starts at {selected[b].starttime.date()}.  {selected[i]} starts at {selected[i].starttime.date()}')
                                return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/participant/')

                            elif selected[i].starttime.date() <= today or selected[b].starttime.date() <= today:
                                messages.add_message(request, messages.WARNING,
                                                     f'{selected[b]} finished at {selected[b].starttime.date()}.  {selected[i]} finished at {selected[i].starttime.date()}')
                                return HttpResponseRedirect(request.path_info)

                            elif selected[i].starttime.date() <= today:
                                messages.add_message(request, messages.WARNING,
                                                     f'{selected[i]} finished at {selected[i].starttime.date()}')
                                return HttpResponseRedirect(request.path_info)

                            elif selected[b].starttime.date() <= today:
                                messages.add_message(request, messages.WARNING,
                                                     f'{selected[b]} finished at {selected[b].starttime.date()}')
                                return HttpResponseRedirect(request.path_info)

                            else:
                                messages.add_message(request, messages.SUCCESS, f'successfully saved')
                                return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/participant/')



                    elif selected[i].starttime.date() >= selected[b].starttime.date() and selected[b].starttime.date() <= today:
                        messages.add_message(request, messages.WARNING,
                                             f'this {selected[i]} start time is {selected[i].starttime.date()}  this {selected[b]} finished {selected[i].starttime.date()}')
                        # return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/host/')
                        return HttpResponseRedirect(request.path_info)

                    elif selected[b].starttime.date() >= selected[i].starttime.date() and selected[i].starttime.date() <= today:
                        messages.add_message(request, messages.WARNING,f'this {selected[b]} start time is {selected[b].starttime.date()}.  this {selected[i]} finished {selected[i].starttime.date()}')
                        # return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/host/')
                        return HttpResponseRedirect(request.path_info)

                    elif selected[b].starttime.date() >= today or selected[i].starttime.date() >= today:
                        messages.add_message(request, messages.SUCCESS,f'this {selected[b]} start time is {selected[b].starttime.date()}.  this {selected[i]} start time is {selected[i].starttime.date()}')
                        return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/participant/')
                        # return HttpResponseRedirect(request.path_info)

        else:
            messages.add_message(request, messages.SUCCESS, f'successfully saved')
            return HttpResponseRedirect('http://127.0.0.1:8000/admin/Certificate/participant/')
        return HttpResponseRedirect(request.path_info)


admin.site.register(Participant, ParticipantAdmin)


class OrgAdmin(admin.ModelAdmin):
    list_display = ('org_name', 'authorized', 'slug')

admin.site.register(Organization, OrgAdmin)


admin.site.register(Certificate)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'activity', 'email')
    readonly_fields = ('activity', )
admin.site.register(ContactUs, ContactAdmin)

admin.site.register(Website)
admin.site.register(GoogleForm)

class SendEmailAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'subject', 'email')
admin.site.register(SendEmail,SendEmailAdmin)
