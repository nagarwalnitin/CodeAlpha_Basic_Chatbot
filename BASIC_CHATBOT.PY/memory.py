def save_name(name):

    with open("memory.txt", "w") as file:
        file.write(name)


def get_name():

    try:
        with open("memory.txt", "r") as file:
            return file.read()

    except:
        return None