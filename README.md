# Яндекс.Афиша
Данный проект позволяет пользователю просматривать интересные места, которые будут отмечены на карте, к каждому месту есть фотографии и небольшое описание.

Посмотреть на работу сайта можно по адресу: [Сайт](https://norgius.pythonanywhere.com/)
## Как установить и запустить

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`

Вам потребуется настроить доступ к `БД`, создав файл `.env` и записав в нём настройки `базы данных` с которой предстоит работать.
```
DATABASE_ENGINE=
DATABASE_FILEPATH=
```
По умолчанию проект использует SQLite3, при использовании другой БД, вам придётся изменить код и работать уже с другими переменными окружения

Также в `.env` передать следующие параметры приложения:
```
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=

STATIC_URL=
STATIC_ROOT=

MEDIA_ROOT=
MEDIA_URL=
```
После того, как пропишете все необходимые настройки можно запустить команду `python3 manage.py migrate`

И запустите сервер командой `python3 manage.py runserver`

Сайт работает по адресу: [Сайт](https://norgius.pythonanywhere.com/)
## Работа в админке
Ссылка на админку: [Админка](https://norgius.pythonanywhere.com/admin/)

В админке для работы вам понадобиться поле `Places`. 
Здесь вы сможете самостоятельно добавлять, изменять или удалять данные.

Добавленные фотографии можно менять местами, выставляя наперед самые красивые на ваш взгляд.
## Загрузка новых данных
Вы можете загружать новые данные используя команду `load_place` и передавая в качестве аргумента ссылку на json-файл:
```
python3 manage.py load_place [ссылка]
```
Json-файл должен быть подобного формата:
```
{
    "title": "Экскурсионная компания «Легенды Москвы»",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4f793576c79c1cbe68b73800ae06f06f.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7a7631bab8af3e340993a6fb1ded3e73.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/a55cbc706d764c1764dfccf832d50541.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/65153b5c595345713f812d1329457b54.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0a79676b3d5e3b394717b4bf2e610a57.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e27f507cb72e76b604adbe5e7b5f315.jpg"
    ],
    "description_short": "Неважно, живёте ли вы в Москве всю жизнь или впервые оказались в столице, составить ёмкий, познавательный и впечатляющий маршрут по городу — творческая и непростая задача. И её с удовольствием берёт на себя экскурсионная компания «Легенды Москвы»!",
    "description_long": "<p>Экскурсия от компании «Легенды Москвы» — простой, удобный и приятный способ познакомиться с городом или освежить свои чувства к нему. Что выберете вы — классическую или необычную экскурсию, пешую прогулку или путешествие по городу на автобусе? Любые варианты можно скомбинировать в уникальный маршрут и создать собственную индивидуальную экскурсионную программу.</p><p>Компания «Легенды Москвы» сотрудничает с аккредитованными экскурсоводами и тщательно следит за качеством экскурсий и сервиса. Автобусные экскурсии проводятся на комфортабельном современном транспорте. Для вашего удобства вы можете заранее забронировать конкретное место в автобусе — это делает посадку организованной и понятной.</p><p>По любым вопросам вы можете круглосуточно обратиться по телефонам горячей линии.</p><p>Подробности узнавайте <a class=\"external-link\" href=\"https://moscowlegends.ru \" target=\"_blank\">на сайте</a>. За обновлениями удобно следить <a class=\"external-link\" href=\"https://vk.com/legends_of_moscow \" target=\"_blank\">«ВКонтакте»</a>, <a class=\"external-link\" href=\"https://www.facebook.com/legendsofmoscow?ref=bookmarks \" target=\"_blank\">в Facebook</a>.</p>",
    "coordinates": {
        "lng": "37.64912239999976",
        "lat": "55.77754550000014"
    }
}
```
Только собрав его в подобный формат и имея рабочие ссылки на изображения можно воспользоваться подобной командой.

В остальных случаях, данные можно заносить через [админку](https://norgius.pythonanywhere.com/admin/)
