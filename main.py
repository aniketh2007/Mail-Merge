PlaceHolder= "[name]"
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
#Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name= name.strip()
        new_letter = letter_content.replace(PlaceHolder,stripped_name)
        # Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt","w") as completed_letters:
            completed_letters.write(new_letter)
            
        