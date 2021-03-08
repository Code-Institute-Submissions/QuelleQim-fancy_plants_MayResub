# Fancy plants
Welcome to the README file of the project Fancy Plants.

This is the fourth and final school project of the Code Institute 
fulsstack developer course. This projects main purpose is to display my
skills in HTML, CSS, Bootstrap, Python and Django. The webpage named
Fancy Plants is a online store that aims to sell plants, plant related
products and plant subscriptions.

Direct link to active website:

https://fancy-plants.herokuapp.com/


## UX/UI

### User Stories (UX)

### Owner Stories (UX)

### Wireframes (UI)

- index/home page
![index/home](/media/wireframes/index.jpg)

- All products view
![All Products](/media/wireframes/all-products.jpg)

- Product details view
![Products Details](/media/wireframes/product-details.jpg)

- Shopping bag view
![Shopping Bag](/media/wireframes/shopping-info.jpg)

- Checkout view
![Checkout](/media/wireframes/checkout.jpg)

- Successfull checkout view
![Checkout Success](/media/wireframes/checkout-success.jpg)

- Plant care view
![Plant Care](/media/wireframes/plant-care.jpg)

- Plant Care Elements. Consists of four diffrent html views.
![Plant Care Elements](/media/wireframes/plant-care-elements.jpg)

- My profile view
![My Profile](/media/wireframes/my-profile.jpg)

- My subscription view
![My Subscriptions](/media/wireframes/my-subscription.jpg)

- Admin product management view
![Product Management/Add/Edit](/media/wireframes/product-management-admin.jpg)

- Register, Login and dropdown navbar in mobile view
![Register/Login/dropdown navbar](/media/wireframes/sign-up-sign-in-nav.jpg)


## Features
In this section the features of the different parts of this project will be described.

### Existing Features

-	Feature 1 – base.html – base template that extends to all other html files. The base template contains meta, CSS, JavaScript and stripe tags, A navbar containing company name, search field and bag. If user is not logged in then it also views log in and register. If user is logged in it says my account, my subscriptions and lo out. If admin is logged in the product management will be visible. Not visible in the view but present in code is also message block content and a toast post load JavaScript tag. At the end a footer that contains company placeholder information, company open hours and social links (Facebook, Instagram and youtube). The footer is visible on all medium and up sized screens. Footer is not included on the mobile view.
-	Feature 2 – index.html – background image of plants, a text box with company motto and a button that states “Shop Now” that redirects to all products.
-	Feature 3 – navbar 1 – on medium sized screens and up: company name, search field, my account button and bag button.  On mobile view the company name is not displayed.
-	Feature 4 – navbar 2 – navbar located beneath navbar number 1. On medium sized screens and up: all products, subscriptions, plants & more, special offers, plants care buttons. On mobile view: the navbar is collapsed and firstly only visible via a hamburger icon. When pressed it reveals home, all products, subscriptions, plants & more, special offers, and plant care buttons.
-	Feature 5 – all products – a view that displays all products in a grid view and divides rows with a thematic break.
-	Feature 6 – products sorted by category – buttons: subscriptions, plants, pots, tools, accessories, new arrivals and clearance all show products after category. For example, when pressing the pots button, the view will show all products available in the pots category.
-	Feature 7 – plantcare.html – shows four images with four different headings, all of these are links to a different html pages with said heading info.
-	Feature 8 – plantcare.html – plant care elements – text containers with information about plant care in four different themes. 
-	Feature 9 – search field – searches for product name and renders hits in view with grid layout.
-	Feature 10 – profile.html – my profile – Default delivery information:  7 input field column form and button that when clicked updates the user information to the database. Order history: shows previous orders with order number, date and order total.  
-	Feature 11 – subscriptions.html – my subscriptions – to be implemented, contains currently heading subscription options and my subscriptions.
-	Feature 12 – products/add.html – product management – view for admin only. Contains a form with 7 input fields in columns:  category, sku, name, description, price, rating and image url with select image button that downloads image. Two buttons at bottom: cancel and add product, which either redirects the user back or saves the product in database.
-	Feature 13 – products/edit.html – same view as feature 12 but with a products previous information saved and editable.
-	Feature 14 – bag.html – shopping bag – if empty, shows text “Your bag is empty” and button “keep shopping” that redirects back to products.html. If not empty, products render beneath each other with information headings: product info, price, qty, subtotal, product name, sku, bag total and delivery cost. Underneath top headings are buttons for update, remove, increment and decrement. Update button save a new quantity of product and remove button removes product from bag. 
-	Feature 15 – checkout.html – checkout – form with 9 input fields columns: full name, email, phone number, street address 1, street address 2 (optional), town or city, county (optional), post code and country. Beneath the form is a checkbox, when checked the form information will be saved to the user profile. Beneath checkbox: payment input field for card number, month, year, CVC and post code for payment which is connected to stripe. Beneath checkbox: two buttons, “adjust bag” redirects back to bag.html, “complete order” initializes a payment. Order summary heading is followed by bags product content and order info. When complete order button is clicked a animation of a spinning arrow is initialized.
-	Feature 16 – checkout_success.html – successful checkout – heading stating “Thank you”, confirmation of email sent to input email. Order info in column, same as in feature 15. Success message with confirmations number and stating confirmation has been sent to inputs email. At bottom button “now check out the latest deals” redirects to products.html.
-	Feature 17 – admin.html - admin Django view – shows 11 functions in which the content of these can be added or edited.
-	Feature 18 – admin/emailaddress.html – email addresses – lets admin add, verify, select email to primary and delete. 
-	Feature 19 - admin/group.html – standard Django admin function which is not used in this project.
-	Feature 20 - admin/user.html – users – allows admin to add, edit, give permissions (active, staff status, superuser status), check important dates and delete users.
-	Feature 21 - admin/order.html – orders – allows admin to create, edit, delete and view information about orders.
-	Feature 22 - admin/category.html – categories – allows admin to view, edit and remove a category.
-	Feature 23 - admin/product.html – products – allows admin to view, edit and delete a product.
-	Feature 24 - admin/site -sites - standard Django admin function which is not used in this project.
-	Feature 25 - admin/socialaccount – social account - standard Django admin function which is not used in this project.
-	Feature 26 - admin/socialapplicationtoken.html – social application tokens - standard Django admin function which is not used in this project.
-	Feature 27 - admin/socialapplication.html – social applications - standard Django admin function which is not used in this project.
-	Feature 26 - admin/subscription.html – subscriptions – allows admin to add, edit, view and delete a subscription.


### Features left to implement
- Feature 11 as mentioned above ought to give user more control over their subscriptions. With checkboxes stating diffrent options for the subscription boxes and save button so that the user can easily and quickly edit their subscription if their plant enviroment changes.
- Feature 11 also should show previously bought subscription boxes and the content of said box.
- To increace the amount a customer returns to the website there should be a newsletter optio, which will inform and give discount to subscribed customers.

## Technologies Used


### Database

- Amazon web services - The project uses amazon to store media and static files.

### Languages

- HTML - The project uses HTML to create visable content.
- CSS - The project uses CSS to style the HTML code.
- Python - The project uses python togheter with the database and Django.
- JavaScript - The project uses JavaScript for functions that were more easily applied that with using Python.

### Framework

- Django - The project uses Django to enable rapid development for a secure and maintanable website.
- Bootstrap - The project uses materialize to simplify the customization of the HTML and CSS code.

### Library

- Google fonts - The project uses google fonts libary to customize text.
- Font awesome - The project uses font awesome to customize the webpage with custom icons.

### Hosting platform

- Heroku - The project uses heroku as cloud hosting platform.

### Other Technologies

- Stripe - The project uses heroku as a method for payment.

## Testing

### Manual Testing

The manual testing is executed with the following method:

Page > action taken > expected result > pass/fail

1. index.html > press 'shop now' button > redirects products.html > pass
2. index.html > press 'all products' button > redirects products.html > pass
3. index.html > press 'subscriptions' button > redirects products-category-subscription_box.html > pass
4. index.html > press 'plants & more' button > opens dropdown menu with five buttons > pass
5. index.html > press buttons individually in 'plants & more' drop down menu > redirect to correct page > pass
6. index.html > press 'special offers' button > opens dropdown menu with three buttons > pass
7. index.html > press buttons individually in 'plants & more' drop down menu > redirect to correct page > pass
8. index.html > press 'plant care' button > redirect to plantcare.html > pass
9. plantcare.html > press all four individual plant care element buttons > redirect to plantcare/water.html, plantcare/sun.html, plantcare/earth.html, plantcare/air.html> pass
10. index.html > press my 'account' button > if not logged in, show buttons 'register' and 'login' > pass
11. index.html > press my 'account' button > if user is logged in, show buttons 'my profile', 'my subscriptions' and 'logout' > pass
12. index.html > press my 'account' button > if superuser is logged in, show buttons 'product management', 'my profile', 'my subscriptions' and 'logout' > pass
13. index.html > press 'bag' button > if no products added, redirect to bag.html and show empty bag > pass
14. index.html > press 'bag' button > if products added, redirect to bag.html and show bag with products inside > pass
15. bag.html > press 'secure checkout' button >  redirect to checkout.html > pass
16. bag.html > fill out form and press 'complete order' button > redirect animated loading image and then to checkout_success.html > pass
17. profile.html > change form info and press 'update information' button > new info saved and rendered in profile.html and success message displayed > pass
18. products/add.html > fill out form correctly and press 'add product' > item saved in products, success message rendered and redirected to product in product details view > pass
19. products/add.html > fill out form incorrectly and press 'add product' > page refuses 'add product' button functionality and demand correct input > pass
20. products/item.html > press 'delete' button > delete product, render success message and redirect to products.html > pass
21. accounts/signup.html > fill out form correctly and press 'sign up' button > user is saved in database and alert message shown and redirected to confirm-email.html > pass 
22. accounts/signup.html > fill out form incorrectly and press 'sign up' button > page refuses 'sign up' button functionality and demands correct information > pass
23. accounts/login.html > fill out form correctly and press 'sign in' button > user is checked in database and in existing, log in correct user > pass
24. accounts/login.html > fill out form incorrectly and press 'sign in' button > page refuses 'sign in' button functionality and demands correct information > pass


### Webpage Images


![index/home](/media/webpage-images/index-home.jpg)

![all products](/media/webpage-images/all-products.jpg)

![product detail](/media/webpage-images/product-details.jpg)

![shopping bag empty](/media/webpage-images/shopping-bag-empty.jpg)

![shopping bag success increment](/media/webpage-images/shopping-bag-success-increment.jpg)

![checkout](/media/webpage-images/checkout.jpg)

![checkout-loading](/media/webpage-images/checkout-loading.jpg)

![checkout-success](/media/webpage-images/checkout-success.jpg)

![plant care](/media/webpage-images/plant-care.jpg)

![plant care elements](/media/webpage-images/plant-care-element.jpg)

![my profile](/media/webpage-images/my-profile.jpg)

![my-subscriptions](/media/webpage-images/my-subscriptions.jpg)

![product management add](/media/webpage-images/product-management-add.jpg)

![product management edit](/media/webpage-images/product-management-edit.jpg)

![register](/media/webpage-images/register.jpg)

![login](/media/webpage-images/login.jpg)



### W3C Validator

- The online project was tested in W3C validator and recived 7 errors and 2 warnings. The test was conducted 8/3-2021, 21:00. 
[Validator.w3.org](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffancy-plants.herokuapp.com%2F)


### Automated Testing

### Bugs Fixed



### Known Issues




## Deployment

The project has been deployed from [github](https://github.com) to [heroku](https://heroku.com).

How the project is deployed: 
Accessed heroku webpage, navigate to settings. In 'Config Vars' all relevant variables connectable
to github, amazon and stripe had been entered.  See table: 

Enviroment variables | Example description
------------ | -------------
AWS_ACCESS_KEY_ID | amazon web services id key
AWS_SECRET_ACCESS_KEY | amazon web service secret access key
DATABASE_URL | key for database url
EMAIL_HOST_PASS | key for Django email hosting
EMAIL_HOST_USER | key for setting email host account
SECRET_KEY | secret key to access Django
STRIPE_PUBLIC_KEY | stripe public key
STRIPE_SECRET_KEY | stripe secret key
STRIPE_WH_SECRET | stripe secret webhook key
USE_AWS | key for amazon web service usage


After input of enviroment variables, navigate to 'deploy'. In 'deployment method' github was selected. 
A couple of minutes of heroku builing the app later states: 'Build succeeded' and ' Deployed', meaning
the project was uploaded to heroku and responsive. 'App connected to GitHub' states that the project
is connected to the correct github user and states that it is deployed from master branch.
'Automatic deploys' are enabled, when a push is made in gitpod then heroku will deploy directly after.

Since the version on heroku is rooted from the github repository's master branch there is no
difference between the deployed version on heroku and the github repository, except for a minor
delay of a few minutes. To run the project localy one needs to clone the github repository
and run code 'python3 manage.py runserver' from terminal.


## Credits

### Content

- Code about how to format date in subscription/admin.py comes from [programiz](https://www.programiz.com/python-programming/datetime/strftime).

- Code about how to add readonly_fields with ModelAdmin in subscription/admin.py comes from [jnns via stackoverflow](https://stackoverflow.com/questions/44718355/how-show-related-object-in-django-admin-from-the-model-with-a-foreign-key-point#44725212).

- Code about how to change custom color of navbar in base.css comes from[Zim via stackoverflow](https://stackoverflow.com/questions/42586729/bootstrap-4-change-hamburger-toggler-color).

- Code for linear gradients in base.css comes from [w3schools.com](https://www.w3schools.com/css/css3_gradients.asp).

- Code for checkboxes in subscription.html comes from [bootstrap](https://getbootstrap.com/docs/5.0/forms/checks-radios/).


### Media

#### Images

- Webpage background image made by Mitchel Lensink and retrived from [unsplash](https://unsplash.com/photos/DFIl2Kw6ulw).

- Water image by Wesley Tingey, image retrived via [unsplashed](https://unsplash.com/photos/9-OCsKoyQlk).

- Sun image by Ivan Torres, image retrived via [unsplashed](https://unsplash.com/photos/AXz346Rhs6A).

- Earth image by Gabriel Jimenez, image retrived via [unsplashed](https://unsplash.com/photos/jin4W1HqgL4).

- Cloud image by Billy Huynh, image retrived via [unsplashed](https://unsplash.com/photos/v9bnfMCyKbg).

##### Subscriptions boxes Category
- Image of beginner box made by Peter Žagar and retrived from [unsplash](https://unsplash.com/photos/bLgWa9b0ioY).

- Image of medium box made by Prudence Earl and retrived from [unsplash](https://unsplash.com/photos/NwBx723XaHw).

- Image of plant Master Box made by Katya Austin and retrived from [unsplash](https://unsplash.com/photos/4Vg6ez9jaec).

##### Plants Category
- Image of zz plant made by Uljana Maljutina and retrived from [unsplash](https://unsplash.com/photos/7QyOFJoungI).

- Image of fiddle-leaf fig tree made by Lauren Mancke and retrived from [unsplash](https://unsplash.com/photos/DpphPG9ENsI).

- Image of string of hearts made by Severin Candrian and retrived from [unsplash](https://unsplash.com/photos/xGpYDi-0348).

##### Pots Category
- Image of small green glazed pot made by Brina Blum and retrived from [unsplash](https://unsplash.com/photos/2RyuA0imp5k).

- Image of small light blue ceramic pot made by Galina N and retrived from [unsplash](https://unsplash.com/photos/miziNqvJx5M).

- Image of big terra cotta pot and saucer made by Brina Blum and retrived from [unsplash](https://unsplash.com/photos/ArCgAeF5_Wk).

##### Tools Category
- Image of metallic watering can made by Emily Underworld and retrived from [unsplash](https://unsplash.com/photos/AmI0d5QoaEg).

- Image of wood handle trowel made by gryffyn m and retrived from [unsplash](https://unsplash.com/photos/JR7IPWMMXcc)

- Image of pruning shears made by lilzidesigns and retrived from [unsplash](https://unsplash.com/photos/RjTJBhtjHSY)

##### Accessories Category
- Image of fancy potting soil made by Neslihan Gunaydin and retrived from [unsplash](https://unsplash.com/photos/BduDcrySLKM).

- Image of glass terrarium with grow light made by David Emrich and retrived from [unsplash](https://unsplash.com/photos/Xlzx6sEoenQ).

- Image of fancy fertilizer dropper 50 ml made by Kadarius Seegars and retrived from [unsplash](https://unsplash.com/photos/CjP0nkn6O88).

##### Clearance Category
- Image of small parlor palm made by Kara Eads and retrived from [unsplash](https://unsplash.com/photos/olvdBsHT1bA).

- Image of medium glass bowl made by Scott Webb and retrived from [unsplash](https://unsplash.com/photos/6zDgwG-2520).

- Image of happy mini pot made by Faria Anzum and retrived from [unsplash](https://unsplash.com/photos/ONK9IlKizS4).

##### New Arraivals Category
- Image of lace aloe made by Stephanie Harvey and retrived from [unsplash](https://unsplash.com/photos/T0inbt7nRME).

- Image of small glass vase made by Tirza van Dijk and retrived from [unsplash](https://unsplash.com/photos/cNGUw-CEsp0).

- Image of hanging wooden shelf made by Severin Candrian and retrived from [unsplash](https://unsplash.com/photos/edRZ0zEBq4I).


### Acknowledgements 
This project recived visual and structual inspiration from these webpages:

- [Grönväxtriket](https://gronvaxtriket.se/)
- [The Sill](https://www.thesill.com/)
- [Plantrédo](https://www.plantredo.com/)
- [Plantagen](https://www.plantagen.se/)
- [Blomsterlandet](https://www.blomsterlandet.se/vaxter/)