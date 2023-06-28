# School Tracker Application

-> In English: [README.ru.md](https://github.com/elesismailov/class-tracker/blob/main/README.ru.md)

## Как запустить:
- Проверьте установлен ли Docker - `docker --version`
- Клонируйте репозитори - `git clone https://github.com/elesismailov/class-tracker.git`
- Перейдите в папку ClassTracker/ - `cd ClassTracker/`
- Запустите изображение - `docker-compose up -d --build`
- Мигрируйте таблицы - `docker-compose exec web python manage.py migrate`
    
    ![Untitled](Readme%20md%20e9ef56d06b614c28bc1ea42d2bfdc393/Untitled.png)
    
- Создайте суперюзера - `docker-compose exec web python manage.py createsuperuser`
    
    ![Untitled](Readme%20md%20e9ef56d06b614c28bc1ea42d2bfdc393/Untitled%201.png)
    
- Создайте школу:
    - Перейдите в браузере сюда [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) и войдите с логином суперюзера
        
        ![Untitled](Readme%20md%20e9ef56d06b614c28bc1ea42d2bfdc393/Untitled%202.png)
        
    - Добавьте школу: 
        
        ![Untitled](Readme%20md%20e9ef56d06b614c28bc1ea42d2bfdc393/Untitled%203.png)
        
        ![Untitled](Readme%20md%20e9ef56d06b614c28bc1ea42d2bfdc393/Untitled%204.png)
        
    - Перейдите в браузере сюда [http://127.0.0.1:8000/sign-up/](http://127.0.0.1:8000/sign-up/), заполните форму, зарегистрируйтесь
        
        ![Untitled](Readme%20md%20e9ef56d06b614c28bc1ea42d2bfdc393/Untitled%205.png)
        
- Настройте email для рассылки
    - В Dockerfile замените `your@email.com` и `your_password` на те которые будут отсылать
        
        ```docker
        ENV EMAIL_HOST_USER='your@email.com' # замените
        ENV EMAIL_HOST_PASSWORD='your_password' # замените
        ```
        