import tkinter
from tkinter import messagebox, filedialog
from googletrans import Translator, LANGCODES
import pyttsx3

# Initiate the Translator from googletrans
translator = Translator(service_urls=["translate.googleapis.com"])

# Function to select a file
def select_file():
    
    root1 = tkinter.Tk()
    root1.withdraw()
    # create tkinter window and hide it

    go=messagebox.askokcancel("File Selection", "Please select the file you "
"want to convert into .mp3")
    # prompt message to select file to convert
    
    if go==False:
        exit(1)
    # handle the user clicking on the cancel button
                           
    # show an "Open" dialog box and return the path to the selected file
    file_path = filedialog.askopenfilename()
    root1.destroy()

    if file_path == "" or file_path==False:
        # if user cancels the file explorer, exit the program
        exit(1)
        
    root1.mainloop()
    
    return file_path

# Function to handle wrong file type
def select_file_type():
    
    def cancel():  # Function for the cancel button
        root.destroy()
        return exit(1)
    
    while True:
        
        # Use the select_file function to select a file
        file_path = select_file()      

        file_type = file_path.split(".")[-1]  # Get the file type
        
        # ask user if they want to select another file
        if file_type not in ("pdf","pptx","docx","txt"):
            root=tkinter.Tk()
            root.withdraw()
            messagebox.showwarning("File Type Error",f"This program does not handle .{file_type} files."
                "  Please select another file?")
            
            root.protocol('WM_DELETE_WINDOW', cancel)
            # Override X button of tkinter window
            
            root.destroy()
            
            # Choose another file
            continue 
                
        break
    
    return file_path
    
# Function to select the output path to a folder    
def select_outpath():
    
    root1 = tkinter.Tk()
    root1.withdraw()
    # create tkinter window and hide it

    go=messagebox.askokcancel("Output Path Selection", "Please select "
"the folder in which you want the .mp3 file to be created.")
    # prompt message to select output path
    
    if go==False:
        exit(1)
    # handle the user clicking on the cancel button
                           
    # show an "Open" dialog box and return the path to the selected folder
    file_output = filedialog.askdirectory()
    root1.destroy()

    if file_output == "" or file_output==False:
        # if user cancels the file explorer, exit the program
        exit(1)
        
    root1.mainloop()
    print(file_output)
    return file_output


# Function to select the right voice
def select_voice():
    global voice_picked
    # Make sure to use the global variable in this function
    
    # Declare a few functions -----------------------------------------
    
    def take_selection():  # Function to get the value of the option menu
        global voice_picked
        # Still make sure to modify the global variable in this function
        voice_picked = value_inside.get()
        root.destroy()
    
    def cancel():  # Function for the cancel button
        root.destroy()
        return exit(1)

    # -----------------------------------------------------------------
    
    engine = pyttsx3.init()  # Initiate the pyttsx3 module
    
    # Get all the voices information ; name, id and language

    voices = []
    voice_ids = []
    voice_langs = []
    for voice in engine.getProperty("voices"):
        voices.append(voice.name)
        voice_ids.append(voice.id)
        voice_langs.append(voice.name.split("- ")[1])
    
    ### Create prompt to select the voice
    ### depending on the file language and preference of the user
    while True:
        # Create the default window
        root = tkinter.Tk()
        root.title("Select the Voice")
        root.eval("tk::PlaceWindow . center")
        
        # create the main sections of the layout,
        # and lay them out
        top = tkinter.Frame(root)
        bottom = tkinter.Frame(root)
        top.pack(side=tkinter.TOP)
        bottom.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)

        # Variable to keep track of the option
        # selected in OptionMenu
        value_inside = tkinter.StringVar(root)

        # Set the default value of the variable
        value_inside.set("Select a Voice")

        # Create the optionmenu widget and passing
        # the options_list and value_inside to it.
        question_menu = tkinter.OptionMenu(root, value_inside, *voices)
        question_menu.pack(in_=top)

        # Set "voice_picked" as the first voice in the list of voices
        voice_picked = voices[0]

        # Submit button
        # Whenever we click the submit button, our submitted
        # option is taken into the "voice_picked" global variable
        # This might be optimized to get rid of the global variable
        submit_button = tkinter.Button(
            root, text="Submit", width=10, height=2, command=take_selection
        )

        
        submit_button.pack(in_=bottom, side=tkinter.LEFT)
        if voice_picked not in voices:  # Deal with a user selecting "Select a Voice"
            continue
        cancel_button = tkinter.Button(
            root, text="Cancel", width=10, height=2, command=cancel
        )
        cancel_button.pack(in_=bottom, side=tkinter.RIGHT)
        # Create a cancel button

        root.protocol('WM_DELETE_WINDOW', cancel)
        # Override X button of tkinter window
        
        root.mainloop()

        index = voices.index(voice_picked)  # Find the index of the voice
        # Get the voice id attributed to that voice
        voice_id_picked = voice_ids[index]

        voice_name = voice_picked.split(" -")[0].split(" ")[1]
        
        # Set the voice to the one picked by the user
        engine.setProperty("voice", voice_id_picked)
        # Translate the text to the language the user picked
        to_speech = translator.translate(
            f"""Hi, my name is {voice_name}.  Let me talk to you, here is my voice.  Is this selection of voice fine with you?""",
            dest=LANGCODES[voice_langs[index].split(" ")[0].lower()],
        )

        engine.say(to_speech.text)  # Say the text
        engine.runAndWait()

        # Ask a question: Yes, No, or Cancel
        root2 = tkinter.Tk()
        root2.withdraw()

        # Confirm selection of voice
        result = messagebox.askyesnocancel(
            "Confirm Selection", f"Is this selection of voice ({voice_name}) fine with you?"
        )

        # Deal with the yes/no question

        root2.destroy()
        if result is True:
            break
        elif result is False:
            continue
        elif result is None:
            exit(1)
            
    return voice_id_picked
