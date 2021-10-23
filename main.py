import pyaudio
from tkinter import*
import speech_recognition as sr
# import symbols list from local directory
from symbols import*
Titile_of_project = "Speech To Text with GUI"
saved_text_file = r".\saved_text.txt"

try:
    icon_path = "./favicon.ico"
except:
    print('Favicon is missing!!')

myFont = "Courier"
buttonFont = "Helvetica"
myFontSize = 12

energy_threshold = 1000
sample_rate = 44100
chunk_size = 512


def replace_symbol(txt):
    # create a duplicate array
    mtxt = txt.split(" ")
    for word in mtxt:
        for key in symbol.keys():
            # compare spoken word and symbol data set
            if(word.lower() == key):
                # replace word with symbol
                mtxt[mtxt.index(word)] = symbol[key]
                pass
            
    return " ".join(mtxt)


def s2t():
    try:
        fi_le = open(saved_text_file, "a+", encoding="utf-8")
    except FileNotFoundError:
        fi_le = open(saved_text_file, "w+", encoding="utf-8")

    r = sr.Recognizer()
    r.energy_threshold = energy_threshold
    # amplitude level to pick up
    with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:
        # listen for 1 second to calibrate the energy threshold for ambient noise levels
        r.adjust_for_ambient_noise(source)
        print('Say Something!')
        audio = r.listen(source)
    # print('Done!')
        try:
            text = r.recognize_google(audio, language="en-IN")
            text = replace_symbol(text)
            print('You said : {} '.format(text))
            fi_le.write(text+'\n')
            fi_le.close()
            return text
        except:
            print("Speech is untangable")
            return None


''' --------------------- GUI ---------------------'''
speaker_output = ""
try:
    save_txt = open(saved_text_file, "r", encoding='utf-8')
    speaker_output = save_txt.read()
# print(speaker_output)
    save_txt.close()
except FileNotFoundError:
    fi_le = open(saved_text_file, "w+", encoding="utf-8")


class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self)
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview
                              )
        self.scrollable_frame = Frame(canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")
                                       )
        )
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


def help_frame(option):
    frame = Toplevel()
    frame.title(Titile_of_project)
    try:
        frame.iconbitmap(icon_path)
    except:
        print('Favicon is missing!!')
    frame.geometry("720x480")
    if option == 'help':
        # Create Main Frame for help
        defaultFrame = Frame(frame)
        defaultFrame.pack(fill="both", expand=True, padx=1, pady=1)
        # Create Inner Widgets
        TopFrame = LabelFrame(defaultFrame, bd=2, width=480, height=300, padx=50,
                              pady=50, relief=RIDGE, bg="#666666", fg="#ffffff", text="Help")
        TopFrame.pack(fill="both", expand=True)
        helpText = Label(TopFrame, bg="#666666", fg="#ffffff",
                         font=(myFont, myFontSize), text="myHelp")
        helpText.pack(fill="both", expand=True, padx=5, pady=5)
    if option == 'about':
        # Create Main Frame for about
        defaultFrame = Frame(frame)
        defaultFrame.pack(fill="both", expand=True, padx=1, pady=1)
        # Create Inner Widgets
        TopFrame = LabelFrame(defaultFrame, bd=2, width=480, height=300, padx=50,
                              pady=50, relief=RIDGE, bg="#7280ab", fg="#ffffff", text="About")
        TopFrame.pack(fill="both", expand=True)
        aboutText = Label(TopFrame, fg="#ffffff", bg="#7280ab",
                          font=(myFont, myFontSize), text="myAbout")
        aboutText.pack(fill="both", expand=True, padx=5, pady=5)


def recordFunction():
    global speaker_output
    try:
        for widget in DisplayFrame.winfo_children():  # clear the frame
            widget.destroy()
    except:
        pass
    speaker_output += '\n'
    speaker_output += str(s2t())
    # capture and show text
    textFrame = LabelFrame(DisplayFrame, font=(
        myFont, myFontSize), text="Conversion Output")
    textFrame.pack(fill="both", expand=True)
    showText = ScrollableFrame(textFrame)
    Text = Label(showText.scrollable_frame, padx=10, pady=5,
                 justify=LEFT, font=(myFont, myFontSize), text=speaker_output)
    Text.pack(fill="both", expand=True)
    showText.pack(fill="both", expand=True)


if __name__ == '__main__':
    # initialisation of tkinter
    root = Tk()
    root.title(Titile_of_project)
    try:
        root.iconbitmap(icon_path)
    except:
        print('Favicon is missing!!')
    root.geometry("720x520")
    ''' Menu Options '''
    menubar = Menu(root)
    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="Help Index",
                          command=lambda: help_frame('help'))
    help_menu.add_command(
        label="About...", command=lambda: help_frame('about'))
    help_menu.add_separator()
    help_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Help", menu=help_menu)
''' --------------------- Creating the frame --------------------- '''
# Create Base Frame
defaultFrame = Frame(root)
defaultFrame.pack(fill="both", expand=True, padx=5, pady=5)
# Create Inner Widgets
TopFrame = Frame(defaultFrame, bd=2, width=480, height=300,
                 padx=10, pady=10, relief=RIDGE, bg="light grey")
TopFrame.pack(fill="both", expand=True)

# Create Main Frame
MainFrame = Frame(TopFrame)
MainFrame.pack(fill="both", expand=True)
# Create Inner Widgets
DisplayFrame = Frame(MainFrame, bd=5, width=720, height=360,
                     padx=2, relief=RIDGE, bg="cadet blue")
DisplayFrame.pack(fill="both", expand=True)
ButtonFrame = Frame(MainFrame, bd=5, width=720, height=80,
                    padx=2, relief=RIDGE, bg="#f0f0f0")
ButtonFrame.pack(fill="both", expand=True)
# Button
recordButton = Button(ButtonFrame, text="Record",
                      padx=20, pady=10, command=recordFunction, fg="#ffffff", bg="#006773", relief=RAISED, font=(buttonFont, 14, "bold"))
recordButton.pack(side=LEFT, padx=30, pady=10)
quitButton = Button(ButtonFrame, text="Quit",
                    padx=20, pady=10, command=root.quit,
                    fg="#ffffff", bg="#de1212", relief=RAISED, font=(buttonFont, 14, "bold"))
quitButton.pack(side=RIGHT, padx=30, pady=10)

root.config(menu=menubar)
root.mainloop()
