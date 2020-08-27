from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list":[
        {"restaurant_name":"Macdonald's", "food_type":"Burgers"},
        {"restaurant_name":"KFC", "food_type":"Crispy"},
        {"restaurant_name":"Baskin Robens", "food_type":"Ice cream"}
        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object": {"restaurant_name":"Macdonald's", "food_type":"Burgers"}
    }
    return render(request, 'detail.html', context)
