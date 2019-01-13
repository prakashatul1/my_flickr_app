# my_flickr_app

## Getting Started

* Create a virtual environment using python 3
* Activate virtual environment
* Clone Project
* Install requirements.txt
* Run command (to get photos from flickr and save in db )
```
python manage.py run_deployment_script
```
Database is alrready having the Data ,to test you need to delete all the models in flickr app using
```
python manage.py shell
```
command and delete 'images' folder inside 'media' folder under project directory.
* Run Django server and you are good to go
