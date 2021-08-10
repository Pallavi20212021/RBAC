# RBAC
Assignment Bluestack


RBAC system is developed in Python 3. To run the project you must have python3.6 and above in your system.
First download the RBAC.py file and open CMD and run the command RBAC.py.

Admin has been added in RBAC system with ID: 1000. So just Enter Admin id to login into the system.
Few Roles and Resources are already added in the system, below are the details:

List of Roles present in RBAC system: 
Account Manager:  {Email: READ/WRITE} {SAP: READ/WRITE/DELETE}
Software Developer:  {UNIX: READ/WRITE} {Directory: READ/WRITE/DELETE}


Roles:Account Manager, Software Developer.
Resources: Email, SAP, UNIX, Directory  with Action Type.


Admin can perform below Roles:

press 1 for login as another user
press 2 for create user
press 3 for add role
press 4 for view all roles
press 5 for edit user roles


And Other User can perform 

press 1 for login as another user
press 2 for view roles
press 3 for access resource

Assumptions:
--> Login the sytem with user_id, as it has been generated 4 digit unique id for each user.
--> While creating a user, user name and role name details are required. It will add user only if role has already been in the system. 
--> First add a role in the system, there is an option to admin to add a role, then assign a role to user.
--> Edit User Role method, First it shows all the user details and there assigned roles. So admin can enter the user id and edit the users role by adding and deleting the roles.


Note: Please take care of case sensitive of names(It has been handled, but might be missed in some cases)
