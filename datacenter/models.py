from django.db import models
import django


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        '''Возвращает время пребывания в хранилище'''

        time_leaved = self.leaved_at
        time_entered = self.entered_at
        if time_leaved:
            duration = time_leaved - time_entered
            duration_hours = round(duration.total_seconds() // 60 // 60)
            duration_minutes = round(duration.total_seconds() // 60 % 60)
            return f'{duration_hours} ч.{duration_minutes} мин.'
        else:
            time_now = django.utils.timezone.localtime()
            duration = time_now - time_entered
            duration_hours = round(duration.total_seconds() // 60 // 60)
            duration_minutes = round(duration.total_seconds() // 60 % 60)
            return f'{duration_hours} ч.{duration_minutes} мин.'

    def find_long_visit(self):
        '''Возвращает True, если время нахождения в хранилище более strange_time'''

        time_now = django.utils.timezone.localtime()
        strange_time = 60   # 60 minutes
        if self.leaved_at:
            duration = self.leaved_at - self.entered_at
            duration_by_minutes = duration.total_seconds() // 60
            if duration_by_minutes > strange_time:
                return True
            return False
        else:
            duration = time_now - self.entered_at
            duration_by_minutes = duration.total_seconds() // strange_time
            if duration_by_minutes > strange_time:
                return True
            return False

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
