from django.http import JsonResponse

# Create your views here.

def index(request):
    data = {

   "Name" : "Daniel Alvarado",

    "Track" : "Backend(Python)",

    "Message" : "How is you're day going so far today?  Its been a pretty busy mess for me lately."
    }

    return JsonResponse(data)