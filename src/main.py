from database.db_connection import execute_query



def listnames():

    names = execute_query("SELECT id,name FROM heroes")
    for i in names:
        print(i)

def getInfo():
    listnames()
    selector = input("who would you like to know more about?")
    names = execute_query(f"SELECT name,about_me FROM heroes WHERE id = {selector}")
    for i in names:
        print(i)

def newHero():
    name = input("Enter new hero name")

    Insert

def prompt():
    option = int(input("What would you like to do?"))
    
    if option == 1:
        yee()


run = True


while run:
    prompt()
