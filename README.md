# Epicurious

##### By [Cynthia Oduol](https://github.com/cynthiaoduol)

Github link: https://github.com/cynthiaoduol/Cook-book.git 

Live site: [View Site]( https://epicuriousrecipe.herokuapp.com/)
  
# Description  
Epicurious is a recipe website that helps people who are proficient cooks find for new ideas and gives guigance to those who are in need of the guidance while cooking.


 
## User Story  
As a user I would like to:
* Sign in to the application to view the different food recipes
* Set up a profile about themselves.
* Find a list of different recipes after signing in.
* Only view details of a single neighborhood.
* Bookmark a single recipe.
* Post their own recipes for others to view.
* Comment on a recipe.
  
  

  
## Setup and Installation  
To get the project : 
  
##### Clone the repository:  
 ```bash 
 https://github.com/cynthiaoduol/Cook-book.git 
```

##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual 
- source virtual/bin/activate  
```  


##### Navigate into the folder:
 ```bash 
cd Cook-book 
```

##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrations:
 ```bash 
python manage.py makemigrations epirecipe
 ``` 
 Then Migrate: 
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
 
 
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/1.1/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs at the moment.
  
## Contact Information   
If you have any question or contributions, please email me at cynthiaobu940@gmail.com 
  


 Copyright (c) 2019 **Cynthia Oduol** 