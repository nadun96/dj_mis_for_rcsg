from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Member


class CustomMemberCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Member
        fields = ('username', 'email', 'residence', 'birth_date', 'is_member', 'is_treasurer',
                  'is_storekeeper', 'is_secretary', 'is_troop_leader', 'is_scoutmaster')

    