# P2_Openclassrooms


Booktoscrape est un programme permettant de récolter les données du site web :
https://books.toscrape.com/

#Etape n°1 : Créer votre environnement virtuel.
Pour cela positionner l'invitation de commande à l'endroit où vous souhaitez lancer le programme, 
puis lancer la commande : py -m venv (nom de l'environnement). 


#Etape n°2 : Activer votre envrionnement virtuel.
Si votre invitation de commande est : 

bash/zsh l'éxécution se fera par la commande -> source (nom de l'environnement)/bin/activate

fish l'éxécution se fera par la commande -> source (nom de l'environnement)/bin/activate.fish

csh/tcsh l'éxécution se fera par la commande -> source (nom de l'environnement)/bin/activate.csh

PowerShell Core l'éxécution se fera par la commande -> source (nom de l'environnement)/Scripts/activate

cmd.exe l'éxécution se fera par la commande -> C:\\(nom de l'environnement)\\Scripts\\activate.bat

PowerShell l'éxécution se fera par la commande -> PS C:\\> (nom de l'environnement)\\Scripts\\Activate.ps1



#Etape n°3: Télécharger les packages nécéssaires.
vous pouvez retrouver l'ensemble des packages dans le "requierement.txt"

ou 

éxécuter les commandes suivantes:

pip install requests==2.25.1

pip install beautifulsoup4==4.9.3



#Etape n°4: Lancer le programme sur le terminal grâce au code : py booktoscrape.py



#Etape n°5 : Attendez que le programme récupère les données jusqu'à ce que le terminal affiche 
	le message suivant : l'extraction de donnée s'est déroulé avec succès !
	
	

#Etape n°6 : Deux nouveaux dossiers se sont crées à l'emplacement du fichier booktoscrape.py

-> Data : pour les données de chaques livres triées en fonction de leur catégorie

-> pictureData : pour les premières de couverture de tous les livres sous format .png


/!\ Relancer le programme fera une mise à jour des données mais supprimera les informations qui ne
sont plus sur le site web

============================================================================================

Booktoscrape is a program to collect data from the website:
https://books.toscrape.com/

#Step #1: Create your virtual environment.

To do this, position the command invitation where you want to launch the program, 
then run the command: py -m venv (environment name).


#Step #2: Activate your virtual environment.

If your order invitation is:

bash/zsh the execution will be done by the command -> source (name of the environment)/bin/activate

fish execution will be done by the command -> source (environment name)/bin/activate.fish

csh/tcsh the execution will be done by the command -> source (environment name)/bin/activate.csh

PowerShell Core the execution will be done by the command -> source (name of the environment)/Scripts/activate

cmd.exe the execution will be done by the command -> C: (name of the environment) Scripts activate.bat

PowerShell the execution will be done by the command -> PS C: > (name of the environment) Scripts Activate.ps1


#Step 3: Download the required packages.
you can find all the packages in the "requierement.txt"

or 

Run the following commands:

pip install requests==2.25.1

pip install beautifulsoup4==4.9.3
cmd.exe the execution will be done by the command: C:  (name of the environment)  Scripts activate.bat

PowerShell the execution will be done by the command: PS C:  > (name of the environment)  Scripts Activate.ps1


#Step 4: Run the program on the terminal using the code: py booktoscrape.py


#Step #5: Wait for the program to retrieve the data until the terminal displays 
	the following message: l'extraction de donnée s'est déroulé avec succès !


#Step 6: Two new folders were created at the location of the file booktoscrape.py

-> Data: for data of each book sorted according to their category

-> pictureData: for the front page of all books in .png format

/!\ Relaunch the program will update the data but will delete the information that are 
no longer on the website
