# The Brewtique

The Brewtique is a one-stop online coffee shop, stocking a wide variety of coffee and brewing equipment. The Brewtique caters to all sorts of coffee drinkers, from casual enjoyers to expert brewers.

## Features

### Models

* Product
    * These are the items to be sold. They have a lot of information saved to each instance.
* Category
    * Two main categories: Coffee (Beans&Grounds), and Equipment (Brew-ware)
* Profile
    * Users can create a profile on the site, where they can store their information like delivery address, email, and past orders 
* Wishlist
    * Users can add, remove, and view products on their wishlist, which is linked to their profile.
* Newsletter
    * Users can sign up for an email newsletter, in which they will learn about product / site updates and special offers

## Deployment

Follow the steps outlined below to deploy:

#### Creating a database

* Sign in to your account at [PostgresSQL from Code Institute](https://dbs.ci-dbs.net/)

* Follow to onscreen instructions to create the DB and access the link

* Save this link (Keep it secret!)

#### Creating a Heroku App

* Login to your [Heroku Dashboard](https://dashboard.heroku.com/apps)

* Create a new app, give it a name, select the region closest to you, and click "Create"

* Navigate to settings, show config vars, and add 'DATABASE_URL' and your recently created PostgreSQL database url as a config var

* In your env.py file, add the DATABASE_URL: ```os.environ['DATABASE_URL'] = 'YOUR DATABASE URL HERE'```

* In your Django project settings.py, comment out the default sqlite DB settings, and paste in the below:
```"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))```

* Migrate your models to your new database with the following in the terminal: ```python3 manage.py migrate```

* Create a superuser on your new DB: ```python3 manage.py createsuperuser```

* Add your Django ```SECRET_KEY``` to your env.py file. New secret keys can be generated at [Djecrety](djecrety.ir):
```os.environ.setdefault('SECRET_KEY', 'Your secret key here')```

* Configure your settings to access the key from the environment: ```SECRET_KEY = os.environ.get('SECRET_KEY')```

* Create a Procfile in the project root directory. Name it ```Procfile``` (no extension)

* Insert the below into your procfile (you'll need gunicorn installed):
```web: gunicorn brewtique.wsgi:application``` -> assuming your main django project folder is called "brewtique"

* Add your Heroku app hostname (something like ```brewtique-resubmission-914b75bb89ab.herokuapp.com```) to your ```ALLOWED_HOSTS``` list in settings.py

* Install WhiteNoise ```pip install whitenoise``` to manage the serving of static files.

* Add the WhiteNoise middleware to your settings.py. [WhiteNoise docs](https://whitenoise.readthedocs.io/en/stable/django.html)

* Add ```SECRET_KEY``` , ```YOUR GENERATED SECRET KEY``` to your Heroku config vars (not the same as the one in env.py!)

* In the Heroku 'Deploy' tab, navigate to 'Deployment Method', select GitHub, and search for your Github repository

* Make sure you select the correct branch!

* Click 'Enable Automatic Deploys', then click 'Deploy Branch'
## Testing and Validation

### Thanks

* [Coffee.ie](https://coffee.ie/) - for the products and descriptions used in the store
