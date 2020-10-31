from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Picture


def admin_add_picture(request):
    """Функция представления для страницы администратора с добавлением
    картинок."""

    if request.method == 'GET':
        # Отображается страница
        return render(request, 'app/admin.html')
    if request.method == 'POST':
        # Обрабатывается запрос на сохранение картинки.
        # Присланные имя, описание и файл
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')
        # Проверяем валидность присланных данных
        if title and description and file:
            # Картинка сохраняется в базу данных
            content = file.file.read()
            filename = 'static/imgs/'+file.name  # имя файла
            with open(filename, 'wb') as p:
                p.write(content)
            picture = Picture(title=title, description=description,
                              filename=filename)
            picture.save()
            return JsonResponse({}, status=201)
        else:
            # Запрос не выполнен
            return JsonResponse({}, status=400)


def admin_show_list(request):
    """Функция представления для страницы администратора со списком
    картинок."""

    if request.method in ('POST'):
        picture_id = request.POST.get('picture_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        try:
            # Получаем картинку
            picture = Picture.objects.get(id=picture_id)
        except Picture.DoesNotExist:
            # Картинки нет
            return JsonResponse({}, status=400)
        picture.title = title
        picture.description = description
        picture.save()
        return JsonResponse({}, status=200)
    if request.method == 'GET':
        pictures = Picture.objects.all()
        data = []
        for i, picture in enumerate(pictures, 1):
            data.append({'id': picture.id, 'num': i, 'title': picture.title,
                         'description': picture.description})
        return render(request, 'app/admin_list.html', context={'list': data})


def delete(request, picture_id):
    """Функция удаляет картинку по Id.
    :param picture_id: Id картинки для удаления."""

    if request.method == 'POST':
        try:
            # Получаем картинку
            picture = Picture.objects.get(id=picture_id)
        except Picture.DoesNotExist:
            # Картинки нет, ничего не удаляем
            return JsonResponse({}, status=400)
        # Удаляем картинку
        picture.delete()
        return JsonResponse({}, status=200)
    return JsonResponse({}, status=400)


def index(request):
    """Функция представления для главной страницы."""

    # Получаем все картинки из базы данных и отправляем их пользователю
    pictures = Picture.objects.all()
    data = []
    for i, picture in enumerate(pictures, 1):
        data.append({'id': picture.id, 'title': picture.title,
                     'description': picture.description,
                     'filename': picture.filename})
    return render(request, 'app/index.html', context={'list': data})
