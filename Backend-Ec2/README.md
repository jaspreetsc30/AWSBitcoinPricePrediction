## Flask App 
This is a basic application with the flask infrastructure.


#### How does it work?
Each "routes" should be modularised within its own `.py` file inside the `/routes/restapi` folder. 

Points to note:
1. Each endpoint can be defined in the form of a function, make sure each function is **UNIQUE** across the entire application, i.e. there shouldn't be another function with the same exactname.
2. Each endpoint can be structured as follows.
![image](https://user-images.githubusercontent.com/44058187/122789417-e10ef980-d2e9-11eb-9467-20bca97861c8.JPG)
3. Don't forget to import a new **"route"** file in `routes/__init__.py` as follows.
![import](https://user-images.githubusercontent.com/44058187/122790103-92159400-d2ea-11eb-8942-33a47125371d.JPG)

#### Setting up the environment
To set up the environment, we need to create a virtual environment. You can use `virtualenv` to create one. Once you have activated your virtual environment, simply install all the requirements from 
requirements.txt by `pip install -r requirements.txt`.

#### How to run the application?
To run the application, we have to simply run the command `flask run` with specifications on port and ip address to deploy the app to.

