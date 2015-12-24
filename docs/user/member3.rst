############################################
User Guide of Parts Implemented by ANIL AĞCA
############################################


1.Pools Table and Operations
############################
   
1.1.Basic Contents
==================
Pools section of the main menu contains a table that has named as pools. Also this table works with olympics section and table.
For each pool, webpage's pools section contains 4 attributes: Pool id, pool name, city, area. And Four operations can be made on pools which are adding a new pool, deleting an existing pool, updating an existing pool and searching.
   
1.2.Operations on Pools
=======================

1.2.1.Adding a New Pool
-----------------------
To add a new pool, firstly Add Pool button that is under the main menu while in 'Pools Page' must be clicked. Then all four attributes which are pool id, pool name, city and area must be filled in order to add a new pool.
Also each pool id must be unique in order to keep integrity, it is not possible to add a new pool with an existing pool id.

   .. figure:: anl/addingpool.png
      :scale: 100 %
      :alt: Figure 1: Adding a New Pool

      *Figure 1: Adding a New Pool*

   
1.2.2.Deleting a Pool
---------------------
In order to delete a Pool, while in pools page, the button near the pool that wanted to be deleted must be ticked first. After that with clicking delete button deletion can be completed. The Pools which are being used by any olympics cannot be deleted. In such attempts an error message will pop.
      
   .. figure:: anl/deletingpool.png
      :scale: 100 %
      :alt: Figure 2: Deleting a Pool

      *Figure 2: Deleting a Pool*

 

1.2.3.Updating a Pool
---------------------
To update an existing pool, while in pools page in order to go to updating page, update pools button must be clicked.Then the update page will show up. In order to proceed the pool that wanted to be updated by the user must be ticked. And then new information about that pool must be entered by user to the form below the pools list. To update successfully all boxes must be filled correctly and also there must be no other pool with entered id currently. With updating a pool’s id, Also the Pool id section of the Olympics that uses that Pool id will be updated in such way, by reflecting the change on pools table to other tables, consistency of the web page is being established.

   .. figure:: anl/updatingpool.png
      :scale: 100 %
      :alt: Figure 3: Updating a Pool

      *Figure 3: Updating a Pool*

 
1.2.4.Searching a Pool
----------------------
In order to search user must click the ‘Search Pools’ button that is under the main menu at ‘Pools Page’. After a keyword must be entered into the box in the search page. Then simply by clicking Search button below list of results will be shown.

   .. figure:: anl/searchingpool.png
      :scale: 100 %
      :alt: Figure 4: Searching a Pool

      *Figure 4: Searching a Pool*

 



2.Sponsors Table and Operations
###############################

2.1.Basic contents
==================
Sponsors page can be reached by clicking ‘Sponsors’ in the main page. In the page appearing sponsors that currently being contained by web page can be seen. Each sponsor has three attributes which are id, sponsor name and starting year of sponsorship. In sponsors table four operations could be done by user which are adding a new sponsor, updating an existing sponsor, deleting a sponsor and Searching in sponsors. 

2.2.Operations on sponsors
==========================

2.2.1.Adding a New Sponsor
--------------------------
While in the ‘Sponsors’ A new sponsor can be added by firstly clicking Add New Sponsor button. Then on the add page all sponsor id, sponsor name and starting year must be filled in order to add successfully. In case of leaving blank space error messages return.Also it is not possible to add a sponsor with same id with another sponsor. In such cases error messages will return.

   .. figure:: anl/addingsponsor.png
      :scale: 100 %
      :alt: Figure 5: Adding a New Sponsor

      *Figure 5: Adding a New Sponsor*


2.2.2.Deleting a Sponsor
------------------------
While in the ‘Sponsors’ deletion operation is possible by ticking the box near the sponsor that wanted to be deleted. After ticking the box by clicking delete button at the bottom of the page operation can be completed. Deleting a sponsor that is being used in olympics currently is not possible. In case of such attempt error message pops.

   .. figure:: anl/deletingsponsor.png
      :scale: 100 %
      :alt: Figure 6: Deleting a Sponsor

      *Figure 6: Deleting a Sponsor*

2.2.3.Updating a Sponsor
------------------------
In order to update a sponsor first ‘Update Sponsor’ button at the ‘Sponsors’ page must be clicked. At the following page the box near the sponsor that is wanted to be updated must be ticked. After new sponsor id, sponsor name and starting year must be entered. Then by clicking update button update operation can be finalized. In case of updating a sponsor’s Id that is being refered by any olympics, all the olympics that consists that sponsor id will be also updated in order to keep consistency of program.

   .. figure:: anl/updatingsponsor.png
      :scale: 100 %
      :alt: Figure 7: Updating a Sponsor

      *Figure 7: Updating a Sponsor*


2.2.4.Search in Sponsors
------------------------
To search firstly ‘Search Sponsors’ button must be clicked on the ‘Sponsors Page’. Then by simply entering the keyword into the form and clicking the ‘Search button’ search operation can be done. The result will be shown on the following page.

   .. figure:: anl/searchingsponsor.png
      :scale: 100 %
      :alt: Figure 8: Searching in Sponsors

      *Figure 8: Searching in Sponsors*




3.Olympics
##########

3.1.Basic Contents
==================
Olympics page contains a table of olympics which contains full name, sponsor id, year and pool id for each Olympic. Full name of an Olympic contains the name of the Olympic, year of an Olympic is the year of that Olympic. Pool Id is id of the pool that Olympic is done which referees to ‘Pools’. Instead of entering pool name and year for each Olympic, entering the id number of the pool is enough. Pool must be added first in order to be referred by an Olympic. Olympics section capable of four operations which are adding new Olympic, deleting an Olympic, updating an Olympic and searching in all olympics.

3.2.Operations
==============

3.2.1.Adding New Olympic
------------------------
After going to olympics page by clicking Olympics Swimming, adding page can be reached by clicking Add New Olympic button from the sub-menu of Olympics page. Then at the next page form must be filled with necessary data. Full name and year of the Olympic that will be added must be entered normally. The pool and sponsor must be entered first at the pools and sponsors table if haven’t added before. Then the id given to the pool and sponsor must be entered into this form. In case of entered poolid doesn’t exist in pools table or sponsored doesn’t exist, error message will pop.

   .. figure:: anl/addingolympic.png
      :scale: 100 %
      :alt: Figure 9: Adding a New Olympic

   *Figure 9: Adding a New Olympic* 



3.2.2.Deleting an Olympic
-------------------------
On the olympics main page which can be reached by clicking the button ‘Olympics’ at main menu, deleting can be done by ticking the empty box near the Olympic that wanted to be deleted and then pressing the delete button at bottom of the page. The new table will be returned after deletion of the Olympic.

   .. figure:: anl/deletingolympic.png
      :scale: 100 %
      :alt: Figure 9: Deleting an Olympic

   *Figure 10: Deleting an Olympic* 


3.2.3.Updating an Olympic
-------------------------
In order to update an Olympic, after reaching to olympics page with clicking ‘Olympics Swimming’ at main menu the ‘Update Olympics’ button from the submenu must be clicked. On the following page, after choosing the olympics that wanted to be updated. New values for attributes must be entered to the following form. After form is filled by simply pressing update button, Update operation can be completed.
   
   .. figure:: anl/updatingolympic.png
         :scale: 100 %
         :alt: Figure 11: Updating an Olympic
   
   *Figure 11: Updating an Olympic* 


3.2.4 Searching Olympics
------------------------
Searching page can be reached by clicking the Search Olympics button on the Olympics page. Search operation can be made by entering the keyword into the form appeared and clicking at search button on the search page. Then Olympics named with the entered keyword will return to the screen.
   
   .. figure:: anl/searcingolympic.png
      :scale: 100 %
      :alt: Figure 12: Searching for an Olympic

*Figure 12: Searching for an Olympic * 


3.3.Error Messages at Olympics
==============================
Error messages shows in cases that violates application’s integrity and consistency. In Olympic Swimming page’s Add operation and Update operation in case of non-existing Poolid and/or Sponsorid being trying to add or updated as, an error message that informs user pops in user’s browser. Shape of the message box may vary on the browser type of user.

    
   
   .. figure:: anl/errormessages1.png
      :scale: 100 %
      :alt: Figure 13: Olympics invalid add/update operation’s error message. 

   *Figure 13: Olympics invalid add/update operation’s error message.* 

Also in case of trying to delete a pool or a sponsor that is currently being used at Olympics table, since that deletion will compromise programs integrity attempt will be ended with failure. And a error message will be shown to user.

   
   .. figure:: anl/errormessages2.png
      :scale: 100 %
      :alt: Figure 14: Unable to delete. 

   *Figure 14: Error message of program being unable to delete a sponsor/pool that is being used* 


