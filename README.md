CRUD

Adding functions 
List All info function:
- 






New Hero Func:
-Propt user for inputs bio, name, etc
- append to table of heroes
- Prompt for abilities 
    -if yes: 
        - diplay all abilites you can add to heroes
        - insert list of heroes sepearted by comma 
        - have a for loop that goes through each ability and executes and adds it to current hero selected 

add abilites func: function can be used on its own and is used if prompted in creating a new hero 
 - take two parameters: location to add and values





 Init:
 1: Prompt user for actions
    Available actions:
     1.) List all heroes
     2.) List all heroes and their abilities
     3.) Add new Hero
     4.) Delete hero 
     5.) Modify Hero 
        -Print all heros and select based on Id
        -user input: id(needs to be stored to plug into functions)
        -ask what you want to edit about the hero(name,bio,abilities etc)

SELECT * FROM heroes JOIN(abilities JOIN ability_types ON abilities.ability_type_id = ability_types.id ) ON 
