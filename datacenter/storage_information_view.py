from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at__isnull=True)
    visit_durations = []
    for non_closed_visit in non_closed_visits:
        visit_durations.append({'duration': non_closed_visit.get_readably_duration()})
    context = {
        'non_closed_visits': non_closed_visits,
        'visit_durations': visit_durations
    }
    return render(request, 'storage_information.html', context)
