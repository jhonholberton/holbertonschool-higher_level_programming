<img src="https://2.bp.blogspot.com/-vOlS5TOodb4/XxTq3sIsFFI/AAAAAAAATbQ/-aDZL-YLpdwVcK04cq2LwNH741OiC4g7ACLcBGAsYHQ/s0/SQL-server.jpg" style="height:100%;width:100%" />

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
**0-privileges.sql** |Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).|
**1-create_user.sql**     |Write a script that creates the MySQL server user user_0d_1.|
**2-create_read_user.sql**      | Write a script that creates the database hbtn_0d_2 and the user user_0d_2.|
**3-force_name.sql**  | Write a script that creates the table force_name on your MySQL server.|
**4-never_empty.sql**    | Write a script that creates the table id_not_null on your MySQL server.|
**5-unique_id.sql** |Write a script that creates the table unique_id on your MySQL server. |
**6-states.sql** | Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server. |
**7-cities.sql** | Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server. |
**8-cities_of_california_subquery.sql** | Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.|
**9-cities_by_state_join.sql** |Write a script that lists all cities contained in the database hbtn_0d_usa.|
**10-genre_id_by_show.sql**     | Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.|
**11-genre_id_all_shows.sql**      | Write a script that lists all shows contained in the database hbtn_0d_tvshows.|
**12-no_genre.sql**  |Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.|
**13-count_shows_by_genre.sql**    | Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.|
**14-my_genres.sql** | Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.|
**15-comedy_only.sql** | Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.|
**16-shows_by_genre.sql** | Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows. |

## Author

* **github** [jhonholberton](https://github.com/jhonholberton)
* **Linkedin:** https://www.linkedin.com/in/jhon-gonzalez-354487202