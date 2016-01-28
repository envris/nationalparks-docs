Introduction
============

.. graphviz::

   digraph d {
      subgraph cluster_loggedin {
         label="logged in";
         menu;
	 scan_qr_when_logged_in;
	 scan_qr_when_logged_in -> manage_ticket;
         search_ticket;
         menu -> search_ticket;
         search_ticket -> search_results [label="keyword"];
	 search_ticket -> manage_ticket [label="GUID"];
         search_results -> manage_ticket;
      }
      subgraph cluster_not_loggedin {
         label="not logged in";
	 login;
	 scan_qr_when_not_logged_in -> view_ticket;
         view_ticket;
	 login_from_view_ticket;
	 view_ticket -> login_from_view_ticket;
      }
      login -> menu;
      login_from_view_ticket -> manage_ticket;
   }


.. graphviz::

   digraph d {
      menu_retail -> org_retail [label="single retail org"];
      menu_retail -> select_org_retail [label="multiple retail orgs"];
      menu_CTO -> org_CTO [label="single CTO org"];
      menu_CTO -> select_org_cto [label="multiple CTO orgs"];
      menu_org -> org_home;
      org_home -> org_CTO;
      org_home -> org_retail;
      select_org_cto;
      select_org_retail;
      select_org_cto_and_retail;
      login;
      login -> select_org_cto_and_retail [label="multiple orgs, cto + retail"];
      select_org_cto_and_retail ->  org_retail;
      select_org_cto_and_retail ->  org_CTO;
      login -> select_org_cto [label="multiple orgs, cto only"];
      select_org_cto ->  org_CTO;
      login -> select_org_retail [label="multiple orgs, retail only"];
      select_org_retail ->  org_retail;
      login -> org_retail [label="single org, retail only"];
      login -> org_CTO [label="single org, CTO only"];
      login -> org_home [label="single org, CTO and retail"];
   }

Parks Australia eTicketing system is a simple way for visitors to Kakadu National Park to purchase a park pass online, from retail shopfronts and through other partnerships such as Commercial Tour Operators.

It allows Independant Travelers to purchase tickets ahead of time, and modify tickets to suite their changing travel plans. It also allows Commercial Tour Operators to purchase tickets on a just-in-time basis to avoid the cost of keeping pre-purchased tickets in stock. It also allows retailers the same convenience, the ability to sell tickets without having to invest in stock.

This manual is for organisations that would like to be able to sell Kakadu National Parks eTickets, without having to carry inventory.


Register your organisation as an eTicket Reseller
-------------------------------------------------

If you organisation is not already Registered as a reseller, then contact Parks Australia. This only needs to be done once per organisation.

Parks Australia will create a record for your organisation in the system, and will set up one person as an administrator of that account. This administrator wil then be able to manage manage accounts for your organisation (including other administrator accounts). This can also be done over the counter at Parks Australia office or Visitor Center.

See also:
 * register your organisation as an eTicket Retailer 


Register a user account
-----------------------

This only needs to be done once per person.

Each person who can access the system needs to have an account. Rather than creating yet-another user name and password for you to remember, you can use a social media account such as Facebook, Twitter, Google or GitHub to log into the eTicketing system. If you are unable to use one of these services from your workplace, contact Parks for an alternative (local) account.

When Parks Australia first sets up an reseller organisation, they create an administrative account for someone in the organisation. This person (Admin Account) will be able to create, delete and modify user accounts for that organisation, including granting and revoking administrative priveleges to other users.


See also:
 * apply to join an organisation using your social media account
 * Retail Administrator: Create new accounts by sending an invitation
 * Retail Administrator: Approve a new account application
 * Retail Administrator: Grant and revoke priveleges to a user account
 * Retail Administrator: Remove users from your organisation 


Log into the Retail Portal
--------------------------

This needs to be done once per day, per Sales Agent (person selling eTickets on behalf of a Retail organisation).

This can be done at the beginning of the day or the first time a ticket sale is made.

If your organisation's administrators have set you up as a Sales Agent, then you will be able to sell tickets using a computer and printer in your store. This is similar to how Independant Travelers purchase tickets online, except:

 * You have to log in to the system to process the sale
 * You will recieve a Reseller Discount
 * You need to print a paper copy of the ticket and give it to the customer

In sumary, you:
 * select "new sale" button on the top of the main menu
 * select the park (only "Kakadu" available at this time).
 * enter the date of arrival at the park, either by hand or using a calendar widget
 * select the type and quantity of tickets required.
 * enter any other required and optional information for those tickets
 * click the "generate tickets" button
 * optionally, pay Parks Australia now (to streamline your activities at the checkout, it's also possible to charge the tickets to your organisation's account and pay for them at the end of the day)
 * charge your customer, print the PDF document on the next screen and give it to them.

See also:
 * how to:... TODO


Getting Help
------------

TODO: phone numbers, urls and email addresses for these...

 * 24/7 email/telephone helpdesk (technical difficulties)
 * 24/7 telephone helpdesk - assisted digital ticket sales
 * Business Hours: email/telephone/shopfront - register as CTO or Retailer
 * online user support forum

Feedback always welcome; Any user can make comments, raise issues or suggestions in our github account. That's also the best place to get support if you want to run your own version of the software (this is open source software).

