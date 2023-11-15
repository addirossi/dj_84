from django.http import HttpResponse, Http404
from django.shortcuts import render

from main.models import Car

def test_page(request):
    return HttpResponse('Всем большой большой привет!')


def html_page(request):
    content = """
<!DOCTYPE html>
<html>
<body>

<h1>This is heading 1</h1>
<h2>This is heading 2</h2>
<h3>This is heading 3</h3>
<h4>This is heading 4</h4>
<h5>This is heading 5</h5>
<h6>This is heading 6</h6>

</body>
</html>
"""
    return HttpResponse(content)


def cars_list(request):
    cars = Car.objects.all()
    #SELECT * FROM car;
    render(request, 'list.html', {'cars': cars})


def car_details(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        print(f'Car id is: {car.price}')
        return render(request, 'details.html', {'car': car})
    except Car.DoesNotExist:
        raise Http404('Car not found')
