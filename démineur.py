import random


champ = [[0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]]

tableau = [["☐","☐","☐","☐","☐","☐","☐","☐","☐","☐"],
["☐","☐","☐","☐","☐","☐","☐","☐","☐","☐"],
["☐","☐","☐","☐","☐","☐","☐","☐","☐","☐"],
["☐","☐","☐","☐","☐","☐","☐","☐","☐","☐"],
["☐","☐","☐","☐","☐","☐","☐","☐","☐","☐"],
["☐","☐","☐","☐","☐","☐","☐","☐","☐","☐"],
["☐","☐","☐","☐","☐","☐","☐","☐","☐","☐"],
["☐","☐","☐","☐","☐","☐","☐","☐","☐","☐"]]


def affichage(tableau):

  print("  0 1 2 3 4 5 6 7 8 9 ")
  for ligne in range(0,8):
    print(ligne, end=" ")
    for colonne in range(0,10):
      print(tableau[ligne][colonne], end=" ")
    print("")

gameOver = False

bombe = False

nbrBombes = 0

while bombe == False:

    for i in range(len(champ)):
        
        for j in range(len(champ[i])):

            champ[i][j] = random.randint(1,10)
            if(champ[i][j] == 4):
                champ[i][j] = "B"
                bombe = True
                nbrBombes += 1
            else:
                champ[i][j] = 0

nbrCases = len(champ)*len(champ[0]) - nbrBombes


while gameOver == False and nbrCases>0:

    affichage(tableau)
    ligne = int(input("choisir une ligne : "))
    colonne = int(input("choisir une colonne : "))

    if(colonne <(len(champ[0])) and ligne <(len(champ))):

      if(champ[ligne][colonne] == "B"):
          gameOver = True
          
          print("Perdu...")

      nbrBombesActuelles =0
      nbrCases -= 1
      
      if(colonne != 9):
          if(champ[ligne][colonne+1] == "B"):
              nbrBombesActuelles= nbrBombesActuelles+1
              
      if(colonne != 0):
          if(champ[ligne][colonne-1] == "B"):
              nbrBombesActuelles= nbrBombesActuelles+1
              

      if(ligne != 0):
          if(champ[ligne-1][colonne] == "B"):
              nbrBombesActuelles= nbrBombesActuelles+1
          
          if(colonne !=0):
              if(champ[ligne-1][colonne-1] == "B"):
                  inbrBombesActuelles= nbrBombesActuelles+1
              
          if(colonne != 9):
              if(champ[ligne-1][colonne] == "B"):
                  nbrBombesActuelles= nbrBombesActuelles+1

      if(ligne !=8):
          if(champ[ligne][colonne-1] == "B"):
              nbrBombesActuelles= nbrBombesActuelles+1

          if(colonne !=0):
              if(champ[ligne][colonne-1] == "B"):
                  inbrBombesActuelles= nbrBombesActuelles+1

          if(colonne != 8):
            if(champ[ligne][colonne] == "B"):
                  nbrBombesActuelles= nbrBombesActuelles+1


      tableau[ligne][colonne] = nbrBombesActuelles
if(gameOver == True):
    print("Perdu...")
else:
    print("Victoire !")
      
print("-")
affichage(champ)
print("-")