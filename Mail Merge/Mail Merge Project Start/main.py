#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

placeholder = "[name]"

with open(r"Mail Merge\Mail Merge Project Start\Input\Names\invited_names.txt") as names_File:
    names = names_File.readlines()
    
with open(r"Mail Merge\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_File:
    letter_Contents = letter_File.read()
    for name in names:
        stripped_Name = name.strip()
        new_Letter = letter_Contents.replace(placeholder, stripped_Name)
        with open(rf"Mail Merge\Mail Merge Project Start\Output\ReadyToSend\letter_for_{stripped_Name}", mode="w") as completed_Letter:
            completed_Letter.write(new_Letter)