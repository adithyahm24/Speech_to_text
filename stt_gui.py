import tkinter as tk
import speech_recognition as sr


def speech_to_text(var):
    global q
    if var == 1:
        lang = 'en-in'
    elif var ==2:
        lang = 'kn-in'
    else:
        lang = 'en-in'

    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    with sr.Microphone() as source:

        audio = r.listen(source, timeout=6)

    try:
        print("recognizing")
        q = r.recognize_google(audio, language=lang)

        return q
    except Exception as e:
        print(e)


class Speech(tk.Tk):
    def __init__(self):
        super().__init__()
        self.text = ''
        self.img = None
        self._frame = tk.Frame(self)
        self._frame.pack()
        self.config(background="#01F3B3")
        self._frame.config(background="#01F3B3")

        l = tk.Label(self._frame, text="Speech Recognition", background='#F3D601')
        l.config(font=("Arial", 40, 'bold'))
        l.grid(row=0, column=0)
        tk.Label(self._frame,text = '',bg = '#01F3B3').grid(row = 1,column =0)
        self.var = tk.IntVar()
        r1 = tk.Radiobutton(self._frame, text="English", variable=self.var, value=1)
        r1.grid(row = 1,column = 0)
        r2 = tk.Radiobutton(self._frame, text="Kannada", variable=self.var, value=2)
        r2.grid(row=2, column=0)
        b1 = tk.Button(self._frame,
                       text="Recognize",
                       height=5,
                       width=60,
                       command=self.con,
                       bg='#FE831D')
        b1.grid(row=4, column=0)

    def con(self):
        self.text = speech_to_text(self.var.get())
        t = tk.Text(self._frame, width=100)
        t.config(font=("Arial", 15, 'bold'))
        t.insert(1.0, self.text )
        t.grid(row=5, column=0)


Speech().mainloop()
