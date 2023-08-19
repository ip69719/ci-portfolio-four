[Link to the live project](https://eleganza-hair-salon.herokuapp.com/)

# Eleganza Hair Salon

## Project Overview
This project was created for an imaginary hair salon website that allows customers to make, edit, and delete appointments.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/responsive_img.png)

### Project Goals
The main goal of this project is to allow users to manage their hair salon appointments online.

## User experience

### User Stories

All the user stories and their acceptance criteria are available [here](https://github.com/users/ip69719/projects/4/views/2?visibleFields=%5B%22Title%22%2C%22Labels%22%2C%22Milestone%22%5D&sortedBy%5Bdirection%5D=asc&sortedBy%5BcolumnId%5D=Milestone&filterQuery=title%3A).

#### Site Owner Stories
* As a Site Owner, I can display information about the salon so that site visitors understand the main purpose of the site.
* As a Business Owner, I want to move site visitors towards becoming customers of the salon so that I can grow my business.
* As a Business Owner, I want to increase awareness about the salon so that I can attract new customers.

#### Admin Stories
* As an Admin User, I want to be able to view all appointments so that I can organise appointments and staff rotas in advance.
* As an Admin User, I can add, modify or cancel appointments on Customers' behalf so that I can manage salon appointments efficiently.
* As an Admin User, I can add, modify or delete service categories so that I can ensure the website accurately reflects services available at the salon.

#### Site User Stories
* As a Site User, I can get key information about the salon from the landing page so that I can spend less time searching for information.
* As a Site User, I want to be able to easily navigate throughout the site so that I can view relevant content.
* As a Site User, I can create an account with username and password so that I can book appointments.
* As a Site User, I can login with username and password so that I can manage my booking requests.
* As a Site User, I can clearly see if I am logged in or not so that I can choose what action to take.
* As a Site User, I can securely logout so that my information is protected.
* As a Site User, I can send an enquiry to the salon by filling out the form so that I can receive additional information.
* As an Authenticated User, I can view my bookings so that I can check upcoming appointments.
* As an Authenticated User, I can book an appointment so that I can attend the salon.
* As an Authenticated User, I can edit my bookings so that I can make changes to my appointment if required.
* As an Authenticated User, I can cancel my bookings so that I can notify the salon if the appointment is no longer required.

### Agile methodology

The agile approach has been applied to develop this application. GitHub [projects board](https://github.com/users/ip69719/projects/4) was used to create user stories and manage the work.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/kanban_board.png)


### CRUD Functionality for users
* Create: A user can book a new appointment.
* Read: A user can view the details of an existing appointment.
* Update: A user can change the details of an existing appointment.
* Delete: A user can cancel an existing appointment.

### Database diagram

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/EDR.png)

### Design choices
I used [Bootstrap](https://getbootstrap.com/) CSS framework because it allows to design websites quickly and effectively.

#### Typography

* Meow Script font was used to create an attractive logo for the site.
* Montserrat was chosen as the main font because it is a versatile font that works well for web and mobile interfaces.

#### Images

* High quality images were selected to support the project goal. 

#### Colour Palette

* Colours were chosen to create a luxurious and elegant brand vibe. 

### Wireframes

The website has been designed with simplicity in mind. Each page contains only key information.

The wireframes were created at the start of the project. The final website differs slightly from the inital wireframes.

I decided that a single-column design is the best option for presenting the content on smaller devices such as mobile phones.

#### Homepage
![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/wireframes/eleganza_homepage.png)

#### Booking form
![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/wireframes/eleganza_booking_form.png)

#### User Profile page
![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/wireframes/eleganza_profile_page.png)

## Features

### All pages

#### Navigation bar
All pages have a **navigation bar** that was created using [Bootstrap](https://getbootstrap.com/) navbar component.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/navbar.png)

The **mobile collapse button** will appear on smaller screens; the **navigation bar** will show as a dropdown when the button is clicked.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/navbar_small.png)

#### Footer
The **footer** displays some of the salon's key information. It is split into three sections: Logo and links to social media, Salon Contact and Opening hours.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/footer.png)

### Home page

#### Hero image
A hero image is placed at the top of a website to create a strong visual impression. It incorporates both a high-quality image and text to represent the brand.

#### Call-to-action (CTA) buttons
The CTA button encourages visitors to book an appointment. When clicked, it brings users to the appointment booking page.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/hero.png)

#### Welcome message and interior image
The middle section of the homepage contains welcoming text highlighting industry awards. It also contains an image of the salon interior that sets the tone of the business.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/welcome.png)

### User Authentication
User authentication is handled by Django-Allauth module which has validations for username/password verification and email verification.

#### Sign up
* New users will have to sign up for a free account using the input form.
* Already registered users can click on the "sign in" link to get redirected to the **Login** page.
* Once signed up, a message will be displayed at the top of the site confirming that the user has successfully logged in.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/sign_up.png)

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/sign_up_msg.png)

#### Login
* The login page has an input form where the users will be required to enter their username and password.
* New users can click on the "sign up" link to get redirected to the **Sign Up** page.
* Once signed in, a message will be displayed at the top of the site confirming that the user has successfully logged in.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/sign_in.png)

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/sign_in_msg.png)

#### Logout
* Logged-in users can log out of the application by clicking on the **Logout** link on the navigation bar.
* Logged-in users will be asked to confirm if they want to log out.
* Once confirmed, a message will be displayed at the top of the site confirming that the user has successfully logged out.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/sign_out.png)

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/sign_out_msg.png)

### Appointment booking form

The appointment booking form is accessible to authenticated users only. If a user clicks on the CTA button but he/she is not signed in, then a message is displayed requesting the user to log in or sign up.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/booking_unavailable.png)

The authenticated user will be presented with a form to fill out once the “Book now” button is clicked. Choosing the date from a calendar and selecting a time slot from a predefined list is made easy with interactive dropdowns.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/form_1.png)
![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/form_2.png)
![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/form_3.png)

If the user inputs to the form are valid, then an appointment record will be saved. A message will be displayed at the top of the site confirming that an appointment has been successfully created. The user will be redirected to the **Appointments** page.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/booking_history_1.png)


#### Booking form validations
User inputs are validated using both built-in and custom built validations. Errors are displayed on the form if conditions are not met.

* **First name** must be at least two characters long
* **Last name** must be at least two characters long
* **Phone** must be at least eight characters long and must contain digits only
* **Email** address must have the following pattern: username + @ symbol + domain name

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/form_validation_1.png)
![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/form_validation_2.png)

#### Avoid double bookings

The same user cannot book an appointment for the same date and time slot. An error message is displayed at the top of the form if a conflict exists.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/form_validation_3.png)

### Appointments

Authenticated users are able to access the **Appointments** page where they can view their appointment history and manage their bookings. If the user has made bookings, then the details of each booking will be shown here along with two buttons.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/booking_history_2.png)

Authenticated users have the ability to update their existing bookings by clicking the "Edit" button. Once the "Edit" button is clicked, the booking form will be displayed. The form will be prefilled with details of the existing appointment.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/edit_booking.png)

If inputs meet the required conditions, then the updated appointment details will be saved when the user clicks the “Update” button. A message will be displayed at the top of the site confirming that the appointment has been successfully updated. Then, the user will be redirected to the Appointments page.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/edit_confirm_msg.png)

If the user inputs are invalid, the validation errors are displayed on the form.

If the user chooses “Cancel” then the appointment will be deleted from the model. A success message is displayed confirming that the appointment has been cancelled. Then, the user is redirected back to the Appointments page.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/cancel_booking.png)

### Admin panel

The admin can access the admin panel by logging in with the superuser details. The admin will be able to get an overview of all the appointments and alter any of the information.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/admin.png)

### Error 404 - Page Not Found Error

Users are redirected to a custom error 404 Page Not Found page if the URL is mistyped or does not exist.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/404.png)

### Error 500 - Internal Server Error

If the server encounters an unexpected condition that prevents it from fulfilling the request, then a custom Error 500 - Internal Server Error template is displayed.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/features/500.png)

## Technologies used

### Languages used

* [HTML5](https://en.wikipedia.org/wiki/HTML5) used to create the structure of the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) used to style the website
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) used to created logic of the website.

### Frameworks, Libraries & Programs Used

* [Bootstrap v 4.6](https://getbootstrap.com/) CSS framework was used for creating responsive design.
* [Cloudinary](https://cloudinary.com/) is used to store all static files and images.
* [Django](https://www.djangoproject.com/) web framework was used to create the application.
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html) used for styling of all forms.
* [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/) used to implement registration and authentication functionality.
* [Font Awesome](https://fontawesome.com/) was used to obtain icons for the website.
* [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) is used to store the projects code after being pushed from Git.
* [Google fonts](https://fonts.google.com/) were used to import the 'Meow Script' and 'Montserrat' fonts into the style.css file.
* [Google Developer Tools](https://developer.chrome.com/docs/devtools/) was used for testing responsiveness of the website.
* [Lucid](https://lucid.app/users/login#/login) was used to create the ERD for the project.
* [TinyPNG](https://tinypng.com/) was used to optimise images for the web.

## Testing

### Validation Testing

* The W3C Markup Validator, W3C CSS Validator Services and CI Python Linter were used to validate the project to ensure there were no syntax errors.

    * W3C Markup Validator [Results](https://github.com/ip69719/ci-portfolio-four/tree/main/django_eleganza/assets/documents/testing/w3c_css_validator_results) - no errors found
    * W3C CSS Validator [Results](https://github.com/ip69719/ci-portfolio-four/tree/main/django_eleganza/assets/documents/testing/w3c_markup_validator_results) - errors and warnings relate to Django template language and were ignored
    * CI Python Linter [Results](https://github.com/ip69719/ci-portfolio-four/tree/main/django_eleganza/assets/documents/testing/ci_python_linter) - no errors found

### Manual Testing

* Test cases are recorded in [this](https://docs.google.com/spreadsheets/d/1Sf8cfgagafrIxZF-q7NSt93RERGrl5QQf0XmTCEtAnM/edit#gid=0) shared google workbook.

### Defect Tracking

* Issues are documented and tracked on [GitHub](https://github.com/ip69719/ci-portfolio-four/issues?q=is%3Aopen+is%3Aissue+label%3Abug).
* I used 'Bug' as a label to distinguish defects from user stories.

## Deployment

The project was deployed to Heroku using the following steps:

**Create Heroku app**
* Log in to [Heroku](https://id.heroku.com/login) and go to the Dashboard.
* Click "New" in the top right corner and select "Create a new app".
* Give the app a name and select the closest region, then click "Create app".

**Create a database**
* Log in to [ElephantSQL.com](https://www.elephantsql.com/).
* Click "Create New Instance".
* Name the "plan" and select the "Tiny Turtle (free)" plan.
* Select "Select Region".
* Select the nearest data center, then click "Review".
* Check the details are correct and then click "Create instance".
* Return to the ElephantSQL dashboard and click on the database instance name for this project.
* In the URL section, click the copy icon to copy the database URL.

**Configure Environment Variables in Heroku**
* Return to the Heroku dashboard open the Settings tab.
* Go to "Settings" tab and scroll down to the “Config Vars” section.
* Click on "Reveal Config Vars".
    * In the field for key, enter DATABASE_URL.
    * Copy and paste database URL from ElephantSQL into the value field, then click “Add”.
    * Configure variable for key PORT and value 8000, then click “Add”.
    * Configure variable for key SECRET_KEY by setting the value to your chosen key, then click “Add”.
    * Configure variable for key CLOUDINARY_URL:
        * Log in to [Cloudinary](https://cloudinary.com/)
        * Click on the copy icon next to API Environment variable.
        * Paste Cloudinary URL into the value field for CLOUDINARY_URL key in Heroku, then click “Add”. Note that *"CLOUDINARY_URL ="* needs to be removed from the beginning of the value copied above.

**Heroku deployment**
* Go to "Deploy" tab and scroll to the “Deployment method” section.
* Click on "GitHub".
* Locate the [GitHub Repository](https://github.com/ip69719/ci-portfolio-four) then click "Connect".
* In "Deploy" tab scroll down to "Manual deploy" section, select main branch and click on "Deploy Branch".
* Click "View" to launch the app. 
* [Link to the live project](https://eleganza-hair-salon.herokuapp.com/)


## Credits

### Media

* Images were sourced from [Shutterstock](https://www.shutterstock.com/home).

### Code

* Used Code Institute Hello Django and  I Think Therefore I Blog Project tutorials as a reference to implement project idea
* Learned how to align Bootstrap navbar items from [this](https://stackoverflow.com/questions/41513463/bootstrap-align-navbar-items-to-the-right) Stack Overflow post.
* Adopted code for footer section from [this](https://mdbootstrap.com/snippets/standard/mdbootstrap/2885120?view=side) footer design by MDBootstrap.
* Learned how to vertically align items using Bootstrap from [this](https://stackoverflow.com/questions/42252443/vertical-align-center-in-bootstrap-4) Stack Overflow post.
* Learned how to change order of flex items with Bootstrap from [this](https://stackoverflow.com/questions/51115456/bootstrap-4-ordering-class) Stack Overflow post.
* Learned how to hide elements with Bootstrap from [this](https://stackoverflow.com/questions/57039195/how-to-hide-element-for-mobile-device-with-bootstrap4) Stack Overflow post.
* Learned how to use Django Form Fields, Widgets and Attributes from [this](https://ordinarycoders.com/blog/article/using-django-form-fields-and-widgets) Ordinary Coders
blog written by Jaysha.
* Learned how to create custom 404 and 500 error pages in Django from [this](https://pythoncircle.com/post/40/designing-custom-404-and-500-error-pages-in-django/) Python Circle blog and [this](https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page) Stack Overflow post.
* [Article](https://www.brennantymrak.com/articles/django-custom-form-validation) written by Brennan Tymrak and GeeksforGeeks [Form validation using django](https://www.geeksforgeeks.org/python-form-validation-using-django/) tutorial were referenced when creating custom form validations.

### Acknowledgements

* Special thanks to my Mentor [Malia Havlicek](https://github.com/maliahavlicek) for support and guidance during this project.