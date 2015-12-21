##################################
Parts Implemented by Mustafa Tıkır
##################################
   When the user click to records bar in the main page, records of the swimmers is going to appear.

   .. figure:: MainPage.png
      :scale: 50 %
      :alt: Main

      *This is the main page*

   Click to the records bar

   .. figure:: RecordsPage.png
      :scale: 50 %
      :alt: Records

      *This is the records page*

   Records page has been appeared.

   In Records page there are 3 tables about swimmer records, and all these tables have 4 fucntions for each one.

   These tables are:

1. Record List
2. High Scores List for Records
3. Lowest Scores List for Records

   Functions for each one have same name and functionality, and their names are:

1. Add
2. Delete
3. Update
4. Search


Functions are going to be explained in the tables

1. Record List
==============
   This table lists the records of the swimmers. It consists of the swimmers of other 2 tables and additional swimmers.

   This is the main table for this project. If user wants to add an swimmer record to other tables or update some data,
   its score have to be in this table.

   In this table there are 2 attributes for user to enter, and one secret attribute that is enabled for default
    for ordering the records.

   So, 2 attributes are showen at the screen.

   These attributes are:

   1. Name of the swimmer  : it is an string attribute
   2. Score                : it is an integer attribute
   3. ID of swimmer        : it is an also integer attribute, but it is enabled by default

   Let me explatin the functions

1.1 Add fuction
---------------
   The first function that i am going to explain is add function for Records list.

   In the Records Page, at the top of the page, there is an button, and it is add button.

   If the user wants to add some record to the table, he or she shoul click to button first.

   .. figure:: AddFuctionRecordList1.png
      :scale: 50 %
      :alt: Add Function for Record List

      *Add button is shown at the top of the page*

   When add button is clicked, the address of wab page is going to be changed and an simple form page will appear.

   .. figure:: AddFuctionRecordList2.png
      :scale: 50 %
      :alt: Add Function form for Record List

      *Add form is shown at the top of the page*

   At this page, the user should write an string for the name and integer for the record.

   After user write the data, it is enough to click to save button being at the buttom of the page.

   And as it is shown below, it is added to Records list.

   .. figure:: AddFuctionRecordList3.png
      :scale: 50 %
      :alt: Data is added for Record List

      *The new appearance of Record list with new data*

1.2 Delete fuction
------------------
   It is really easy to delete an row(tuple) from the table.

   As shown below, there is an empty button for each row of table, and at the buttom there is delete button.

   .. figure:: DeleteFuctionRecordList1.png
      :scale: 50 %
      :alt: Delete fuction for Record List

      *This screen cast shows how the delete function works*

   When one of the empty button is clicked and the delete is pressed, then that row of the table is going to be deleted.

   As it is shown below, it is deleted from the Records list.

   .. figure:: DeleteFuctionRecordList2.png
      :scale: 50 %
      :alt: After delete operation is done for Record List

      *The new appearance of Record list after the delete operation is implemented.*

   **Important Note**

   As i mentioned before, the value is going to be deleted dont have to be in the other tables.

   What if it is in the other tables, there is going to appear an error message.

   This error message is shown below

   .. figure:: DeleteFuctionRecordList3.png
      :scale: 50 %
      :alt: After an invalid tuple try to delete

      *Error message after invalid tuple tried to be deleted*

1.3 Update fuction
------------------

   Update function updates the data in the Records list.

   For update an row of the table, the user should first select the update button which is at the bottom.

   .. figure:: UpdateFuctionRecordList1.png
      :scale: 50 %
      :alt: Update operation for Record List

      *User needs to click to update button first*

   After user clicked to update button, an new web page appears. That web page shows all the attributes and tuples of the table.

   And, all rows have an button their left hand side for selecting the tuple which is going to be updated.

   The user should select one of these and should fullfilled the form with true types of characthers.

   And then, user should click the update.

   .. figure:: UpdateFuctionRecordList2.png
      :scale: 50 %
      :alt: Update form for Record List

      *This screen cast shows how the update form seems and works*

   After the all necessery things is done in update form. The new appeance of Record page with updated data appears.

   .. figure:: UpdateFuctionRecordList3.png
      :scale: 50 %
      :alt: After update operation is done for Record List

      *Record list with updated data*

   **Important Note**

   What if the record with existing in the other tables want to be updated?

   The answer is the name of that tuple can be updated, but score of that tuple cannot be updated. So, it stays same in
   case it is tried to be changed.

1.4 Search fuction
------------------

   The another and last fuction for Records table is search function.

   It is easy to implement. Click to search function which is below of the table and shown below figure

   .. figure:: SearchFuctionRecordList1.png
      :scale: 50 %
      :alt: Search operation for Record List

      *Click to search*

   If user clicks to search funciton, the web site turns an new page and that page request an name for searching

   .. figure:: SearchFuctionRecordList2.png
      :scale: 50 %
      :alt: Search form for Record List

      *Type the full name of swimmer for searching*

   The user should write the full name of the swimmer for seaching.

   After user write it, the page shown below appears

   .. figure:: SearchFuctionRecordList3.png
      :scale: 50 %
      :alt: After Search operation for Record List

      *The page after search operation correctly done*

   If invalid name is entered, the page is going to show no value.

2. High Scores List for Records
===============================
   This table lists only the records of swimmer who has high score.

3. Lowest Scores List for Records
=================================
   This table lists only the records of swimmer who has low score.


