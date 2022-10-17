from tkinter import *
from PirminesFunkcijos import *
spejimai = Spejimai()
def naujas_zaidimas():
    for w in nuotraukos_frame.winfo_children():
        w.pack_forget()
    rezultato_frame.place_forget()
    label1.pack()
    if spejimai.sunkumas == "Lengvas":
        spejimai.spejamas_zodis = random.choice(lengvu_zodziu_sarasas)
    elif spejimai.sunkumas == "Vidutinis":
        spejimai.spejamas_zodis = random.choice(vidutiniu_zodziu_sarasas)
    elif spejimai.sunkumas == "Sunkus":
        spejimai.spejamas_zodis = random.choice(sunkiu_zodziu_sarasas)

    spejimai.nematomas_zodis = "−" * len(spejimai.spejamas_zodis)
    spejimai.bandymai = 6
    if spejimai.zodis == 1:
        teksto_langas.config(text="Turi 6 bandymus atspėti pirmąjį žodį. Sėkmės !", font=20)
        spejimai.taskai = 0
    elif spejimai.zodis == 2:
        teksto_langas.config(text="Turi 6 bandymus atspėti antrąjį žodį. Sėkmės !", font=20)
    elif spejimai.zodis == 3:
        teksto_langas.config(text="Turi 6 bandymus atspėti trečiąjį žodį. Sėkmės !", font=20)

    teksto_langas2.config(text=spejimai.nematomas_zodis, font=20)
    sunkumo_langas.config(text=f"Sunkumas: {spejimai.sunkumas}", font=30, bg="white")
    bandymu_langas.config(text=f"Liko bandymų:{spejimai.bandymai}")
    yjungti_visus_mygtukus()
    paslepti_zaidimo_mygtuka()


def klaidos_nuotrauka():
    if spejimai.bandymai == 5:
        label1.pack_forget()
        label2.pack()
    if spejimai.bandymai == 4:
        label2.pack_forget()
        label3.pack()
    if spejimai.bandymai == 3:
        label3.pack_forget()
        label4.pack()
    if spejimai.bandymai == 2:
        label4.pack_forget()
        label5.pack()
    if spejimai.bandymai == 1:
        label5.pack_forget()
        label6.pack()
    if spejimai.bandymai == 0:
        label6.pack_forget()
        label7.pack()


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
    if spejimai.zodis == 3:
        naujas_zaidimas_frame.place(x=50, y=300)
        rezultato_frame.place(x=150, y=300)
        naujas_zaidimas_button.grid()
        naujas_zaidimas_button.config(text="Naujas žaidimas")
        rezultato_button.grid()


def sunkumas_lengvas():
    spejimai.sunkumas = "Lengvas"
    spejimai.taskai = 0
    spejimai.zodis = 1
    tasku_langas.config(text=f"Taškai: {spejimai.taskai}")
    naujas_zaidimas()


def sunkumas_vidutinis():
    spejimai.sunkumas = "Vidutinis"
    spejimai.taskai = 0
    spejimai.zodis = 1
    tasku_langas.config(text=f"Taškai: {spejimai.taskai}")
    naujas_zaidimas()


def sunkumas_sunkus():
    spejimai.sunkumas = "Sunkus"
    spejimai.taskai = 0
    spejimai.zodis = 1
    tasku_langas.config(text=f"Taškai: {spejimai.taskai}")
    naujas_zaidimas()


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

    rezultatu_db = c.execute('''SELECT * from rezultatai ORDER BY taskai DESC LIMIT 0,11''')
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
