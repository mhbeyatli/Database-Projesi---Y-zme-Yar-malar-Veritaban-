Parts Implemented by Elanur Yoktan
==================================

OPENWATER SWIMMING
==================

   When user click the Openwater Swimming from the navigation bar, the main table that created 
   with using multiple left joins on 3 tables in one query, is going to appear.


   .. figure:: Yoktan/main.png
         :scale: 40 %
         :alt: Main  
         
         *This is the main page of openwater swimming*

   There is a navigation bar on the left side of the page. There are three different 
   tables and a main table. Each link on navigation bar points out one table and its 
   operations like add, delete, update and search. 
   
   These tables are: 
  
   1. Competition Results
   2. Swimmers
   3. Competition Informations
   
   When the user click to "ALL OPENWATER RECORDS", the main page of open water swimming 
   that shown above will remain. 
   
1. Competition Results
======================

   When the user click to "COMPETITION RESULTS", competition results table and buttons 
   that are about functions of table are going to appear.
   
   .. figure:: Yoktan/compresults.png
         :scale: 30 %
         :alt: Competition Results     
          
         *This is the competition results page*

   This table lists the results of the openwater competitions.

   In this table there are 3 attributes for user to enter. Two of them are referenced from other tables.

   These attributes are:
   
   1. competition id : it is an integer attribute and referenced from competition info table
   2. year           : it is a numeric(4) attribute
   3. winner id      : it is an integer attribute and referenced from swimmers table
   
1.1 Add Function
----------------

   The first function that i am going to explain is add function for Competition Results table. At the top of the page, there is 
   an add button.

   If the user wants to add a result to the table, he or she should click to add button first. Then, an add page will appear.
   
   .. figure:: Yoktan/cradd.png
         :scale: 30 %
         :alt: Competition Results Add Page  
         
         *competition results add form*
         
   Because of competition id and winner id are referenced from other tables, user should enter reasonable variables that are 
   also in reference tables. If the entered data is reasonable when user click to save button result is saved as shown below:
   
   .. figure:: Yoktan/crsaved.png
         :scale: 30 %
         :alt: saved result
         
         *saved result*

   If the entered data is not reasonable, that means at least one of the variables that is referenced from other table does not 
   exist in reference table. So, there is going to appear an error message.
   
   .. figure:: Yoktan/cradd2.png
         :scale: 30 %
         :alt: save result
         
         *Error message after added invalid result*
         
1.2 Delete Function
-------------------

   As shown below, there is a checkbox for each row of table, and at the buttom there is a delete button. After selection and 
   click delete, selected row is removed. 
   
   .. figure:: Yoktan/crdelete.png
         :scale: 30 %
         :alt: delete result
         
         *Delete function of competition results*
         
1.3 Update fuction
------------------
   
   For update operation user should select a row and click update. 
   
   .. figure:: Yoktan/crupdate.png
         :scale: 30 %
         :alt: update result
         
         *Update function of competition results*
   
   Then, an update page will appear. User should change data wanted to update and click update button. If changed data is 
   reasonable update occurs. 
   
   .. figure:: Yoktan/crupdate2.png
         :scale: 30 %
         :alt: update function
         
         *Update function of competition results*
     
   But, if changed data is not reasonable, it means referenced variables do not exist in reference table, there is going to 
   appear an error message.
   
   .. figure:: Yoktan/crupdate3.png
         :scale: 30 %
         :alt: update error
         
         *Error message after try to update with invalid result*


1.4 Search function
-------------------
   
   There is a problem in search function of this table.

2. Swimmers
===========

   When the user click to "SWIMMERS", swimmers table and buttons that are about functions of table are going to appear.
   
   .. figure:: Yoktan/swimmers.png
         :scale: 30 %
         :alt: Swimmers
         
         *Swimmers table*

   This table lists the informations of openwater swimmers.

   In this table there are 4 attributes for user to enter.

   These attributes are:
   
   1. swimmer id  : it is an integer attribute
   2. name        : it is a string attribute
   3. surname     : it is a string attribute
   4. nationality : it is a string attribute
   
2.1 Add Function
----------------
    
   At the top of the page, there is an add button.

   If the user wants to add a swimmer to the table, he or she should click to add button first. Then, an add page will appear.
   
   .. figure:: Yoktan/sadd.png
         :scale: 30 %
         :alt: Swimmers Add
         
         *Swimmers add form*
         
2.2 Delete Function
-------------------

   As shown below, there is a checkbox for each row of table, and at the buttom there is a delete button. After selection and 
   click delete, selected row is removed.
   
   .. figure:: Yoktan/sdelete.png
         :scale: 30 %
         :alt: Swimmers Delete
         
         *Swimmers delete form*
   
   For this table there is exceptional stuation. If data that wanted to remove, is used in another table user can not delete 
   this row and there is going to appear an error message.
   
   .. figure:: Yoktan/sdelete2.png
         :scale: 30 %
         :alt: Swimmers Delete Error
         
         *Error message after try to delete a data that are used in another table*


2.3 Update Function
-------------------

   There is a problem in update function of this table. 
   

2.4 Search Function
-------------------
   
   For search operation user should click search button. A search page will appear and user should enter name of swimmer because 
   search function searchs by name. 
   
   .. figure:: Yoktan/ssearch.png
         :scale: 30 %
         :alt: Swimmers Search
         
         *Swimmer search by swimmer name*
   
3. Competition Informations
===========================

   When the user click to "COMPETITION INFO", competition informations table and buttons that are about functions of table are 
   going to appear.
   
   .. figure:: Yoktan/compinfo.png
         :scale: 30 %
         :alt: Competition Info
         
         *Competition Informations Table*
         
         
   This table lists the informations of openwater competitions.

   In this table there are 5 attributes for user to enter.

   These attributes are:
   
   1. competition id     : it is an integer attribute
   2. competition name   : it is a string attribute
   3. number of swimmers : it is an integer attribute
   4. location           : it is a string attribute
   5. prize              : it is an integer attribute
   
3.1 Add Function
----------------
    
   At the top of the page, there is an add button.

   If the user wants to add a competition to the table, he or she should click to add button first. Then, an add page will appear.
   
   .. figure:: Yoktan/compadd.png
         :scale: 30 %
         :alt: Competition Add
         
         *Competition add form*
         
         
   .. figure:: Yoktan/compadd2.png
         :scale: 30 %
         :alt: Competition Saved
         
         *Competition saved*
       
3.2 Delete Function
-------------------

   As shown below, there is a checkbox for each row of table, and at the buttom there is a delete button. After selection and 
   click delete, selected row is removed.
   
   .. figure:: Yoktan/compdelete.png
         :scale: 30 %
         :alt: Competition Delete
         
         *Competition delete form*
         
   
   For this table there is exceptional stuation. If data that wanted to remove, is used in another table user can not delete 
   this row and there is going to appear an error message.
   
   .. figure:: Yoktan/compdelete2.png
         :scale: 30 %
         :alt: Competition Delete Error
         
         *Error message after try to delete a data that are used in another table*


3.3 Update Function
-------------------

   For update operation user should select a row and click update. 
   
   .. figure:: Yoktan/compupdate.png
         :scale: 30 %
         :alt: update competition button
 
   
   Then, an update page will appear. User should change data wanted to update and click update button.
   
   .. figure:: Yoktan/compupdate2.png
         :scale: 30 %
         :alt: update competition
   
   If changed data is used another table, data is also updated in other table.
   
     .. figure:: Yoktan/compupdate3.png
         :scale: 30 %
         :alt: update competition change other tables
   

3.4 Search Function
-------------------
   
   For search operation user should click search button. A search page will appear and user should enter name of competition
   because search function searchs by competition name. 
   
   .. figure:: Yoktan/compsearch.png
         :scale: 30 %
         :alt: Swimmers Search
         
         *Competition search by competition name*
