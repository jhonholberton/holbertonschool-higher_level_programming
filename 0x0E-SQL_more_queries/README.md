<img src="https://2.bp.blogspot.com/-vOlS5TOodb4/XxTq3sIsFFI/AAAAAAAATbQ/-aDZL-YLpdwVcK04cq2LwNH741OiC4g7ACLcBGAsYHQ/s0/SQL-server.jpg" style="height:50%;width:100%" />

# 0x0D. SQL - Introduction

# Description

MySQL is an open-source database management software that helps users store, organize, and later retrieve data. It has a variety of options to grant specific users nuanced permissions within the tables and databases—this tutorial will give a short overview of a few of the many options.

````CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';````

The CREATE USER statement creates one or more user accounts with no privileges. It means that the user accounts can log in to the MySQL Server, but cannot do anything such as selecting a database and querying data from tables.

To allow user accounts to work with database objects, you need to grant the user accounts privileges. And the GRANT statement grants a user account one or more privileges.

The following illustrates the basic syntax of the GRANT statement:

````GRANT privilege [,privilege],..````
````ON privilege_level ````
````TO account_name;````

## Learning Objectives

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION



#### Files
Files | Description |
-------- | ----------- |
**0-list_databases.sql** |Write a script that lists all databases of your MySQL server.|
**1-create_database_if_missing.sql**     |Write a script that creates the database hbtn_0c_0 in your MySQL server.|
**2-remove_database.sql**      | Write a script that deletes the database hbtn_0c_0 in your MySQL server.|
**3-list_tables.sql**  | Write a script that lists all the tables of a database in your MySQL server.|
**4-first_table.sql**    | Write a script that creates a table called first_table in the current database in your MySQL server.|
**5-full_table.sql** | Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server. |
**6-list_values.sql** | Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server. |
**7-insert_value.sql** | Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server. |
**8-count_89.sql** | Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server. |
**9-full_creation.sql** |Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.|
**10-top_score.sql**     | Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.|
**11-best_score.sql**      | Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.|
**12-no_cheating.sql**  | Write a script that updates the score of Bob to 10 in the table second_table.|
**13-change_class.sql**    | Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.|
**14-average.sql** | Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.|
**15-groups.sql** | Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.|
**16-no_link.sql** | Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server. |

## Author

* **github** [jhonholberton](https://github.com/jhonholberton)
* **Linkedin:** https://www.linkedin.com/in/jhon-gonzalez-354487202