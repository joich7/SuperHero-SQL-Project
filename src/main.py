from database.db_connection import execute_query,create_connection



def listallInfo():

    basic_info_query = """
        SELECT id,name FROM heroes
    """
    abilities_query = f"""
        SELECT hero_id, name 
        FROM abilities 
        JOIN ability_types 
        ON abilities.ability_type_id = ability_types.id
    """
    basic_info = execute_query(basic_info_query).fetchall()
    abilities = execute_query(abilities_query).fetchall()
    for hero in basic_info:
        ability = []
        for x in abilities:
            
            if x[0] == hero[0]:
                ability.append(x[1])
        print(f"{hero[0]} {hero[1]} {ability}")

def getInfo():
    listnames()
    selector = input("who would you like to know more about?")
    names = execute_query(f"SELECT name,about_me FROM heroes WHERE id = {selector}")
    for i in names:
        print(i)



def newHero():
    name = input("Enter new hero name")
    about = input(f"Enter {name}'s about me text.")
    biography = input(f"Enter {name}'s biography ")
    quer = """
    INSERT INTO heroes (name,about_me,biography)
    VALUES(%s,%s,%s)
    """
    execute_query(quer,(name,about,biography))

    input()



run = True


#while run:
#    newHero()


def listnames():
    query = """
        SELECT id,name FROM heroes
    """
    returned_items = execute_query(query).fetchall()
    for i in returned_items:
        print(f"{i[0]}) {i[1]}")


def updateName(id):
    name = input("what would you like to change about this hero 1) name 2)abilities 3)")
    
    
    quer = f"""
    INSERT INTO heroes (name,about_me,biography)
    VALUES(%s,)
    """
    execute_query(quer,(name,about,biography))




def prompt():
    option = int(input("What would you like to do?"))
    
    if option == 1:
        yee()
