from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404


def passcard_info_view(request, passcode):
    passcard_by_passcode = get_object_or_404(Passcard, passcode=passcode)
    passcard_visit = Visit.objects.order_by('-entered_at').filter(passcard=passcard_by_passcode)
    get_list_or_404(passcard_visit)
    # passcard_visit = get_list_or_404(Visit, passcard=passcard_by_passcode)


    def time_this_passcard_visit():
        this_passcard_visits = []
        for one_visit in passcard_visit:
            this_passcard_visits.append({'entered_at': one_visit.entered_at,
                                         'duration': one_visit.duration,
                                         'is_strange': one_visit.long_visit()})
        return this_passcard_visits

    context = {
        'passcard': passcard_by_passcode,
        'this_passcard_visits': time_this_passcard_visit(),
    }
    return render(request, 'passcard_info.html', context)
