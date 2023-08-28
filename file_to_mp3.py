import tkinter
from tkinter import messagebox, filedialog
import pyttsx3
from PyPDF2 import PdfReader
from googletrans import Translator, LANGCODES
from pptx import Presentation
import docx
import docx2txt


engine = pyttsx3.init()  # Initiate the pyttsx3 module

# Initiate the Translator from googletrans
translator = Translator(service_urls=["translate.googleapis.com"])

# Get all the voices information ; name, id and language

voices = []
voice_ids = []
voice_langs = []
for voice in engine.getProperty("voices"):
    voices.append(voice.name)
    voice_ids.append(voice.id)
    voice_langs.append(voice.name.split("- ")[1])

root1 = tkinter.Tk()
# show an "Open" dialog box and return the path to the selected file
file_path = filedialog.askopenfilename()
root1.destroy()

if file_path == "":
    # if user cancels the file explorer, exit the program
    exit(1)

file_type = file_path.split(".")[1]  # Get the file type

# Get only the file name without the full path or the type
file_name = file_path.split("/")[-1].split(".")[0]

output_file_name = file_name + ".mp3"  # Create the mp3 output file name


# Function to take the selection of the user


def take_selection():  # Function to get the value of the option menu
    global voice_picked
    voice_picked = value_inside.get()
    root.destroy()
    return voice_picked


def cancel():  # Function for the cancel button
    root.destroy()
    return exit(1)


parts = []


# Function to ignore header and footer from pdf
def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 50 and y < 720:
        parts.append(text)


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
    # option is taken into the "voice_picked" variable
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
    root2.geometry("1x1+0+0")
    root2.eval("tk::PlaceWindow . center")

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


# End of inputs for file and voice
# -------------------------------------------------------------------
# Core job: File extraction and export into mp3

# PDF
if file_type == "pdf":
    text = ""

    reader = PdfReader(file_path)  # Read the select file
    count = len(reader.pages)  # Get the number of pages in the file

    for i in range(count):  # Iterate on the pages and add the text together
        page = reader.pages[i]
        page.extract_text(visitor_text=visitor_body)
        text += "".join(parts)

    # Clean the text to remove any newline
    clean_text = text.strip().replace("\n", " ")

    print(text, "\n\n", clean_text)

# PowerPoint
elif file_type == "pptx":
    # open pptx file
    f = open(f"{file_path}", "rb")
    prs = Presentation(f)

    text_runs = []

    # pptx reads in all text for detected shapes in powerpoint
    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    text_runs.append(run.text)

    # Join the text runs with "... " to get one text with long pauses
    text = "... ".join(text_runs)
    # Clean the text to remove any newline
    clean_text = text.strip().replace("\n", " ")

elif file_type == "docx":
    # open Word document
    doc = docx.Document(file_path)

    # read in each paragraph in file without borders
    text = [p.text for p in doc.paragraphs]
    long_text = ""
    for line in text:
        # Join the elements of the list with different conditions
        # If last letter is a period -> " "
        # If last letter is something else -> "... ""
        if len(line) > 0:
            if line[-1] != ".":
                long_text += line + "... "
            else:
                long_text += line + " "

    # Clean the text
    # Remove trailing and leading spaces
    # Replace newlines by space
    clean_text = long_text.strip().replace("\n", " ")

elif file_type == "txt":
    # Open the file and read each line
    f = open(file_path)
    text = f.readlines()
    long_text = ""
    for line in text:
        # Join the elements of the list with different conditions
        # If last letter is a period -> " "
        # If last letter is something else -> "... ""
        if len(line) > 0:
            if line[-1] != ".":
                long_text += line + "... "
            else:
                long_text += line + " "

    # Clean the text
    # Remove trailing and leading spaces
    # Replace newlines by space
    clean_text = long_text.strip().replace("\n", " ")

engine.save_to_file(clean_text, output_file_name)  # Save speech to file
engine.runAndWait()
engine.stop()
