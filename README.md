## Низкоуровневая работа с веб

### Цель работы

Освоить основные навыки обращения c Web из программы на Python, средства парсинга веб-страниц, соответствующие библиотеки.

![image](https://user-images.githubusercontent.com/70951761/145885992-5dbf4d0b-aa38-408e-a988-d173709afcc8.png)


1. При ответе вашего сервера посылайте некоторые основные заголовки:
    1. Date
    2. Content-type
    3. Server
    4. Content-length
    5. Connection: close.

![image](https://user-images.githubusercontent.com/70951761/145886183-2c33a5dc-2a10-47a6-89b7-95cae4053d53.png)

2. Создайте файл настроек вашего веб-сервера, в котором можно задать прослушиваемый порт, рабочую директорию, максимальный объем запроса в байтах. Можете добавить собственные настройки по желанию.

![image](https://user-images.githubusercontent.com/70951761/145886243-ab5c9597-bc36-4a1d-aba2-9b677d9740bf.png)

3. Если файл не найден, сервер передает в сокет специальный код ошибки - 404.

![image](https://user-images.githubusercontent.com/70951761/145887921-a670d619-c7f4-4560-857b-1ebd06994bf2.png)

4. Сервер должен работать в многопоточном режиме.

![image](https://user-images.githubusercontent.com/70951761/145887960-0cb70d2c-c2f7-48ee-972e-914935f5610a.png)

5. Сервер должен вести логи в следующем формате: Дата запроса. IP-адрес клиента, имя запрошенного файла, код ошибки.

![image](https://user-images.githubusercontent.com/70951761/145889045-7d0463c1-d55b-407e-a136-87869ef16e77.png)

6. Добавьте возможность запрашивать только определенные типы файлов (.html, .css, .js и так далее). При запросе неразрешенного типа, верните ошибку 403.

![image](https://user-images.githubusercontent.com/70951761/145889692-1e1f3a94-8a3b-4deb-9d6d-3e5638c47071.png)

7. Реализуйте поддержку постоянного соединения с несколькими запросами.

<img width="288" alt="Снимок экрана 2021-12-14 в 00 14 54" src="https://user-images.githubusercontent.com/70951761/145890079-d161b468-c034-4680-99d4-a055846219e4.png">

8. Реализуйте поддержку бинарных типов данных, в частночти, картинок.

![image](https://user-images.githubusercontent.com/70951761/145890146-ea145807-50ab-4b77-b191-7e943d19fad6.png)


<!-- Docs to Markdown version 1.0β17 -->
