import django

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import datetime
from django.shortcuts import get_object_or_404, get_list_or_404


def passcard_info_view(request, passcode):
    # passcard_by_passcode = Passcard.objects.get(passcode=passcode)
    passcard_by_passcode = get_object_or_404(Passcard, passcode=passcode)
    # passcard_visit = Visit.objects.filter(passcard=passcard_by_passcode)
    passcard_visit = get_list_or_404(Visit, passcard=passcard_by_passcode)

    # Программируем здесь
    def long_visit():
        q = []
        for one_visit in passcard_visit:
            if one_visit.leaved_at:
                p = one_visit.leaved_at - one_visit.entered_at
                p_h = p.seconds // 60
                if p_h > 60:
                    q.append(p_h)
        return q

    # this_passcard_visits = [
    #     # {
    #     #     'entered_at': passcard_visit,
    #     #     'duration': long_visit(),
    #     #     'is_strange': False
    #     # },
    # ]

    def time_this_passcard_visit():
        this_passcard_visits = []
        for one_visit in passcard_visit:
            this_passcard_visits.append({'entered_at': one_visit.entered_at,
                                         'duration': one_visit.duration,
                                         'is_strange': False})

        return this_passcard_visits

    context = {
        'passcard': passcard_by_passcode,
        'this_passcard_visits': time_this_passcard_visit(),
        'time': time_this_passcard_visit()
    }
    return render(request, 'passcard_info.html', context)
