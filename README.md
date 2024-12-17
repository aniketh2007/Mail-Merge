# Mail-Merge
- This project is to automate normal simple tasks which was developed based on the learnings of absolute and relative file path.
- In this project we can replace the [name] in the starting_letter.txt to the name list present in the name.txxt. And we generate specific letter to send via mail.
- The user can change the names in the name.txt if the user desires.
- Step 1 : We use the relative path method and open method to open the desired file in the file location  and along with with () method to pervent from manually type close() method to stop reading from the file and we use redlines() method to convert the names into a list of names.
- Step 2: Then open the file starting_letter.txt file and we loop thorugh the list of names and replace [name] with the names present in the list using replace() method. Then we use strip() method to remove the spaces and \n the new line when the list is created using readlines() method.
- Step 3 : To create customise letters. As by default in write method() if the file doesn't exist we can create new files. we use the f string to place the name for the file heading.
- 
