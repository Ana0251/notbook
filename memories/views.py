from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Memory, Profile, Interests, Comment
from .forms import MemoryForm, ProfileForm, InterestsForm, CommentForm
import random


# Create your views here.
def index(request):
    memories = Memory.objects.filter(type='pu')

    return render(request, 'notebook/index.html',
                      {'memories': memories})


class MemoryView(ListView):
    def get(self, request):
        try:
            memories = Memory.objects.filter(writer=request.user)
            return render(request, 'notebook/memories.html',
                          {'memories': memories})
        except TypeError:
            return redirect('memories:home')


class MemoryDetailView(DetailView):
    def get(self, request, memory_id):
        memory = Memory.objects.get(id=memory_id)
        memories = Memory.objects.all()
        try:
            comments = Comment.objects.filter(memory=memory_id)
            form = CommentForm()
        except Comment.DoesNotExist:
            form = CommentForm()
        return render(request, 'notebook/memory.html',
                      {'memories': memories, 'memory': memory, 'form': form, 'comments': comments})

    def post(self, request, memory_id):
        form = CommentForm(data=request.POST)
        print("1")
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.memory = Memory.objects.get(id=memory_id)
            new_comment.writer = request.user
            new_comment.save()
            return redirect('memories:memory', memory_id)


class NewMemoryView(ListView):
    def get(self, request):
        form = MemoryForm()
        memories = Memory.objects.all()
        return render(request, 'notebook/new_memory.html',
                      {'form': form, 'memories': memories})

    def post(self, request):
        form = MemoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_memory = form.save(commit=False)
            new_memory.writer = request.user
            new_memory.save()
        return redirect('memories:memorys')


class EditMemoryView(ListView):
    def get(self, request, memory_id):
        memory = Memory.objects.get(id=memory_id)
        form = MemoryForm(instance=memory)
        return render(request, 'notebook/edit_memory.html', {'memory': memory, 'form': form})

    def post(self, request, memory_id):
        print(request.POST)
        memory = Memory.objects.get(id=memory_id)
        form = MemoryForm(instance=memory, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('memories:memorys')


class EditProfileView(ListView):
    def get(self, request):
        try:
            profile = Profile.objects.get(profile=request.user)
            form = ProfileForm(instance=profile)
        except TypeError:
            return redirect("users:login")
        except Profile.DoesNotExist:
            form = ProfileForm()

        return render(request, 'notebook/edit_profile.html', {'form': form})

    def post(self, request):
        try:
            profile = Profile.objects.get(profile=request.user)
            form = ProfileForm(instance=profile, data=request.POST, files=request.FILES)
        except Profile.DoesNotExist:
            form = ProfileForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.profile = request.user
            new_profile.save()
            return redirect('memories:home')


class EditInterstedView(ListView):
    def get(self, request):
        try:
            interest = Interests.objects.get(interest=request.user)
            form = InterestsForm(instance=interest)
        except Interests.DoesNotExist:
            form = InterestsForm()
        return render(request, 'notebook/edit_interest.html', {'form': form})

    def post(self, request):
        try:
            interest = Interests.objects.get(interest=request.user)
            form = InterestsForm(instance=interest, data=request.POST)
        except Interests.DoesNotExist:
            interest = Interests.objects.create(interest=request.user)
            form = InterestsForm(intance=interest, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('memories:home')



