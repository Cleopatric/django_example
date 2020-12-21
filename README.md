#  Run project

1. Clone git repository:
    ```sh
    git clone https://github.com/Cleopatric/django_example
    ```

2. Set virtual environment:
    ```sh
    python3 -m venv venv
    ```

3. Activate virtual environment:
    
    MacOS/Linux
    
    ```sh
    source venv/bin/activate
    ```
    
    Windows
    ```sh
    venv\Scripts\activate
    ```

4. Open project repository:

    ```sh
     cd django_project/
    ```
   
5. Install requirements:

    ```sh
     pip install -r requirements.txt
    ```

6. Run Django makemigrations:

    ```sh
    python manage.py runserver makemigrations 
    ```
   
7. Run Django migrations:

    ```sh
    python manage.py runserver migrate
    ```

8. Run Django app:

    ```sh
    python manage.py runserver 0.0.0.0:8000
    ```
 
   
# Docker run

Run services in the background:
```sh
docker-compose up -d
```


Run services in the foreground:
```sh
docker-compose up --build
```


Inspect volume:

```sh
docker volume ls
```
and
```sh
docker volume inspect <volume name>
```

View networks:
```sh
docker network ls
```

Bring services down:
```sh
docker-compose down
```
