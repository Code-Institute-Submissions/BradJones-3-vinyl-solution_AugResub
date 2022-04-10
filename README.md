# Vinyl Solution
# Table of Contents
1. [Introduction](#Introduction)
2. [UX](#UX)
   *  [User Stories](#User-Stories)
   *  [Development Planes](#Development-Planes)
3. [Features](#Features)
   * [Existing Features](#Existing-Features)
   * [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
6. [Testing](#Testing)
   * [Testing.md](TESTING.md)
7. [Deployment](#Deployment)
8. [Credits](#Credits)
   * [Content](#Content)
9. [Acknowledgements](#Acknowledgements)

# Introduction

# UX

## When using this website, please note that the Stripe functionality is set up to be in a test mode. DO NOT ENTER your personal card number when checking out an order. Please use these test numbers instead:

    - card number: 4242 4242 4242 4242 
    - date: 04 24
    - CVV: 424

## User Stories

**User Goals**
  * I want to have a rough idea of what this website is when i first land on the homepage.
  * I want to be able to easily navigate around the website.
  * I want to be able to register an account.
  * I want to be able to see more information about the products.

**How This Will Be Achieved**
  * A brief description when landing on the hompage.
  * A simple navigation bar located at the top of the page.
  * Using the navigation bar to 'Sign Up'.
  * Clicking on the product will show a description of that product.

## Development Planes

## Skeleton

The developer used [Balsamiq](https://balsamiq.com/wireframes/ "Balsamiq Homepage") to create the wireframes for the website.

### Wireframe Images
[Wireframe images](wireframes.md)

### Colour Scheme

### Typography

The font used for this website was Quicksand which was found via Google fonts which can be found here [GoogleFonts](https://fonts.google.com/specimen/Quicksand "Link to the font used throughout the website")

## Features

### Existing Features

### Future Features

## Issues And Bugs

## Technologies Used

 * [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki") has been used because it is the standard markup language for documents designed to be displayed in a web browser.
 * [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3 "Link to CSS Wiki") has been used to style certain aspects of the website.
 * [Fontawesome](https://fontawesome.com/ "Link to FontAwesome") has been used for the icons used throughout the website.
 * [Googlefonts](https://fonts.google.com/) has been used to style the fonts of the writing on the web site. 
 * [Python](https://www.python.org/ "Link to Python")
 * [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)"Link to Flask Wiki")
 * [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript")
 * [jQuery](https://jquery.com/ "Link to jQuery") has been used to initialize Materialize functionality.
 * [Heroku](https://www.heroku.com/ "Link to Heroku") is used to deploy and host the project.
 * [Git](https://git-scm.com/ "Link to Git Homepage")
   * Git was used to utilise the GitPod terminal to allow the developer to commit and push to GitHub.
 * [GitHub](https://github.com/ "Link to GitHub Homepage")
   * GitHub was used to store the project after pushing.
 * [Balsamiq](https://balsamiq.com/ "Link to Balsamiq Homepage")
   * Balsamiq was used to create the wireframes during the designing stages of the project.

### Testing.md

For the testing section please refer to [TESTING.md](TESTING.md) file.

### Local deployment

* Login to your GitHub account and open up the repository you would like to copy
* Click on the button with a drop-down menu named ‘Code’ which will be placed next to the green ‘Gitpod’ button
* You will then have the option to download it on to your system via the ‘Download ZIP’ option

### Heroku deployment

1. Create a requirement.txt file that is need to Heroku to confirm dependencies. In your terminal please type:  
`pip3 freeze --local > requirements.txt`
2. Create a Procfile to confirm to heroku apps the commands that are executed by the app.  
`echo web: python run.py > Procfile`
3. Add, commit and push these files to GitHub.
4. In Heroku create a new app. The name has to be unique.
5. In Heroku you need to link Github to Heroku via the dashboard link "Deploy".  
 Go to "Deployment method" and choose "GitHub".  
 Below Deployment method find you repository name listed and select it.  
 6. Still in Heroku go to "Settings" and click "Reveal Config Vars"
 7. In this section you need to fill in the inputs field with the variables written in the env.py file.  
    - **SECRET_KEY** : `<your secret key>`
    - **STRIPE_PUBLIC_KEY** : `<this can be found from your Stripe account under the name of 'Publish key'>`
    - **STRIPE_SECRET_KEY** : `<your own personal secret key found in your Stripe dashboard>`
    - **STRIPE_WH_SECRET** : `<can be found in your 'endpoint' tab from your Strip account under the name of 'signing secret'>`
8. Then enable "Automatic deploys".
9. In "Manual Deployment" click "Deploy Branch".
10. You should get the message "Your app is successfully deployed".
11. Click "View" to lunch the app.

## Credits