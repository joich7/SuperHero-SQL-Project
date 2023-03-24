from database.db_connection import execute_query,create_connection

def listAbilities():
    abilities = execute_query("SELECT * FROM ability_types").fetchall()
    for ability in abilities:
        print(f"{ability[0]}) {ability[1]}")

def listallInfo():

    basic_info_query = """
        SELECT id,name FROM heroes
    """
    abilities_query = f"""
        SELECT *
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
        joinStr = " ".join(ability)
        print(f"""{hero[0]}) {hero[1]}

        Abilities: {joinStr}""")

def getInfo(x):
    info = execute_query(f"SELECT name,about_me FROM heroes WHERE id = {x}")
    for i in info:
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


end = False

def listnames():
    try:
        query = """
            SELECT id,name FROM heroes
        """
        returned_items = execute_query(query).fetchall()
        for i in returned_items:
            print(f"{i[0]}) {i[1]}")
    except:
        print("enter a valid hero number")


def updateHero(location):
    select = int(input("""what would you like to change about this hero 
    1) Name 
    2) About me 
    3) Biography
    4) Abilities \n"""))

    if select == 1:
        value = input("Input new Name: ")
        quer = """
        UPDATE heroes
        SET name = %s
        WHERE id = %s
        """
        execute_query(quer,(value,location,))
    elif select == 2:
        value = input("Input new about me info: ")
        quer = """
        UPDATE heroes
        SET about_me = %s
        WHERE id = %s
        """
        execute_query(quer,(value,location,))
    elif select == 3:
        value = input("Input new biography: ")
        quer = """
        UPDATE heroes
        SET biography = %s
        WHERE id = %s
        """
        execute_query(quer,(value,location,))
    elif select == 4:
        listAbilities()
        value = input("Input new abilities")
        splValue = value.split(",")
        print(splValue)
        for ability in splValue:
            quer = """
            INSERT into abilities (hero_id, ability_type_id)
            VALUES(%s,%s)
            """
            execute_query(quer, (location, ability))

        #quer = """
        #UPDATE abilities
        #SET ability_type_id = %s
        #WHERE hero_id = %s
        #"""

        #execute_query(quer,(value,location))
    
    


    #abilities
    #about info
    #bio
    #

#add new abilities function 
listallInfo()

while end:
    option = int(input("""What would you like to do? 
    1)list all charachters and abilities
    2)list specific heros abilities and info
    3)Make new hero 
    4)edit
    5)delete
    6)quit \n"""))
    
    if option == 6:
        end = False
    elif option == 1: #list all
        listnames()
        selector = input("who would you like to know more about?")
        getInfo(selector)
    
    elif option == 2: #list specific
        selector = input("who would you like to know more about?")
        getInfo(selector)
        
    elif option == 3: # Make new Hero
        newHero()

    elif option == 4: # Edit hero 
        listnames()
        selector = input("Which hero would you like to edit?")
        getInfo(selector)
        updateHero(selector)
  
