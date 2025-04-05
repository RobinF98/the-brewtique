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

## Manual Testing

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Navigation | Click 'View Store' or 'Home' | Redirects to product page | Works as expected |
| Navigation | Click 'Category' dropdown and select a category | Redirects to products page with applied filters | Works as expected |
| Navigation | Type in Search bar and click search / press enter | Redirects to product page with search query applied | Works as expected |
| Navigation | Click on 'Sort' dropdown and select a sort order | Redirects to product page with applied filters / search query, in specified sort order | Works as expected |
| Navigation - Login | Click 'My Account' dropdown and select 'Login' | Redirected to Login page | Works as expected |
| Navigation - User loggeed in | Click 'Wishlist' in 'My Account' dropdown | Redirected to Wishlist page | Works as expected |
| Navigation - SuperUser loggeed in | Click 'Product Management' in 'My Account' dropdown | Redirected to Add Product page | Works as expected |
| Navigation - User loggeed in | Click Newsletter in Navbar | Redirected to Newsletter signup page | Works as expected |
| Login page | Enter correct credentials and click Sign In | User is logged in and redirected to home page | Works as expected |
| Login page | Enter incorrect credentials | Wrong password/username error appears | Works as expected |
| Sign in page | Click Sign Up | Redirected to Sign Up page | Works as expected |
| Sign Up page | Username, password 1, and password 2 entered according to requirements | New User is created, logged in, and redirected to home page | Works as expected |
| Sign Up page | Passwords not entered identically / fewer than 8 characters | Password mismatch / too short error(s) appear | Works as expected |
| Sign Up page | Username entered with invalid characters | Invalid username error appears | Works as expected |
| Product Page | Click on a product name | Redirected to product detail page for that product | Works as expected |
| Product detail | Click 'Add to cart' | Selected qty of product is added to cart. Cart preview amount is updated | Works as expected |
| Product detail | Click 'Add to Wishlist' | Product is added to wishlist. Page reloaded. 'Add to Wishlist' is replaced by 'Remove from Wishlist' | Works as expected |
| Prodict detail | Click 'Remove from wishlist' | Product is removed from wishlist. Page reloaded. 'Remove from wishlist' is replaced by 'Add to Wishlist' | Works as expected |
| Product detail - superuser | Click 'Edit' or 'Delete' | Redirected to Update Product view, or product is deleted, respectively | Works as expected |
| Cart | Change line item qty and click update | Page reloaded with new qty and subtotal for line item amended | Works as expected |
| Checkout | Fill in form and credit card info correctly - click 'Complete Order' | Redirected to Checkout success page. Order is sent through to Stripe and payment goes through | Works as expected |
| Checkout | Click 'Complete Order' with 'Save delivery info' checkbox checked  | Delivery info for the user is saved and applied to future orders | Works as expected |
| Wishlist | Click on product name | Redirected to product detail page for that product | Works as expected |
| Wishlist | Click on bin icon next to product name | Product is removed from the wishlist | Works as expected |
| Newsletter | Add name and email to form, click submit button  | Name and email address is added as a Newsletter instance. Redirected to Newsletter success page | Works as expected |
| Newsletter | User is signed in. Name and email is saved to User Profile | Form is prepopulated with name and email | Works as expected |
| Product Update | Amend product details, click submit button | Product is saved. Redirected to product detail page | Works as expected |
| Product Update | Amend product details, but include incorrect data / leave out required field, click submit | Validation error raised on form fields in question. Product not saved | Works as expected |
| Add product | Fill in form, click submit | Product added. Redirected to product detail page for the new product | Works as expected |
| Responsiveness - Navbar | - | Navbar changes to hideable sidebar on smaller screens | Works as expected |
| Responsiveness - full site | - | Site resizes to fit smaller screens in legible and pleasing manner | Works as expected |

## SEO
## Facebook page
### Thanks

* [Coffee.ie](https://coffee.ie/) - for the products and descriptions used in the store
