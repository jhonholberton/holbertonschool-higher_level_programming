<img src="https://miro.medium.com/max/1400/1*9TZHTGKjIyUOAvmQkV1RNA.png" style="height:100%;width:100%" />

# Python - Object-relational mapping

## Description

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

#### Files
Files | Description |
-------- | ----------- |
**0-select_states.py**   |Write a script that lists all states from the database hbtn_0e_0_usa.|
**1-filter_states.py**   |Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.|
**2-my_filter_states.py**   |Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.|
**3-my_safe_filter_states.py**   |Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?|
**4-cities_by_state.py**   |Write a script that lists all cities from the database hbtn_0e_4_usa.|
**5-filter_cities.py**   |Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa.|
**model_state.py**   |Write a python file that contains the class definition of a State and an instance Base = declarative_base().|
**7-model_state_fetch_all.py**   |Write a script that lists all State objects from the database hbtn_0e_6_usa.|
**8-model_state_fetch_first.py**   |Write a script that prints the first State object from the database hbtn_0e_6_usa.|
**9-model_state_filter_a.py**   |Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa.|
**10-model_state_my_get.py**   |Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa.|
**11-model_state_insert.py**   |Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa.|
**12-model_state_update_id_2.py**   |Write a script that changes the name of a State object from the database hbtn_0e_6_usa.|
**13-model_state_delete_a.py**   |Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa.|
**14-model_city_fetch_by_state.py**   |write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa.|
**model_city.py**   |Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.|

## Author

* **github** [jhonholberton](https://github.com/jhonholberton)
* **Linkedin:** https://www.linkedin.com/in/jhon-gonzalez-354487202