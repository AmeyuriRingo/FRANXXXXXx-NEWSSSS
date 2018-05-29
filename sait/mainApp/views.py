from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homepage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Если у вас остались вопросы, то задавайте их по телефону или почте', ' +375(29)757-23-12, nickos_k@mail.ru']})
