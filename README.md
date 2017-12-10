# WEBSITE'S LOG
### this is a log analysis of a website


#### _the queries are:_
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

## Defined views:

* **errors** view

`create view errors as
  select to_char(time, 'month dd, yyyy') as day, count(*) as total from log
  where status like '%404%' group by day;`

* **requests** view

`create view requests as
 select to_char(time, 'month dd, yyyy') as day, count(*) as total from log group by day;`


# Needed Software
  you will need python3 and postgresql to run this code
  * download python from [here](https://www.python.org/downloads/release/python-363/)

  * download postgresql from [here](https://www.postgresql.org/download/)

**OR** _you can download VirtualBox/Vagrant environment_
* you can download VirtualBox from [her](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)

* you can download vagrant from [here](https://www.vagrantup.com/)



# Use a terminal
you will use a Unix-style terminal on your computer, If you are a __Linux__ or a __Mac__ user your will do fine.
On __Windows__ I recommend using the __Git Bash__ terminal that comes with the __Git__ software.
If you don't have __Git__ installed you can get it from [here](https://git-scm.com/downloads).
And if you are new to terminal-style and BASH you can take a look at [this](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/)





# Download the Data
the database that you are going to work on is in _newsdata.sql_ file. You can download it from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)


To build the reporting tool, you'll need to load the site's data into your local database.

To load the data, `cd` into the vagrant directory and use the command `psql -d news -f newsdata.sql`.
Here's what this command does:
* `psql` — the PostgreSQL command line program
* `-d news` — connect to the database named news which has been set up for you
* `-f newsdata.sql` — run the SQL statements in the file newsdata.sql

### _How to run it_:
There is a single python file called "log.py".
`cd` to the directory where the _log.py_ exists, open a terminal window and type `python log.py`
