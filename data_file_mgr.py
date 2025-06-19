import datetime

def initiate_file():
    content = ""
    with open("temp.txt", 'r') as file:
        content = file.read()
    if(not content.startswith('dates,temperature')):
        with open("temp.txt", 'w') as file:
            file.write("dates,temperature\n")
        return True
    else:
        return False

def save_to_file(new_time, new_temp):
    with open("temp.txt", 'a') as file:
        file.write(f"{new_time},{new_temp}\n")