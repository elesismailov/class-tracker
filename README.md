# School Tracker Application

-> На русском: [README.ru.md](https://github.com/elesismailov/class-tracker/blob/main/README.ru.md)

## How to run it:
- Make sure Docker is installed - `docker --version`
- Clone the repo - `git clone https://github.com/elesismailov/class-tracker.git`
- Go to ClassTracker forlder - `cd ClassTracker/`
- Spin up and build the docker image - `docker-compose up -d --build`
- Migrate the tables - `docker-compose exec web python manage.py migrate`
    
    ![Untitled](Readme%20md%20e9ef56d06b614c28bc1ea42d2bfdc393/Untitled.png)
    
- Create super user - `docker-compose exec web python manage.py createsuperuser`
    
    ![Untitled](Readme%20md%20e9ef56d06b614c28bc1ea42d2bfdc393/Untitled%201.png)
    
- Create a school
    - Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) in your browser and log in with the superuser credentials
        
        ![Untitled](Readme%20md%20e9ef56d06b614c28bc1ea42d2bfdc393/Untitled%202.png)
        
    - Add new school
        
        ![Untitled](Readme%20md%20e9ef56d06b614c28bc1ea42d2bfdc393/Untitled%203.png)
        
        ![Untitled](Readme%20md%20e9ef56d06b614c28bc1ea42d2bfdc393/Untitled%204.png)
        
    - Go to [http://127.0.0.1:8000/sign-up/](http://127.0.0.1:8000/sign-up/), fill out the form, sign up
        
        ![Untitled](Readme%20md%20e9ef56d06b614c28bc1ea42d2bfdc393/Untitled%205.png)
        
- Set up email
    - In Dockerfile replace change the `your@email.com` and `your_password` with your credentials for and email
        
        ```docker
        ENV EMAIL_HOST_USER='your@email.com' # change this
        ENV EMAIL_HOST_PASSWORD='your_password' # change this
        ```
        
- Explore!