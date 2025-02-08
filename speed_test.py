from tkinter import * 
from speedtest import Speedtest

def speed():
    sp = Speedtest()
    sp.get_servers()
    down = sp.download()
    up = sp.upload()
    download_speed = str(round(down / (10**6), 1)) + " Mbps"
    upload_speed = str(round(up / (10**6), 1)) + " Mbps"
    lab_down.config(text="Download Speed: " + download_speed)
    lab_up.config(text="Upload Speed: " + upload_speed)

# Create main window
sp = Tk()
sp.title("Speed Test")
sp.geometry("500x600")
sp.configure(bg="pink")

# Heading Label
Label(sp, text="Speed Test", font=("Arial Bold", 30, "bold"), bg="pink", fg="black").place(x=60, y=40, height=50, width=380)

# Download Speed Labels
Label(sp, text="Download Speed", font=("Arial Bold", 20, "bold"), bg="pink", fg="black").place(x=55, y=130, height=50, width=380)
lab_down = Label(sp, text="00", font=("Arial Bold", 20, "bold"), bg="pink", fg="black")
lab_down.place(x=55, y=200, height=50, width=380)

# Upload Speed Labels
Label(sp, text="Upload Speed", font=("Arial Bold", 20, "bold"), bg="pink", fg="black").place(x=55, y=290, height=50, width=380)
lab_up = Label(sp, text="00", font=("Arial Bold", 20, "bold"), bg="pink", fg="black")
lab_up.place(x=55, y=360, height=50, width=380)

# Start Button
Button(sp, text="Start", font=("Arial Bold", 20, "bold"), relief=RAISED, bg="black", fg="white", command=speed).place(x=200, y=450, height=50, width=100)

sp.mainloop()
