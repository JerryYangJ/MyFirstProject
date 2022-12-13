
with open("Web/flask/templates/老王.txt", 'r', encoding='utf-8')as f:
    lines_list = f.readlines()
    user_name = lines_list[0]
    profile_info = ''.join(lines_list[1:])
print(user_name, profile_info)