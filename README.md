# Together
Social media application build by following the book Django 3 By Example: Build powerful and reliable Python web applications from scratch, 3rd Edition by Antonio Mele.

Application is a basic start for social media app. It allows to register, login, logout, upload images as a posts. Like/unlike images, follow/unfollow users. It has a basic user profile. It is prepared to be login with social app authentication (Google, Facebook). It has a bookmark for inserting images from other sites. It counts likes and views.
With this app I learned how to use Django framework and how to build a social media app.

I am using this app as a base for more advanced social media app and I think it is a good start for anyone who wants to build a social media app.

Application is build using Django 4.0.1 and Python 3.10.0

App is prepared to be login with social app authentication (Google, Facebook) - extra configuration is needed.

App has set email backend from smtp.google.com - extra configuration is needed.

For full functionality of the app, it is recommended to run the app from the runserver_plus command and connect to the local Redis database server.

## Simple Installation - allow to see the front end of the app - most of the features require extra installation
1. Clone the repository
2. Create a virtual environment
3. Install the requirements
4. Create a .env file and add the following:
    - SECRET_KEY=your_secret_key
    - DEBUG=True
    - ALLOWED_HOSTS=localhost,
    - EMAIL_HOST_USER=your_email
    - EMAIL_HOST_PASSWORD=your_password
5. Run the migrations
6. Create a superuser
7. Run the server to start and test the app locally.

## Extra Installation - allow to use all the features of the app

### Runserver_plus - django-extensions

1. Install below extensions:
```
   pip install django-extensions==2.2.5
   pip install werkzeug==0.16.0
   pip install pyOpenSSL==19.0.0
```
2. Add django_extensions to INSTALLED_APPS in settings.py - this is already done in the project. Please remember to remove it before deploying to production.
3. Run the server with command:
```
   python manage.py runserver_plus --cert-file cert.crt
```
In command runserver_plus we need to add the certificate file. Django Extensions will create the certificate file for us. If we want to use our own certificate file we need to add the path to the file.
4. Go to https://localhost:8000/ and accept the certificate
5. Those settings are not applied to production environment. As well as the django-extensions package.

### Setting up Redis database server
1. Install Redis:
   1. If you are Linux user you can download Redis from [here](https://redis.io/download)
   2. unpack archived file .tar.gz
   3. go to the unpacked directory and run:
   ```
   cd Redis-7.0.10
   make
   ```
   4. Run redis server with command:
   ```
   src/redis-server
   ```
2. If you are Windows user you can run Redis server in Windows Subsystem for Linux (WSL) or use Docker. For more information go to [Redis on Windows](https://redis.com/blog/redis-on-windows-10/) 
3. In case of issues, please verify the default redis settings in settings.py file. Line 99 - 101:
```
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
```
### Social app authentication
#### Facebook
1. Create an account on [Facebook for Developers](https://developers.facebook.com/apps)
2. Create an app.
3. Add Facebook Login product.
4. Add Valid OAuth Redirect URIs: http://together.com:8000/
5. Go to the app dashboard and copy the App ID and App Secret.
6. Add the App ID and App Secret to the .env file.
7. Go back to the facebook app click settings.
8. In the field App Domains add main-website.com
9. Be sure that the below fields are active:
    - Client OAuth Login
    - Web OAuth Login
    - Enforce HTTPS
    - Embedded Browser OAuth Login
10. In the field Valid OAuth Redirect URIs add http://together.com:8000/social-auth/complete/facebook/

#### Google
1. Create an account on [Google Cloud Platform](https://console.developers.google.com/apis/credentials)
2. Create a project.
3. Go to the OAuth consent screen and add the following:
    - Application name
    - Authorized domains: main-website.com
4. Go to the Credentials tab and click Create Credentials.
5. Choose OAuth client ID.
6. Choose Web application.
7. Add the following:
    - Name
    - Authorized redirect URIs: http://together.com:8000/social-auth/complete/google-oauth2/
8. Copy the Client ID and Client Secret.



## Features
- User registration
- User login
- User logout
- User profile
- Social app authentication (Google, Facebook)
- Image upload as a post
- Javascript bookmark for inserting images from other sites
- Follow/Unfollow users
- Like/Unlike images
- Counting likes and views

## Technologies
- Python 3.10.0
- Django 4.0.1
- JavaScript
- Redis database server

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgements
- [Django 3 By Example: Build powerful and reliable Python web applications from scratch, 3rd Edition](https://www.amazon.com/Django-Example-powerful-reliable-applications/dp/1838981950/ref=sr_1_1?keywords=django+3&qid=1695231491&sr=8-1)
- [Django Documentation](https://docs.djangoproject.com/en/4.0/)
- My wife for her patience and support while I was spending evenings and weekends on this project.
