The Drop-down Menu
==================




menu_retail
^^^^^^^^^^^

menu item labelled "Retail". Present if user has Retail or Admin for 1 or more organisations


menu_cto
^^^^^^^^

menu item labelled "CTO". Present if user has Guide or Admin for 1 or more organisations


menu_search
^^^^^^^^^^^
menu item labelled "Search". Present if the user has Guide, SalesAgent or Admin for 1 or more organisations.



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
