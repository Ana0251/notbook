from django import forms
from .models import Memory, Profile, Interests, Comment


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ('title', 'text', 'place',
                  'history', 'ftravel', 'image',
                  'type')
        labels = {'title': 'موضوع:', 'text': 'متن:', 'place': 'مکان:',
                  'history': 'تاریخ:', 'ftravel': 'هم خاطره ها:', 'image': 'عکس خاطره:',
                  'type': 'نوع خاطره:'}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('job', 'place', 'birthday', 'avatar')
        labels = {'job': 'شغل:', 'place': 'محل زندگی:', 'birthday': 'تاریخ تولد:', 'avatar': 'عکس:'}

class InterestsForm(forms.ModelForm):
    class Meta:
        model = Interests
        fields = ('tag',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

