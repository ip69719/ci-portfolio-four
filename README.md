[Link to the live project](https://eleganza-hair-salon.herokuapp.com/)

# Eleganza Hair Salon

## Project Overview
This project was created for an imaginary hair salon website designed to allow customers to make, edit and delete appointments.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/images/responsive_img.png)

### Project Goals
The main goal of this project is to allow users to manage their hair salon appointments online.

## User experience

### User Stories

All user stories and their acceptance criteria are availabe [here](https://github.com/users/ip69719/projects/4/views/2?visibleFields=%5B%22Title%22%2C%22Labels%22%2C%22Milestone%22%5D&sortedBy%5Bdirection%5D=asc&sortedBy%5BcolumnId%5D=Milestone&filterQuery=title%3A)

* Site Owner Stories
    * As a Site Owner, I can display information about the salon so that site visitors understand the main purpose of the site.
    * As a Business Owner, I want to move site visitors towards becoming customers of the salon so that I can grow my business.
    * As a As a Business Owner, I want to increase awareness about the salon so that I can attract new customers.

* Admin Stories
    * As an Admin User, I want to be able to view all appointments so that so that I can organise appointments and staff rotas in advance.
    * As an Admin User, I can add, modify or cancel appointments on Customers' behalf so that I can manage salon appointments efficiently.
    * As an Admin User, I can add, modify or delete service categories so that I can ensure the website accurately reflects services available at the salon.

* User Stories
    * As a Site User, I can get key information about the salon from the landing page so that I can spend less time searching for information.
    * As a Site User, I want to be able to easily navigate throughout the site so that I can view relevant content.
    * As a User, I can create an account with username and password so that I can book appointments.
    * As a Site User, I can login with username and password so that I can manage my booking requests.
    * As a Site User, I can clearly see if I am logged in or not so that I can choose what action to take.
    * As a Site User, I can securely logout so that my information is protected.
    * As a Site User, I can send an enquiry to the salon by filling out the form so that I can receive additional information.
    * As an Authenticated User, I can view my bookings so that I can check upcoming appointments.
    * As an Authenticated User, I can book an appointment so that I can attend the salon.
    * As an Authenticated User, I can edit my bookings so that I can make changes to my appointment if required.
    * As an Authenticated User, I can cancel my bookings so that I can notify the salon if the appointment is no longer required.

### Agile methodology

Agile approach has been applied to develop this application. GitHub [projects board](https://github.com/users/ip69719/projects/4) was used to create user stories and manage the work.

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/kanban_board.png)

### Database diagram

![](https://github.com/ip69719/ci-portfolio-four/blob/main/django_eleganza/assets/documents/EDR.png)

#### Typography

* Meow Script font was used to create an attractive logo for the site.
* Montserrat was chosen as the main font because it is a versatile font that works well for web and mobile interfaces.

#### Images

* High quality images were selected to support the project goal. 

#### Colour Palette

* Colours were chosen to create a luxurious and elegant brand vibe. 

### Wireframes

## Features

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

### Acknowledgements

* Special thanks to my Mentor [Malia Havlicek](https://github.com/maliahavlicek) for support and guidance during this project.