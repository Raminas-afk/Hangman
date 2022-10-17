from tkinter import *
from spejimai import *
from instrukcija import *
import sqlite3

# Pagrindinis langas

root = Tk()
root.resizable(False, False)
root.title('Kartuvės')
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.config(bg="white")

# SQLite

conn = sqlite3.connect("rezultatai.db")
c = conn.cursor()

# Boolean kuris padeda atskirti ar bus spėjamas sekantis žodis, ar pradedamas naujas žaidimas

naujas_zaidimas = False

# Kitos funkcijos

spejimai = Spejimai()


def atnaujinti_bandymu_langa():
    bandymu_langas.config(text=f"Liko bandymų:{spejimai.bandymai}")


def atnaujinti_tasku_langa():
    tasku_langas.config(text=f"Taškai: {spejimai.taskai}")


def atnaujinti_pranesimu_langa(spejimas=None):
    for raide in range(len(spejimai.spejamas_zodis)):
        if spejimai.spejamas_zodis[raide] == spejimas:
            pranesimu_langas.config(text=f"Atspėjai! raidė '{spejimas}' yra šiame žodyje.")
            break
    else:
        pranesimu_langas.config(text=f"Neatspėjai! Raidės '{spejimas}' nėra šiame žodyje.")

    if spejimai.spejamas_zodis == spejimai.nematomas_zodis and spejimai.zodis == 3:
        pranesimu_langas.config(text="Žodis atspėtas! Žaidimas baigtas.")
    elif spejimai.spejamas_zodis == spejimai.nematomas_zodis:
        pranesimu_langas.config(text="Žodis atspėtas!")
    elif spejimai.bandymai == 0 and spejimai.zodis == 3:
        pranesimu_langas.config(text="Žodis neatspėtas! Žaidimas baigtas.")
    elif spejimai.bandymai == 0:
        pranesimu_langas.config(text="Žodis neatspėtas!")

    if naujas_zaidimas:
        if spejimai.zodis == 1:
            pranesimu_langas.config(text="Turite 6 bandymus atspėti pirmąjį žodį. Sėkmės !")
        elif spejimai.zodis == 2:
            pranesimu_langas.config(text="Turite 6 bandymus atspėti antrąjį žodį. Sėkmės !")
        elif spejimai.zodis == 3:
            pranesimu_langas.config(text="Turite 6 bandymus atspėti trečiąjį žodį. Sėkmės !")


def atnaujinti_nematoma_zody(spejimas=None):
    for raide in range(len(spejimai.spejamas_zodis)):
        if spejimai.spejamas_zodis[raide] == spejimas:
            spejimai.nematomas_zodis = spejimai.nematomas_zodis[:raide] + spejimai.spejamas_zodis[raide] + \
                                       spejimai.nematomas_zodis[raide + 1:]
    teksto_langas2.config(text=spejimai.nematomas_zodis)
    if spejimai.bandymai == 0:
        teksto_langas2.config(text=spejimai.spejamas_zodis)



def pradeti_nauja_zaidima():
    global naujas_zaidimas
    naujas_zaidimas = True

    if spejimai.sunkumas == "Lengvas":
        spejimai.spejamas_zodis = random.choice(lengvu_zodziu_sarasas)
    elif spejimai.sunkumas == "Vidutinis":
        spejimai.spejamas_zodis = random.choice(vidutiniu_zodziu_sarasas)
    elif spejimai.sunkumas == "Sunkus":
        spejimai.spejamas_zodis = random.choice(sunkiu_zodziu_sarasas)

    spejimai.nematomas_zodis = "−" * len(spejimai.spejamas_zodis)
    spejimai.bandymai = 6
    if spejimai.zodis == 1:
        spejimai.taskai = 0
    atnaujinti_nematoma_zody()
    atnaujinti_pranesimu_langa()
    atnaujinti_bandymu_langa()
    yjungti_visus_mygtukus()
    paslepti_zaidimo_mygtuka()
    atnaujinti_kartuviu_nuotrauka()
    atnaujinti_tasku_langa()
    naujas_zaidimas = False


def atnaujinti_kartuviu_nuotrauka():
    if spejimai.bandymai == 5:
        label1.pack_forget()
        label2.pack()
    elif spejimai.bandymai == 4:
        label2.pack_forget()
        label3.pack()
    elif spejimai.bandymai == 3:
        label3.pack_forget()
        label4.pack()
    elif spejimai.bandymai == 2:
        label4.pack_forget()
        label5.pack()
    elif spejimai.bandymai == 1:
        label5.pack_forget()
        label6.pack()
    else:
        label6.pack_forget()
        label7.pack()
    if naujas_zaidimas:
        for w in nuotraukos_frame.winfo_children():
            w.pack_forget()
        label1.pack()
        rezultato_frame.place_forget()  # Panaikinamas rezultato įrašymo mygtukas pradedant naują žaidimą.


def pergales_nuotrauka():
    for w in nuotraukos_frame.winfo_children():
        w.pack_forget()
        label8.pack()


def isjungti_spejamus_mygtukus(spejimas):
    if spejimas == "A":
        a_button["state"] = DISABLED
    elif spejimas == "Ą":
        a2_button["state"] = DISABLED
    elif spejimas == "B":
        b_button["state"] = DISABLED
    elif spejimas == "C":
        c_button["state"] = DISABLED
    elif spejimas == "Č":
        c2_button["state"] = DISABLED
    elif spejimas == "D":
        d_button["state"] = DISABLED
    elif spejimas == "E":
        e_button["state"] = DISABLED
    elif spejimas == "Ę":
        e2_button["state"] = DISABLED
    elif spejimas == "Ė":
        e3_button["state"] = DISABLED
    elif spejimas == "F":
        f_button["state"] = DISABLED
    elif spejimas == "G":
        g_button["state"] = DISABLED
    elif spejimas == "H":
        h_button["state"] = DISABLED
    elif spejimas == "I":
        i_button["state"] = DISABLED
    elif spejimas == "Į":
        i2_button["state"] = DISABLED
    elif spejimas == "Y":
        y_button["state"] = DISABLED
    elif spejimas == "J":
        j_button["state"] = DISABLED
    elif spejimas == "K":
        k_button["state"] = DISABLED
    elif spejimas == "L":
        l_button["state"] = DISABLED
    elif spejimas == "M":
        m_button["state"] = DISABLED
    elif spejimas == "N":
        n_button["state"] = DISABLED
    elif spejimas == "O":
        o_button["state"] = DISABLED
    elif spejimas == "P":
        p_button["state"] = DISABLED
    elif spejimas == "R":
        r_button["state"] = DISABLED
    elif spejimas == "S":
        s_button["state"] = DISABLED
    elif spejimas == "Š":
        s2_button["state"] = DISABLED
    elif spejimas == "T":
        t_button["state"] = DISABLED
    elif spejimas == "U":
        u_button["state"] = DISABLED
    elif spejimas == "Ų":
        u2_button["state"] = DISABLED
    elif spejimas == "Ū":
        u3_button["state"] = DISABLED
    elif spejimas == "V":
        v_button["state"] = DISABLED
    elif spejimas == "Z":
        z_button["state"] = DISABLED
    elif spejimas == "Ž":
        z2_button["state"] = DISABLED


def yjungti_visus_mygtukus():
    for w in left_frame.winfo_children():
        w["state"] = ACTIVE


def isjungti_visus_mygtukus():
    for w in left_frame.winfo_children():
        w["state"] = DISABLED


def paslepti_zaidimo_mygtuka():
    naujas_zaidimas_button.grid_forget()
    naujas_zaidimas_frame.place_forget()


def rodyti_pasleptus_mygtukus():
    if spejimai.zodis < 3:
        naujas_zaidimas_frame.place(x=120, y=300)
        naujas_zaidimas_button.grid()
        naujas_zaidimas_button.config(text="Sekantis žodis")
    elif spejimai.zodis == 3:
        naujas_zaidimas_frame.place(x=50, y=300)
        rezultato_frame.place(x=150, y=300)
        naujas_zaidimas_button.grid()
        naujas_zaidimas_button.config(text="Naujas žaidimas")
        rezultato_button.grid()


def pakeisti_sunkuma(naujas_sunkumas):
    if naujas_sunkumas == "Lengvas":
        spejimai.sunkumas = "Lengvas"
    if naujas_sunkumas == "Vidutinis":
        spejimai.sunkumas = "Vidutinis"
    if naujas_sunkumas == "Sunkus":
        spejimai.sunkumas = "Sunkus"
    spejimai.zodis = 1
    sunkumo_langas.config(text=f"Sunkumas: {spejimai.sunkumas}")
    pradeti_nauja_zaidima()


def popup_instrukcija():
    naujas = Tk()
    naujas.geometry("350x200+600+340")
    naujas.title("Instrukcija")
    naujas.resizable(False, False)

    instrukcijos_langas = Label(naujas, text=instrukcija)
    instrukcijos_langas.pack()
    isjungti = Button(naujas, text="Gerai", command=naujas.destroy)
    isjungti.pack(side=TOP)


def popup_rezultatas():
    naujas = Tk()
    naujas.geometry("200x300+600+340")
    naujas.title("Rezultatai")
    naujas.resizable(False, False)
    #tekstas = Label(naujas, text="Top 10 rezultatai")
    #tekstas.place(x=1, y=1)
    rezultatu_db = c.execute('''SELECT * from rezultatai ORDER BY taskai DESC LIMIT 0,10''')
    i = 0

    for irasas in rezultatu_db:
        for x in range(len(irasas)):
            e = Label(naujas, width=10, fg='blue', text=irasas[x], anchor='w', )
            e.grid(row=i, column=x, padx=2)

        i = i + 1

    isjungti = Button(naujas, text="Gerai", command=naujas.destroy)
    isjungti.place(x=75, y=250)
    naujas.bind("<Return>", lambda event: naujas.destroy())


def rezultatas_vardas():
    naujas = Tk()
    naujas.title("Rezultatai")
    naujas.resizable(False, False)
    naujas.geometry("300x50+600+340")
    tekstas = Label(naujas, text="Įveskite savo vardą :")
    zaidejo_vardas = Entry(naujas)
    yrasyti = Button(naujas, text="Įrašyti", command=lambda: [yrasyti_rezultata(zaidejo_vardas), naujas.destroy()])
    atsakymas = Label(naujas, text="")
    naujas.bind("<Return>", lambda event: [yrasyti_rezultata(zaidejo_vardas), naujas.destroy()])
    tekstas.pack(side=LEFT)
    zaidejo_vardas.pack(side=LEFT)
    yrasyti.pack(side=LEFT)
    atsakymas.pack(side=BOTTOM)


def yrasyti_rezultata(zaidejo_vardas):
    vardas = zaidejo_vardas.get()
    with conn:
        c.execute(f"INSERT INTO Rezultatai VALUES ('{vardas}', '{spejimai.sunkumas}', {spejimai.taskai})")


def iseiti():
    root.quit()


# Meniu toolbaras

meniu = Menu(root)
root.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)
meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Naujas žodis", command=pradeti_nauja_zaidima)

sunkumo_meniu = Menu(submeniu, tearoff=0)
sunkumo_meniu.add_command(label="Lengvas", command=lambda: pakeisti_sunkuma("Lengvas"))
sunkumo_meniu.add_command(label="Vidutinis", command=lambda: pakeisti_sunkuma("Vidutinis"))
sunkumo_meniu.add_command(label="Sunkus", command=lambda: pakeisti_sunkuma("Sunkus"))
submeniu.add_cascade(label="Sunkumas", menu=sunkumo_meniu)
submeniu.add_command(label="Rezultatai", command=lambda: popup_rezultatas())
submeniu.add_command(label="Instrukcija", command=lambda: popup_instrukcija())

submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)

# Frames / Labels

left_frame = Frame(root, bg="white")
naujas_zaidimas_frame = Frame(root)
nuotraukos_frame = Frame(root, width=100, height=100)
rezultato_frame = Frame(root)

pranesimu_langas = Label(root, text="", font=20, bg="white")
teksto_langas2 = Label(root, text=spejimai.nematomas_zodis, font=20, bg="white")
sunkumo_langas = Label(root, text=f"Sunkumas: Lengvas", font=30, bg="white")
tasku_langas = Label(root, text="Taškai: 0", font=30, bg="white")
bandymu_langas = Label(root, text="", font=30, bg="white")

# Kartuviu progreso nuotraukos (Labels)

klaida1 = PhotoImage(file="Kartuviu progreso nuotraukos/1.png")
label1 = Label(nuotraukos_frame, image=klaida1)
label1.pack()

klaida2 = PhotoImage(file="Kartuviu progreso nuotraukos/2.png")
label2 = Label(nuotraukos_frame, image=klaida2)

klaida3 = PhotoImage(file="Kartuviu progreso nuotraukos/3.png")
label3 = Label(nuotraukos_frame, image=klaida3)

klaida4 = PhotoImage(file="Kartuviu progreso nuotraukos/4.png")
label4 = Label(nuotraukos_frame, image=klaida4)

klaida5 = PhotoImage(file="Kartuviu progreso nuotraukos/5.png")
label5 = Label(nuotraukos_frame, image=klaida5)

klaida6 = PhotoImage(file="Kartuviu progreso nuotraukos/6.png")
label6 = Label(nuotraukos_frame, image=klaida6)

klaida7 = PhotoImage(file="Kartuviu progreso nuotraukos/7.png")
label7 = Label(nuotraukos_frame, image=klaida7)

pergale = PhotoImage(file="Kartuviu progreso nuotraukos/8.png")
label8 = Label(nuotraukos_frame, image=pergale)

# Klaviatūros mygtukai

# Pirma eile
a_button = Button(left_frame, text="A", command=lambda: spejimai.tikrinti_spejima("A"), height=1, width=2)
a_button.grid(row=0, column=0)
a2_button = Button(left_frame, text="Ą", command=lambda: spejimai.tikrinti_spejima("Ą"), height=1, width=2)
a2_button.grid(row=0, column=1)
b_button = Button(left_frame, text="B", command=lambda: spejimai.tikrinti_spejima("B"), height=1, width=2)
b_button.grid(row=0, column=2)
c_button = Button(left_frame, text="C", command=lambda: spejimai.tikrinti_spejima("C"), height=1, width=2)
c_button.grid(row=0, column=3)
c2_button = Button(left_frame, text="Č", command=lambda: spejimai.tikrinti_spejima("Č"), height=1, width=2)
c2_button.grid(row=0, column=4)
d_button = Button(left_frame, text="D", command=lambda: spejimai.tikrinti_spejima("D"), height=1, width=2)
d_button.grid(row=0, column=5)
e_button = Button(left_frame, text="E", command=lambda: spejimai.tikrinti_spejima("E"), height=1, width=2)
e_button.grid(row=0, column=6)
e2_button = Button(left_frame, text="Ę", command=lambda: spejimai.tikrinti_spejima("Ę"), height=1, width=2)
e2_button.grid(row=0, column=7)
e3_button = Button(left_frame, text="Ė", command=lambda: spejimai.tikrinti_spejima("Ė"), height=1, width=2)
e3_button.grid(row=0, column=8)
f_button = Button(left_frame, text="F", command=lambda: spejimai.tikrinti_spejima("F"), height=1, width=2)
f_button.grid(row=0, column=9)
g_button = Button(left_frame, text="G", command=lambda: spejimai.tikrinti_spejima("G"), height=1, width=2)
g_button.grid(row=0, column=10)
# Antra eilė
h_button = Button(left_frame, text="H", command=lambda: spejimai.tikrinti_spejima("H"), height=1, width=2)
h_button.grid(row=1, column=0)
i_button = Button(left_frame, text="I", command=lambda: spejimai.tikrinti_spejima("I"), height=1, width=2)
i_button.grid(row=1, column=1)
i2_button = Button(left_frame, text="Į", command=lambda: spejimai.tikrinti_spejima("Į"), height=1, width=2)
i2_button.grid(row=1, column=2)
y_button = Button(left_frame, text="Y", command=lambda: spejimai.tikrinti_spejima("Y"), height=1, width=2)
y_button.grid(row=1, column=3)
j_button = Button(left_frame, text="J", command=lambda: spejimai.tikrinti_spejima("J"), height=1, width=2)
j_button.grid(row=1, column=4)
k_button = Button(left_frame, text="K", command=lambda: spejimai.tikrinti_spejima("K"), height=1, width=2)
k_button.grid(row=1, column=5)
l_button = Button(left_frame, text="L", command=lambda: spejimai.tikrinti_spejima("L"), height=1, width=2)
l_button.grid(row=1, column=6)
m_button = Button(left_frame, text="M", command=lambda: spejimai.tikrinti_spejima("M"), height=1, width=2)
m_button.grid(row=1, column=7)
n_button = Button(left_frame, text="N", command=lambda: spejimai.tikrinti_spejima("N"), height=1, width=2)
n_button.grid(row=1, column=8)
o_button = Button(left_frame, text="O", command=lambda: spejimai.tikrinti_spejima("O"), height=1, width=2)
o_button.grid(row=1, column=9)
p_button = Button(left_frame, text="P", command=lambda: spejimai.tikrinti_spejima("P"), height=1, width=2)
p_button.grid(row=1, column=10)
# Trečia eilė
r_button = Button(left_frame, text="R", command=lambda: spejimai.tikrinti_spejima("R"), height=1, width=2)
r_button.grid(row=2, column=0)
s_button = Button(left_frame, text="S", command=lambda: spejimai.tikrinti_spejima("S"), height=1, width=2)
s_button.grid(row=2, column=1)
s2_button = Button(left_frame, text="Š", command=lambda: spejimai.tikrinti_spejima("Š"), height=1, width=2)
s2_button.grid(row=2, column=2)
t_button = Button(left_frame, text="T", command=lambda: spejimai.tikrinti_spejima("T"), height=1, width=2)
t_button.grid(row=2, column=3)
u_button = Button(left_frame, text="U", command=lambda: spejimai.tikrinti_spejima("U"), height=1, width=2)
u_button.grid(row=2, column=4)
u2_button = Button(left_frame, text="Ų", command=lambda: spejimai.tikrinti_spejima("Ų"), height=1, width=2)
u2_button.grid(row=2, column=5)
u3_button = Button(left_frame, text="Ū", command=lambda: spejimai.tikrinti_spejima("Ū"), height=1, width=2)
u3_button.grid(row=2, column=6)
v_button = Button(left_frame, text="V", command=lambda: spejimai.tikrinti_spejima("V"), height=1, width=2)
v_button.grid(row=2, column=7)
z_button = Button(left_frame, text="Z", command=lambda: spejimai.tikrinti_spejima("Z"), height=1, width=2)
z_button.grid(row=2, column=8)
z2_button = Button(left_frame, text="Ž", command=lambda: spejimai.tikrinti_spejima("Ž"), height=1, width=2)
z2_button.grid(row=2, column=9)

# Kiti mygtukai

naujas_zaidimas_button = Button(naujas_zaidimas_frame, text="Sekantis žodis", command=pradeti_nauja_zaidima)
rezultato_button = Button(rezultato_frame, text="Išsaugoti rezultatą", command=rezultatas_vardas)

# Rėmelių placement

pranesimu_langas.pack(side=TOP, fill=X, expand=False)
teksto_langas2.place(x=120, y=130)
sunkumo_langas.place(x=380, y=355)
tasku_langas.place(x=20, y=355)
bandymu_langas.place(x=170, y=355)
left_frame.place(x=40, y=200)
nuotraukos_frame.place(x=360, y=50)

pradeti_nauja_zaidima()

root.mainloop()
