import random


class Rbac:
    def __init__(self, user, roles):
        self.users = user
        self.roles = roles
        self.current_user_id = 1000


class Role:
    def __init__(self, resource_name, action_type):
        self.resource_name = resource_name
        self.action_type = action_type


class User:
    def __init__(self, user_name, user_role):
        self.user_name = user_name
        self.user_role = user_role


class Action:

    def add_role(self, rbac):
        print("To add/update a role in RBAC need to provide role name, resource name and action type")
        role_name = input("Enter role name: ").strip()
        resource_name = input("Enter resource  name: ").strip()
        action_type = input("Enter action type: ").strip()
        resource = Role(resource_name, action_type)
        if rbac.roles.get(role_name, None) != None:
            rbac.roles[role_name].add(resource)
            print(role_name + " role has been updated")
        else:
            resources = []
            resources.append(resource)
            rbac.roles[role_name] = resources
            print("New Role " + role_name + " role has been added")

    def edit_user_role(self,rbac):
        self.view_users(rbac)
        user_id = int(input("Enter user id: "))
        while True:
            if rbac.users.get(user_id, None) is not None:
                print("Press 1 for add role")
                print("Press 2 for delete role")
                arg = int(input())
                if arg == 1:
                    role_name = input("Enter Role name that to be added: ")
                    role_name = role_name.split(",")
                    while True:
                        if self.check_role(rbac, role_name) == None:
                            role_name = input("Please enter valid role: ")
                            role_name = role_name.split(",")
                        else:
                            break

                    rbac.users.get(user_id).user_role.extend(role_name)
                    print("Role has been succesfully added")
                    return
                elif arg == 2:
                    role_name = input("Enter Role name that to be deleted: ")
                    role_name = role_name.split(",")
                    while True:
                        if self.check_role(rbac, role_name) == None:
                            role_name = input("Please enter valid role: ")
                            role_name = role_name.split(",")
                        else:
                            break

                    user_details = rbac.users.get(user_id)
                    if role_name[0] in user_details.user_role:
                        user_details.user_role.remove(role_name[0])

                        print("Role has been succesfully deleted")
                        return

                return
            else:
                user_id = int("Enter valid user id: ")

    def view_roles(self, rbac):
        print("List of Roles present in RBAC system: ")
        for role_name, resources in rbac.roles.items():
            print(role_name + ":", end="  ")
            for resource in resources:
                print("{" + resource.resource_name + ": " + resource.action_type + "}", end=" ")
            print("\n")

    def create_user(self, rbac):
        print("To add a user in RBAC, Please provide user name and role \n")
        print("Note: For multiple role assignation please add roles ',' seperated")
        user_name = input("Enter user name: ")
        user_role = input("Enter role: ")
        user_role = user_role.split(",")
        while True:
            if self.check_role(rbac, user_role) == None:
                user_role = input("Please enter valid roles: ")
                user_role = user_role.split(",")
            else:
                break

        user = User(user_name, user_role)
        while True:
            user_id = random.randint(1000, 9999)
            if user_id not in rbac.users.keys():
                rbac.users[user_id] = user
                print("user has been successfully added with this unique id: {}".format(user_id))
                break

    def check_role(self, rbac, role_name):
        for role in role_name:
            if role.lower().strip() != "admin" and rbac.roles.get(role.strip(), None) == None:
                print(role + " role does not exist.")
                return None
        return "exist"

    def view_users(self, rbac):
        print("List of all registered users in RBAC system: ")
        for user_id, user_details in rbac.users.items():
            print(str(user_id)+ ":", end="  ")
            print(user_details.user_name + ", {", end="")
            for role in user_details.user_role:
                print(role, end=" ")
            print("}")
            print("\n")

    def check_resource_access(self, rbac):
        resource_name = input("Please enter resource name: ").strip()
        user_details = rbac.users[rbac.current_user_id]
        user_roles = map(lambda x: x.lower(), user_details.user_role)
        if "admin" in user_roles:
            print("Admin has all rights to resources")
        else:
            for role in user_details.user_role:
                for resource in rbac.roles[role.strip()]:
                    if resource.resource_name.lower() == resource_name.lower().strip():
                        print("User has access to " + resource_name + " with " + resource.action_type + " rights")
                        return
            print("No access right to this resource")

    def log_in(self, rbac):
        user_id = int(input("Please enter User Id: ").strip())
        user_details = rbac.users.get(user_id, None)
        if  user_details == None:
            print("User does not exist")
            self.log_in(rbac)
        elif "Admin" in user_details.user_role:
            self.admin_switch(user_id, rbac)
        else:
            self.user_switch(user_id, rbac)


    def admin_switch(self, user_id, rbac):
        rbac.current_user_id = user_id
        print("\n")
        print("hi! you are logged in as admin")
        print("press 1 for login as another user")
        print("press 2 for create user")
        print("press 3 for add role")
        print("press 4 for view all roles")
        print("press 5 for edit user roles")
        arg = int(input())
        switcher = {1: self.log_in,
            2: self.create_user,
            3: self.add_role,
            4: self.view_roles,
            5: self.edit_user_role
        }
        fun = switcher.get(arg, None)
        if fun is not None:
            fun(rbac)
        self.admin_switch(user_id, rbac)


    def user_switch(self, user_id, rbac):
        rbac.current_user_id = user_id
        print("\n")
        print("hi! you are logged in as {}".format(rbac.users[user_id].user_name))
        print("press 1 for login as another user")
        print("press 2 for view roles")
        print("press 3 for access resource")
        arg = int(input())
        switcher = {1: self.log_in,
            2: self.view_roles,
            3: self.check_resource_access,
        }
        fun = switcher.get(arg, None)
        if fun is not None:
            fun(rbac)
        self.user_switch(user_id, rbac)

if __name__ == "__main__":
    user = User("admin", ["Admin"])
    user = {1000: user}
    roles = {}
    resources = []
    resource = Role("Email", "READ/WRITE")
    resources.append(resource)
    resource = Role("SAP", "READ/WRITE/DELETE")
    resources.append(resource)
    roles["Account Manager"] = resources
    resources1 = []
    resource = Role("UNIX", "READ/WRITE")
    resources1.append(resource)
    resource = Role("Directory", "READ/WRITE/DELETE")
    resources1.append(resource)
    roles["Software Developer"] = resources1
    rbac = Rbac(user, roles)
    print("Admin has been added in RBAC system with ID: 1000. So just Enter Admin id to login into the system.")
    print("Few Roles and Resources are already added in the system, below are the details.")
    # print(rbac.users)
    # print(rbac.roles)

    role = Action()
    role.view_roles(rbac)
    role.log_in(rbac)
    # role.view_roles(rbac)
    # role.view_users(rbac)
    # role.check_resource_access(rbac)
    # #role.add_role(rbac)
    # role.create_user(rbac)
    # role.check_resource_access(rbac)
    # role.add_role(rbac)
    # role.create_user(rbac)
    # role.check_resource_access(rbac)
    # role.view_roles(rbac)
    # role.view_users(rbac)











