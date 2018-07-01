from django.shortcuts import render


# Create your views here.
def goods(request):
    params = {}
    return render(request, 'goods.html', context=params)


def good(request, good_id):
    params = {'good_id': good_id}
    return render(request, 'good.html', context=params)