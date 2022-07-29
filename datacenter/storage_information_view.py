from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_list_or_404


def storage_information_view(request):
    # Программируем здесь
    visit = Visit.objects.filter(leaved_at=None)


    non_closed_visits = [
        {
            'who_entered': visit,
            'entered_at': visit,
            'duration': visit,
        }
    ]
    context = {
        'non_closed_visits': visit,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
