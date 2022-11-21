from .models import Memory, Interests, Profile


def lastMemory(request):
    memory = Memory.objects.all()
    return dict(lastm=memory[0])


def intersted(request):
    if request.user.is_authenticated:
        try:
            tags = Interests.objects.get(interest=request.user)
            return dict(tags=tags.tag.all())
        except Interests.DoesNotExist:
            return dict()
    return dict()


def detailProfile(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(profile=request.user)
            return dict(profile1=profile)
        except Profile.DoesNotExist:
            return dict()
    return dict()

def myPhoto(request):
    if request.user.is_authenticated:
        try:
            memory = Memory.objects.filter(writer=request.user)
            return dict(memoryph=memory)
        except Profile.DoesNotExist:
            return dict()
    return dict()



def randMemory(request):
    memory = Memory.objects.all()
    memory = memory[0:3]
    return dict(memory13=memory)


