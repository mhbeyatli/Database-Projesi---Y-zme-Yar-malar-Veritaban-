Parts Implemented by Muhammed Habib Beyatlı
===========================================

SWIMMING MEDALS
===============
   When it is clicked to Swimming Medals link, three tables about swimming medals will be showed up.

   .. figure:: mhb/Main.png
      :scale: 50 %
      :alt: Main

   These are Medals, Medal Records, and Front-Runner tables.
   All the tables have add, delete, and update functions.
   There is also a text bar on the top of the page which can allow search in Medals and Front-Runner tables.

1.Medals
========
   Medals table is the main table of this part. This table is top of the hierarchy. It is directly connected to Medal Records table.
   Medals table shows the which countries won the medals in competetions.

   .. figure:: mhb/Medals1.png
      :scale: 50 %
      :alt: Medals

   There are 4 attributes of Medals table.
   Competition ID: An integer attribute which generates automatically and is related to Medal Records table.
   Gold: A varchar attribute.
   Silver: A varchar attribute.
   Bronze: A varchar attribute.

1.1 Add function of Medals
--------------------------

   If a user wants to add a data to the table, s/he must click 'Add New Competition' button which is holding on the table.

   .. figure:: mhb/Medals1.png
      :scale: 35 %
      :alt: Medals

   When it is clicked to the button, a form will be seen.

   .. figure:: mhb/Medals2.png
      :scale: 35 %
      :alt: Medals

   The user writes the data in the boxes and click 'Save' button to add the record the table and the database via this form.

   .. figure:: mhb/Medals3.png
      :scale: 35 %
      :alt: Medals

1.2 Delete function of Medals
-----------------------------

   If a user wants to delete a data from the table, s/he must click the 'Delete' button which is holding right of the table.

   .. figure:: mhb/Medals4.png
      :scale: 35 %
      :alt: Medals

   When it is clicked to the button, the data will delete from the table and the database.

   .. figure:: mhb/Medals5.png
      :scale: 35 %
      :alt: Medals

   If 'Competition ID' attribute matches a record in the Medal Records table, an error message will occur and the deletion cannot be completed.

   .. figure:: mhb/Medals6.png
      :scale: 35 %
      :alt: Medals

1.3 Update function of Medals
-----------------------------

   If a user wants update a record, s/he must click the 'Update' button which is the last element of the table.

   .. figure:: mhb/Medals7.png
      :scale: 35 %
      :alt: Medals

   When it is clicked to the button, a new page will be appear which have boxes and the old values of the record.

   .. figure:: mhb/Medals8.png
      :scale: 35 %
      :alt: Medals

   The user changes the data in the boxes and click 'Save' button to update the record the table and the database via this page.

   .. figure:: mhb/Medals9.png
      :scale: 35 %
      :alt: Medals

2.Medal Records
===============
   Medal Records table is on the middle of this part. It is directly connected both Medals and Front-Runner tables.
   Medal Records table shows the high score of a competition.

   .. figure:: mhb/Mr1.png
      :scale: 35 %
      :alt: Medals

   There are 3 attributes of Medal Records table.
   Best Score ID: An integer attribute which generates automatically and is related to Front-Runner table.
   Best Score(Minutes): A float attribute which cannot be empty.
   Competition ID: An integer attribute which is unique and related to Medal table.

2.1 Add function of Medal Records
---------------------------------

   If a user wants to add a data to the table, s/he must click 'Add New Best Score' button which is holding on the table.

   .. figure:: mhb/Mr1.png
      :scale: 35 %
      :alt: Medals

   When it is clicked to the button, a form will be seen.

   .. figure:: mhb/Mr2.png
      :scale: 35 %
      :alt: Medals

   The user writes the data in the boxes and click 'Save' button to add the record the table and the database via this form.

   .. figure:: mhb/Mr3.png
      :scale: 35 %
      :alt: Medals

   If 'Competition ID' attribute does not match a record in the Medals table, an error message will occur and the addition cannot be completed.

   .. figure:: mhb/Mr4.png
      :scale: 35 %
      :alt: Medals

   If a 'Competition ID' value is already exist, an error message will occur and the addition cannot be completed.

   .. figure:: mhb/Mr4.png
      :scale: 35 %
      :alt: Medals

   If the user does not write a data to 'Best Score', the record will not added to the table and the database.

2.2 Delete function of Medal Records
------------------------------------

   If a user wants to delete a data from the table, s/he must click the 'Delete' button which is holding right of the table.

   .. figure:: mhb/Mr5.png
      :scale: 35 %
      :alt: Medals

   When it is clicked to the button, the data will delete from the table and the database.

   .. figure:: mhb/Mr6.png
      :scale: 35 %
      :alt: Medals

   If 'Best Score ID' attribute matches a record in the Front-Runner table, an error message will occur and the deletion cannot be completed.

   .. figure:: mhb/Mr7.png
      :scale: 35 %
      :alt: Medals

2.3 Update function of Medal Records
------------------------------------

   If a user update a record, s/he must click the 'Update' button which is the last element of the table.

   .. figure:: mhb/Mr8.png
      :scale: 35 %
      :alt: Medals

   When it is clicked to the button, a new page will be appear which have a box and the old best record value.

   .. figure:: mhb/Mr9.png
      :scale: 35 %
      :alt: Medals

   The user changes the data in the boxes and click 'Save' button to update the record the table and the database via this page.

   .. figure:: mhb/Mr10.png
      :scale: 35 %
      :alt: Medals

   If the user erase the value and click 'Save' button, the value will stay the same old value.

3.Front-Runner
==============
   Front-Runner table is the undermost part. It is directly connected both Medal Records table.
   Medal Records table shows the name and the age of a winner of a competition.

   .. figure:: mhb/Fr1.png
      :scale: 35 %
      :alt: Medals

   There are 4 attributes of Medal Records table.
   Name ID: An integer attribute which generates automatically.
   Name: A varchar attribute.
   Age: An integer attribute.
   Best Score ID: An integer attribute which is related to Medal Records table.

3.1 Add function of Front-Runner
--------------------------------

   If a user wants to add a data to the table, s/he must click 'Add Front-Runner Name' button which is holding on the table.

   .. figure:: mhb/Fr1.png
      :scale: 35 %
      :alt: Medals

   When it is clicked to the button, a form will be seen.

    .. figure:: mhb/Fr2.png
      :scale: 35 %
      :alt: Medals

   The user writes the data in the boxes and click 'Save' button to add the record the table and the database via this form.

    .. figure:: mhb/Fr3.png
      :scale: 35 %
      :alt: Medals

   If 'Best Score ID' attribute does not match a record in the Medal Records table, an error message will occur and the addition cannot be completed.

   If the user does not write a data to 'Name', the record will not added to the table and the database.

3.2 Delete function of Front-Runner
-----------------------------------

   If a user wants to delete a data from the table, s/he must click the 'Delete' button which is holding right of the table.

   .. figure:: mhb/Fr3.png
      :scale: 35 %
      :alt: Medals

   When it is clicked to the button, the data will delete from the table and the database.

   .. figure:: mhb/Fr4.png
      :scale: 35 %
      :alt: Medals

3.3 Update function of Front-Runner
-----------------------------------

   If a user wants update a record, s/he must click the 'Update' button which is the last element of the table.

   .. figure:: mhb/Fr4.png
      :scale: 35 %
      :alt: Medals

   When it is clicked to the button, a new page will be appear which have boxes and the old values of the record.

   .. figure:: mhb/Fr5.png
      :scale: 35 %
      :alt: Medals

   The user changes the data in the boxes and click 'Save' button to update the record the table and the database via this page.

   .. figure:: mhb/Fr6.png
      :scale: 35 %
      :alt: Medals

Search function
===============

   There is a text box on the tables which implement searching.

   .. figure:: mhb/Fr7.png
      :scale: 35 %
      :alt: Medals

   If a user wants search a word in Medals and Front-Runner tables, the word or some part of that word must be written in the box.
   After that when it is clicked to the button, Medals and Front-Runner tables will show just the wanted records.

   .. figure:: mhb/Fr8.png
      :scale: 35 %
      :alt: Medals



