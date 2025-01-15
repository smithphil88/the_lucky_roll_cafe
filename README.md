# The Lucky Roll Cafe

Image of site on different devices

## Table of Contents

- [Introduction](#introduction)
- [Design](#design)
- [Features](#features)
- [User Stories](#user-stories)
- [Languages](#languages)
- [Database](#database)
- [Agile Design Principles](#agile-design-principles)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## Introduction

The focus of this site was to implement the django framework and python on the back-end in order to create a user-friendly site. The site is a board game cafe site, where the user is able to create, edit and delete a user account along with the ability to book a specific type of table dependent on the users needs. As per the scope of the project, CRUD (create, read, update and delete) ideology was followed and the user is able to edit and delete their booking if they so wish to. The site has an admin panel for the business owner to allow messages to be sent by the user for any additional requests (table location, food requirements etc.)

## Design

The idea behind the design for the site was simplicity and functionality presented in an appealing and intuitive manner. Users who would be brought to the site are likely to know what they want and the design encourages them to use the site. Navigation throughout the site is intuitive with functions such as being able to access the nav-bar at all times and having messages appear to let them know a certain request has been successful or unsuccessful. I thought about the customer base for this type of business and wanted a historic and old feel to the site.

### Color Scheme

I choose a color scheme that fit with the theme of coffee and board games. I found I color scheme that fitted my theme from [coolors.com](https://coolors.co/dad7cd-a3b18a-588157-3a5a40-344e41)

### Font

My font was chosen from [googlefonts](https://fonts.google.com/specimen/Modern+Antiqua) - I chose Modern Antiqua as it fell under the medieval filter on google fonts and this links suitably with the historic feel I initially desired.

### Wireframes

I used the [Balsamiq](https://balsamiq.com/) wireframing tool to design simple mock-ups of my site to give me an initial idea of how the site layout should be.

![screenshot](documentation/wireframes/wireframe-home.png)
![screenshot](documentation/wireframes/wireframe-register.png)
![screenshot](documentation/wireframes/wireframe-signout.png)
![screenshot](documentation/wireframes/wireframe-booking.png)

## Features

### Site Pages

The following examples are screenshots of the various pages on my site.

### Home page

This is where the user will first land on the site, it leads them to either registering if it their first time visiting the site. A user must register in order to view any details. Or if they alreay have an account, they can proceed to the login page.

![screenshot](documentation/features/homepage-signedin.png)

### About page

This page includes information about what the cafe provides. It enables users to go directly to the booking form if the so wish, it includes a small selection of what games are on offer in the cafe and a drinks menu too.

![screenshot](documentation/features/about.png)

### Booking page

On this page, a logged in user is able to choose details for their booking at the cafe. The user has to include details of the type of table they so require, a date of booking, which has been designed so they cannot book in the past, a choice of time slots are avaliable, number of guests (with the maximum being 12) and a place where the user can disclosure any further requirements.

![screenshot](documentation/features/booking.png)

### My Profile page

In this section of the site a user is able to update their information, such as username, first name and last name. If they so wish a user is able to find out information about restting their password on this page too. The ability to delete their account is also included on this page with a modal appearing confirming if a user is sure they want this action to occur.

![screenshot](documentation/features/profile.png)

### My Bookings page

This page displays all bookings that a user has made. They appear with two functions, the ability to edit or delete a booking.

![screenshot](documentation/features/my-bookings.png)

### User actions

User registration

![screenshot](documentation/features/register.png)

User login

![screenshot](documentation/features/login.png)

User logout

![screenshot](documentation/features/logout.png)

Password reset

![screenshot](documentation/features/reset-password.png)

User profile edit

![screenshot](documentation/features/edit-profile.png)

Delete profile

![screenshot](documentation/features/account-delete.png)

Book a table

![screenshot](documentation/features/booking.png)

Edit a booking

![screenshot](documentation/features/edit-booking.png)

Delete a booking

![screenshot](documentation/features/booking-delete.png)

### Future features

#### Game review 

A page on the site where a user can post their own experience of a board game. This would be akin to Trip Advisor, with a rating system, the ability to post a photo and a text area where the user can offer their opinion.

#### Comprehensive message to business owners function

This would be an area of the site where a user can make board game recoomendations, ideas for events/theme nights etc directly to the owner. 

## User Stories

All of user stories can be located in the liked GitHub project [here](https://github.com/users/smithphil88/projects/3).

## Languages

Technologies used;

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [Heroku](https://www.heroku.com) used for hosting the deployed site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [Gunicorn](https://gunicorn.org/) used for WSGI server

## Database

Lucid chart image

![screenshot](documentation/lucidchart.png)

## Agile design principles

Github project screenshot

Github issues screenshot
Use of MoSCoW  

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

## Credits

### Content

| Source | Comments |
| --- | --- | --- |
| [Flexbox Froggy](https://flexboxfroggy.com/) | modern responsive layouts |
| [W3 Schools](https://www.w3schools.com/django/index.php) | django basics |