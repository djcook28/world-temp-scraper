import datetime

def initiate_file():
    content = ""
    with open("temp.txt", 'r') as file:
        content = file.read()
    if(not content.startswith('dates,temperature')):
        with open("temp.txt", 'w') as file:
            file.write("dates,temperature\n")

def save_to_file(temp):
    with open("temp.txt", 'a') as file:
        current_time = datetime.datetime.now()
        current_time = datetime.datetime.strftime(current_time, "%y-%m-%d-%H-%M-%S")
        file.write(f"{current_time},{temp}\n")