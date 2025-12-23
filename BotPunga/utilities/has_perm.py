import discord

def has_perm(user, role_list):
    roles = [role.id for role in user.roles if role.name != "@everyone"]
    for permission in role_list:
        if permission in roles:
            return True
    
    return False
