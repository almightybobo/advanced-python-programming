# Intro to Databases

This unit covers the fundamentals of dealing with Databases using Python. "Databases", as a general topic, is incredibly broad and complex. It's a science on itself and a discipline expanding decades. This unit assumes you know the basics of Relational Databases; you know about database engines, tables, rows, columns and a little bit of SQL. If that's not the case, and you feel you should learn a little bit more about Relational Databases, you can get started with this Free course from Udacity: **[Intro to Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197)**.

## SQLite

Throughout this unit, we'll use [SQLite](https://en.wikipedia.org/wiki/SQLite) as our Database Engine. Most traditional Relational Database Engines act as Client-Server architectures. That means, you need to install the Database Server, execute it, and then connect from your Python code to it (as a client). That's overly complicated for this unit, as we want to focus mainly in the concepts behind Database work, which can be found in any DB Engine: Postgres, MySQL, Oracle and obviously, SQLite.

Python includes a SQLite library already buitlin. That means that **you don't have to install ANYTHING**. It works out of the box.

SQLite works by creating files that act as the persistent storage for our database. Our entire database will be contained in a single file which we'll load and save as we're working in our application.

## Getting Started with Python and SQLite

You can use a script as simple as the following one to get started:

```python
import sqlite3

db = sqlite3.connect('example.db')

c = db.cursor()

TABLE_SQL = """
CREATE TABLE book (
  id integer primary key autoincrement,
  author text not null,
  title text not null,
  isbn text
);
"""

# Create table
c.execute(TABLE_SQL)

# Insert a row of data
c.execute("INSERT INTO book VALUES (1, 'Edgar A. Poe', 'The Raven', 'X-99')")

db.commit()

results = c.execute('SELECT * FROM book')

for result in results:
    print(result)
```

Both [Python 2](https://docs.python.org/2/library/sqlite3.html) and [Python 3](https://docs.python.org/3/library/sqlite3.html) support SQLite, so make sure you check their comprehensive docs.
