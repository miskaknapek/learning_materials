#{ sqlite learning }
----------------------------
###( 20130712 )



##resources


nice basic tutorial
(this I've also saved to disk)
http://souptonuts.sourceforge.net/readme_sqlite_tutorial.html

- command line sqlite tutorial
http://www.sqlite.org/sqlite.html

- using sql for lightweight data anlaysis (by rufus)
https://schoolofdata.org/2013/03/26/using-sql-for-lightweight-data-analysis/

- quick guide to sqlite commands 
http://www.sqlite.org/cli.html

w3schools’ sql intro 
https://www.w3schools.com/sql/default.asp


####quick various tidbits : 
—————

how to matplotlib on a remote server ( without a display ) 
https://stackoverflow.com/questions/5503601/python-headless-matplotlib-pyplot 
how to connect sqlite3 with python 
http://pythoncentral.io/introduction-to-sqlite-in-python/ 
more : http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/



###prototyping environments
——————

- online prototyping environment 
http://sqlfiddle.com/



@@code
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


###datatypes of sqlite3
—————————
( SQLite page )

    -  NULL
    - INTEGER
    - REAL ( floating point num ) 
    - TEXT ( utf-8. utf-16be, or utf-16le
    - BLOB ( blob of data, stored exactly as it is input ) 


###import data, eg csv 
————————

    sqlite> create table foo(a, b);  	// make schema 
    sqlite> .mode csv				// set to csv mode
    sqlite> .import test.csv foo		// do the importing

optional : 
    set separator and import
    	•	sqlite> .separator "\t" ---IMPORTANT! should be in double quotes
    	•	 sqlite> .import afile.csv tablename-to-import-to


###how to check the schema ( datatypes ) of a table
————————

    sqlite> schema table_name  	// make schema 
    sqlite> CREATE TABLE table_name( f1 varchar(10), f2 varchar(10) );
    another example 
    insert into test (f2) values( 00 );


###how to limit output : 
—————————

    sqlite> select * from test limit 1;
    1|2


###how to print from a certain line : 
—————————

    sqlite> select * from test offset 1;
    |0


###create a table from the command line
------------------
    code (from bash):
    sqlite3 databasename.db


###define table
----------------
    sqlite3 databasename.db "create table t1 ( t1key INTEGER PRIMARY KEY, data TEXT, num double, timeEnter DATE);"

or just (from inside sqlite3 )

    "create table t1 ( t1key INTEGER PRIMARY KEY, data TEXT, num double, timeEnter DATE);"    

###insert values
---------------
    sqlite3 databasename.db "insert into t1 (data, num) values ('This is sample data', 3);"
    sqlite3 databasename.db "insert into t1 (data, num) values ('more sample data', 6);"
    sqlite3 databasename.db "insert into t1 (data, num) values ('and a bit more', 9);"

!!! NOTE (above ) : the columns for inserting data are specified ( data, num ) - there are in fact more data columns.

###show/select particular values
------------------
sqlite3 databasename.db "select * from t1"
# show only the first two rows (there are three rows by now)
    sqlite3 databasename.db "select * from t1 limit 2"

// shows only rows where the num (third) column has a value >3 and <12

    sqlite3 databasename.db "SELECT * from t1  WHERE num > 3 AND WHERE num < 12 "
 
    sqlite> select * from shippinglists02 where HELCOM_Detail_ShipType = "Yatch" limit 100 ;
    1000239|316002960|CFK4220|Canada|A|2006|MQ2|48.6|8|3|467|12|Other|Yatch
    1006829|310380000|ZCDF7|Bermuda|A|2006|LE GRAND BLEU|108.3|17.1|5.05|5556|1666|Other|Yatch
    1006881|319622000|ZCGA2|Cayman Islands|A|2006|HAMPSHIRE|50|10|3.4|685|205|Other|Yatch
    1007287|319741000|ZCGS3|Cayman Islands|A|2006|SKAT|70.7|13.2|3.8|1998|599|Other|Yatch
    … etc…



###DISTINCT
------------------
    select unqiue values in a given column ( or unique combinations of several columns ) 

    SELECT DISTINCT columnName FROM table

    // specific 
    SELECT DISTINCT customerID FROM orders order by customerid;
    // two column unique combos 
    SELECT DISTINCT customerID, shipperid FROM orders order by shipperid;


###select similar … with LIKE 
------------------
( one can also do regular expressions with this :) 

    SELECT * FROM categories WHERE description LIKE ‘%tea%’;


    > 1|Beverages|Soft drinks, coffees, teas, beers, and ales



###IN 
… allows one to specify several values in the WHERE clause
( the IN operator is sort of like writing several OR conditions )
------------------

    SELECT * FROM Customers
    WHERE Country IN ('Germany', 'France', 'UK');

    SELECT * FROM Products
    WHERE (Price BETWEEN 10 AND 20)
    AND NOT CategoryID IN (1,2,3);



###AS (alisases)
------------------
Give something, or an expression, a name, using AS, eg… 

    select o.orderID, o.orderdate, c.customername from orders as o, customers as c where c.customerid=o.customerid;

    SELECT Orders.OrderID, Orders.OrderDate, Customers.CustomerName
    FROM Customers, Orders
    WHERE Customers.CustomerName="Around the Horn" ANDCustomers.CustomerID=Orders.CustomerID;



###BETWEEN 
------------------
… selects values between a given value range 

    select price from products where price between 10 and 50 order by price;



###INNER JOIN 
-----------
the intersection of sets… i.e. an AND operation
    
    select * from orders inner join customers on orders.customerid=customers.customerid and country like "%portugal%"



###LEFT JOIN 
-----------
returns all the items from the left dataset, plus the matching rows from the right dataset.

    
    SELECT Customers.CustomerName, Orders.OrderID
    FROM Customers
    LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    ORDER BY Customers.CustomerName;



###RIGHT JOIN 
-----------
returns all the items from the right dataset, plus the matching rows from the left dataset.

    SELECT Customers.CustomerName, Orders.OrderID
    FROM Customers
    RIGHT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    ORDER BY Customers.CustomerName;



###FULL OUTER JOIN 
-----------
returns all records, from left and right datasets, where there is a match

    SELECT Customers.CustomerName, Orders.OrderID
    FROM Customers
    FULL OUTER JOIN Orders ON Customers.CustomerID=Orders.CustomerID
    ORDER BY Customers.CustomerName;



###SELF JOIN
-----------
A self join is a regular join, but where the table is joined with itself .
I.e. one does an internal operation on the table, comparing elements of the table with itself. 
Eg. the following query allows one to create a list of customers within the same city. 

    SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2,A.City
    FROM Customers A, Customers B
    WHERE A.CustomerID <> B.CustomerID
    AND A.City = B.City 
    ORDER BY A.City;


###UNION (ALL)
-----------
Combines the results of two or more SELECT statements
- Each SELECT statement within UNION must have the same number of columns.
- The columns must also have similar data types
- The columns in each SELECT statements must also be in the same order

    SELECT City FROM Customers
    UNION
    SELECT City FROM Suppliers
    ORDER BY City;

    (union all - takes care of duplicate values ) 

    SELECT City FROM Customers
    UNION ALL
    SELECT City FROM Suppliers
    ORDER BY City;

    ( union with where ) 

    SELECT City, Country FROM Customers
    WHERE Country='Germany'
    UNION
    SELECT City, Country FROM Suppliers
    WHERE Country='Germany'
    ORDER BY City;

    ( union all with where ) 

    SELECT City, Country FROM Customers
    WHERE Country='Germany'
    UNION ALL
    SELECT City, Country FROM Suppliers
    WHERE Country='Germany'
    ORDER BY City;



###GROUP BY 
-----------
Used to group results by values in particular columns. 
( Often used in combination with aggregate functions ( count, max, min, sum, avg )

    SELECT COUNT(CustomerID), Country
    FROM Customers
    GROUP BY Country;

    // similar to the above, but orders it by the number of customers 
    SELECT COUNT(CustomerID), Country
    FROM Customers
    GROUP BY Country
    ORDER BY COUNT(CustomerID) DESC;



###HAVING
-----------
A way of signifying/asking for particular properties, a bit like WHERE. 
However, as WHER can’t be used by aggregate functions, HAVING can. 

    SELECT COUNT( CustomerID), Country
    FROM Customers
    GROUP BY Country
    HAVING COUNT( CustomerID ) > 5;

    // sightly modified version of the above 
    SELECT COUNT( CustomerID), Country
    FROM Customers
    WHERE CustomerID > 3    //  << EG WITH WHERE
    GROUP BY Country
    HAVING COUNT( CustomerID ) > 5;



###EXISTS
-----------
For testing whether a record exists at all, in a subquery. 
The EXISTS operator returns true if the subquery returns one or more records.

    SELECT SupplierName
    FROM Suppliers
    WHERE EXISTS (SELECT ProductName FROM Products WHERE SupplierID = Suppliers.supplierId AND Price < 20 );

    SELECT SupplierName
    FROM Suppliers 
    WHERE EXISTS ( SELECT ProductName FROM Products WHERE SupplierId = Suppliers.supplierId AND Price = 22 );



###AND and ALL
-----------
Are like AND/OR in searches, in conjunction with which search queries match. 
Need to be used with WHERE and HAVING clauses. 
Any returns true if any subquery matches. 
All returns true only if all subquery matches, match. 

( NOTE : DOESN’T WORK SO WELL WITH SQLITE3 )

    SELECT ProductName
    FROM Products
    WHERE ProductID = ANY ( SELECT ProductID FROM OrderDetails WHERE Quantity = 10 );

    SELECT ProductName
    FROM Products
    WHERE ProductID = ANY (SELECT ProductID FROM OrderDetails WHERE Quantity > 99);

    SELECT ProductName
    FROM Products
    WHERE ProductID = ALL (SELECT ProductID FROM OrderDetails WHERE Quantity = 10);



###SELECT INTO
-----------
Copies the rests of a query into  a new table. 
Can also copy only some of the columns into the new table. 

( NOTE : DOESN’T WORK SO WELL WITH SQLITE3 )

    SELECT * INTO CustomersBackup2017
    FROM Customers;

    SELECT * INTO CustomersBackup2017 IN 'Backup.mdb'
    FROM Customers;

// Copies only the German companies

    SELECT * INTO CustomersGermany
    FROM Customers
    WHERE Country = 'Germany';

// copies data from several tables into a new table 

    SELECT Customers.CustomerName, Orders.OrderID
    INTO CustomersOrderBackup2017
    FROM Customers
    LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

// to copy the schema of another table 
// ( add a condition that can’t be satisfied, and you get an empty table ) 

    SELECT * INTO newtable
    FROM oldtable
    WHERE 1 = 0;



###INSERT INTO SELECT
-----------
Copies data from one table and inserts it inot another 
( requires that data types in the source and destination tables match )
( the existing records in the target table are unaffected )

// copies Suppliers into Customers ( columns without data will contain null )

    INSERT INTO Customers (CustomerName, City, Country)
    SELECT SupplierName, City, Country FROM Suppliers;

// copies Suppliers into Customers (fills all columns )

    INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode,Country)
    SELECT SupplierName, ContactName, Address, City, PostalCode, Country FROMSuppliers;

// copies As above, but only copies German customers
    
    INSERT INTO Customers (CustomerName, City, Country)
    SELECT SupplierName, City, Country FROM Suppliers
    WHERE Country='Germany';


###CREATE VIEW
-----------
Creates and stores a particular view onto the data, as a variable, which persists through restarts.
 ( Variable === V_Customer, in the example below )

    CREATE VIEW V_Customer
    AS SELECT First_Name, Last_Name, Country
    FROM Customer;

// more advanced

    CREATE VIEW V_REGION_SALES
    AS SELECT A1.Region_Name REGION, SUM(A2.Sales) SALES
    FROM Geography A1, Store_Information A2
    WHERE A1.Store_Name = A2.Store_Name
    GROUP BY A1.Region_Name;



###TRUNCATE TABLE
-----------
Remote the entries from the table, but not the table itself. 
Faster and less resource intensive than DELETE FROM, apparently 

    TRUNCATE TABLE Customer;



###CONCATENATE
-----------
Allows concatenating several variables into one string .

    SELECT CONCAT(Region_Name, Store_Name) FROM Geography 
    WHERE Store_Name = 'Boston';

    // oracle syntax, which works nicely with sqlite3
    select  city||''||country from suppliers;


###SUBSTRING / SUBSTR()
-----------
Fetches portions of a string - as in javascript 

    SELECT SUBSTR (Store_Name, 3) 
    FROM Geography 
    WHERE Store_Name = 'Los Angeles';

// combine it with the concatenate commands :) 

    select  substr(city,0,3)||'/'||substr(country,0,3) from suppliers;


###INSTR  ( < alas, not so sqlite3 compatible :( ) 
-----------
Function for finding the start of a pattern in a string. 
( Maybe Index is the relevant JS equivalent )

    SELECT INSTR (Store_Name, 'o') 
    FROM Geography 
    WHERE Store_Name = 'Los Angeles';



###TRIM  
-----------
Removes bits and pieces of text from  a string 

TRIM( [ [LOCATION] [remstr] FROM ] str)



###LENGTH  
-----------
Length of a string 

    select length( country) from suppliers;



###REPLACE
-----------
Replaces - something in string str1, where str2 occurs, replace it with str3

    REPLACE (str1, str2, str3)



###OVER
————
Something about partitions… read more here … 







###offset - from where things begin
-------
( there are three rows, but this only starts at the third one, and shows only a single row in any event )

    sqlite3 databasename.db "select * from t1 limit 1 offset 2";



###show the table names
-----------
    sqlite3 databasename.db ".table"




###write the table data to a csv file
------------------
(remember the writing to stdout is where the magic writing actually/finally happens)
( code )

    sqlite> .mode csv
    sqlite> .output results.csv
    sqlite> SELECT * from t1;
    sqlite> .output stdout
    sqlite> .quit




###list the actions done to the database
------------
    sqlite3 databasename.db ".dump";




###various random example queries 
————

    // takes the shipping list and extracts the count of ships, per country, that have a net tonnage btw 80-90 tonnes, groups by country.
    select count(imo), country from hships where Net_tonnage > 80 AND Net_tonnage < 90 group by country order by count(imo);

    // displays country-ordered list by the sum( net_tonnage ) per country ( where the net tonnage is over 1500 tonnes ) 
    select sum( net_tonnage ), country from hships group by country having sum( net_tonnage ) > 1500 order by country;







