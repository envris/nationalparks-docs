.. _logging-in:

Logging in
==========

Normaly, a user is a member of only one organisation, but it is
possible for them to be in more than one. A user can have different
roles in  organisations, such as Admin, Guide and Sales Agent.
There is more information about this in
:ref:`roles-and-responsabilities`.


Simple Case
-----------

The common situations are:
 * Admin for a single organisation
 * Guide for a single organisation
 * Sales Agent for a single organisation
 * Guide and Sales Agent for a single organisation

Depending on a user's role, they see a different page when they first log in.

+--------+-------+-------+------------+--------------------------------+
| action | Admin | Guide | SalesAgent | Page                           |
+========+=======+=======+============+================================+
| login  | 1     | 0     | 0          | Org Home                       |
+--------+-------+-------+------------+--------------------------------+
| login  | 0     | 1     | 1          | Org Home [#]_                  |
+--------+-------+-------+------------+--------------------------------+
| login  | 0     | 1     | 0          | CTO Home                       |
+--------+-------+-------+------------+--------------------------------+
| login  | 0     | 0     | 1          | Retail Home                    |
+--------+-------+-------+------------+--------------------------------+

.. [#] This assumes the user is Guide and Sales agent in the same organisation.

These login scenarios involve the following pages:

+---------------+--------------------+---------------------------------------------------------+
| page name     | example URL        | description                                             |
+===============+====================+=========================================================+
| login         | /accounts/login/   | The page where a user logs in.                          |
+---------------+--------------------+---------------------------------------------------------+
| CTO home      | /cto/123/          | Page about Tours (etc) for one organisation             |
+---------------+--------------------+---------------------------------------------------------+
| Retail Home   | /retail/123/       | FIT ticket order form (a lot like the public form)      |
+---------------+--------------------+---------------------------------------------------------+
| Org Home      | /org/123/          | Organisation Summary, links to Retail and CTO Homes     |
+---------------+--------------------+---------------------------------------------------------+


Unusual Cases - A member of multiple organisations
--------------------------------------------------

It's probably uncommon, but a user could have roles in different organisations.

For example:
 * Guide for multiple organisations
 * Sales Agent for multiple organisations
 * Admin for multiple organisations

In these situations, when a person logs in, they would have to chose
which organisation they want to act on behalf of. Then they would navigate
to the correct page.

+--------+-------+-------+------------+--------------------------------+
| action | Admin | Guide | SalesAgent | Page                           |
+========+=======+=======+============+================================+
| login  | 0     | 2+    | 0          | select CTO -> CTO Home         |
+--------+-------+-------+------------+--------------------------------+
| login  | 2+    | 0     | 0          | select Org -> Org Home         |
+--------+-------+-------+------------+--------------------------------+
| login  | 0     | 0     | 2+         | select Retail -> Retail Home   |
+--------+-------+-------+------------+--------------------------------+

Those unusual cases require aditional pages:

+---------------+--------------+---------------------------------------------------------+
| page name     | example URL  | description                                             |
+===============+==============+=========================================================+
| Select Org    | /org/        | List of organisation user is a member of                |
+---------------+--------------+---------------------------------------------------------+
| Select CTO    | /cto/        | List of organisations user is Guide or Admin of         |
+---------------+--------------+---------------------------------------------------------+
| Select Retail | /retail/     | List of organisations user is a Sales Agend or Admin of |
+---------------+--------------+---------------------------------------------------------+

It could be even more complicated. If a user is a Guide for one organisation
and a Sales agent for another, when they log in, they would need to chose
which organisation they are acting on behalf of. If they were a Guide and
Sales agent for the same organisation, they would not have to make that choice.

+--------+-------+-------+------------+--------------------------------------------+
| action | Admin | Guide | SalesAgent | Page                                       |
+========+=======+=======+============+============================================+
| login  | 0     | 1     | 1          | Org Home (if same org)                     |
+--------+-------+-------+------------+--------------------------------------------+
| login  | 0     | 1     | 1          | select Org (if different orgs) -> Org Home |
+--------+-------+-------+------------+--------------------------------------------+

In the more complicated combinations, the user would have to select the
organisation they are acting on behalf of when they log in.

+--------+-------+-------+------------+--------------------------------+
| action | Admin | Guide | SalesAgent | Page                           |
+========+=======+=======+============+================================+
| login  | 0+    | 2+    | 1+         | select Org -> Org Home         |
+--------+-------+-------+------------+--------------------------------+
| login  | 0+    | 1+    | 2+         | select Org -> Org Home         |
+--------+-------+-------+------------+--------------------------------+


Visualising the login logic
---------------------------

Overall, this diagram shows the different naviation paths from logging in.
It looks complicated because it covers all possible situations, however each
user would only experience one path based on their personal circumstances,
so it should not be a complicated experience for them.

.. graphviz::

   digraph d {
      node [style=filled fillcolor=white];

      login [label="Login"];
      cto_home [label="CTO Home"];
      select_cto [label="Select CTO" fillcolor=lightgrey];
      retail_home [label="Retail Home"];
      select_retail [label="Select Retail" fillcolor=lightgrey];
      org_home [label="Org Home"];
      select_org [label="Select Org" fillcolor=lightgrey];

      login -> cto_home;
      login -> select_cto -> cto_home;
      login -> org_home;
      login -> select_org -> org_home;
      login -> retail_home;
      login -> select_retail -> retail_home;
   }

