# Сайт PictureViewer #
## Краткое руководство
Сайт PictureViewer содержит:
1) Административная панель без авторизации. На административной панели есть страница с формой загрузки изображения. На форме есть три поля:
  * Название изображения;
  * описание изображения;
  * загрузка изображения.

На административной панели есть еще страница со списком изображений. Список состоит из названий и описаний. Возможность редактировать названия и описания, а также удалять картинку. Редактирование названия и описания, а также их удаление происходят без перехода на отдельную страницу и без обновления страницы со списком.
2) Главная страница. Javascript-cлайдер, меняющий по таймеру загруженные изображения. Показывается по одному изображению. Есть возможность листать картинки, кликая по стрелкам.
3) База данных. В базе есть таблица Picture со следующими полями:
  - id;
  - title - название картинки;
  - description - описание картинки;
  - filename - путь к файлу, сохраненному на сервере;
  - date - дата сохранения.
В таблицу записываются данные загруженной картинки. При редактировании или удалении картинки в списке в административной панели в базе также происходят соответствующие изменения.
