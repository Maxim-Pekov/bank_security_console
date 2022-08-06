from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at__isnull=True)
    visits = []
    for non_closed_visit in non_closed_visits:
        visits.append({'duration': non_closed_visit.get_readably_duration(),
                                'owner_name': non_closed_visit.passcard.owner_name,
                                'entered_at': non_closed_visit.entered_at,
                                'suspect': non_closed_visit.find_long_visit()
                       })
    context = {
        'non_closed_visits': visits
    }
    return render(request, 'storage_information.html', context)
