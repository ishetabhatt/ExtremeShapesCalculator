import tkinter as tk
import math

class ShapeCalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="lightblue")  # Set the desired background color

        self.root.title("Extreme Shape Calculator")

        # Calculate the screen width and height
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # Calculate the x and y coordinates for centering the window
        x = (screenWidth - 900) // 2  # Adjust the width of the window as needed
        y = (screenHeight - 800) // 2  # Adjust the height of the window as needed

        # Set the geometry of the window to center it on the screen
        self.root.geometry(f"900x800+{x}+{y}")

        # Create the title label
        self.homeLable = tk.Label(self.root, text="Extreme Shape Calculator", font=("Ubuntu", 44, "bold"), bg="lightblue", fg="#143675")
        self.homeLable.pack(pady=(250,0))  # Add some vertical spacing
        
        self.homeLable = tk.Label(self.root, text="Created by Ishetagon & Nayanagon", font=("Ubuntu", 28, "bold"), bg="lightblue", fg="#5B82C2")
        self.homeLable.pack(pady=(20,60))

        # Create the "Circulars" button
        self.circularsButton = tk.Button(self.root, text="Circulars", width=20, command=self.openCircular, bg="#60749E", fg="white")
        self.circularsButton.pack(pady=10)  # Add some vertical spacing

        # Create the "Polygons" button
        self.polygonsButton = tk.Button(self.root, text="Polygons", width=20, command=self.openPolygons, bg="#60749E", fg="white")
        self.polygonsButton.pack(pady=10)  # Add some vertical spacing

        # Initializing windows and labels
        self.circularsWindow = None
        self.polygonsWindow = None
        self.resultArea = None
        self.resultLabel = None

    def openCircular(self):
        if self.circularsWindow is None:
            self.circularsWindow = tk.Toplevel(self.root)
            self.circularsWindow.title("Circulars")
            self.circularsWindow.configure(bg="#F5CBE3")

            # Set the dimensions of the circulars window to match the parent window
            self.circularsWindow.geometry(self.root.geometry())

            circularLabel = tk.Label(self.circularsWindow, text="Select one of the following:", font=("Ubuntu", 30, "bold"), bg="#F5CBE3", fg="#3D0F29")
            circularLabel.pack(pady=(250,10))

            # Create a variable to hold the selected value of the radio buttons
            self.radioVar = tk.StringVar()

            # Create the radio buttons
            rbCircle = tk.Radiobutton(self.circularsWindow, text="Circle", variable=self.radioVar, value="Circle", font=("Ubuntu", 17, "bold"), bg="#F5CBE3", fg="#752753")
            rbCircle.pack()

            rbSemi = tk.Radiobutton(self.circularsWindow, text="Semi-circle", variable=self.radioVar, value="Semi-circle", font=("Ubuntu", 17, "bold"), bg="#F5CBE3", fg="#752753")
            rbSemi.pack()

            rbQuart = tk.Radiobutton(self.circularsWindow, text="Quarter", variable=self.radioVar, value="Quarter", font=("Ubuntu", 17, "bold"), bg="#F5CBE3", fg="#752753")
            rbQuart.pack()

            rbSect = tk.Radiobutton(self.circularsWindow, text="Sector (mention angle below)", variable=self.radioVar, value="Sector", font=("Ubuntu", 17, "bold"), bg="#F5CBE3", fg="#752753")
            rbSect.pack()

            self.angleVar = tk.StringVar()
            self.angleVarEntry = tk.Entry(self.circularsWindow, textvariable=self.angleVar, width=20)
            self.angleVarEntry.pack(pady=(0,20))

            # Submit button which checks the choice input
            submitButton = tk.Button(self.circularsWindow, text="Submit", command=self.validInput, bg="#824B6B", fg="white")
            submitButton.pack(pady=10)

            self.errorLabel = tk.Label(self.circularsWindow, text="", bg="#F5CBE3", fg="red")
            self.errorLabel.pack()

            # Closes the Circulars window
            self.circularsWindow.protocol("WM_DELETE_WINDOW", self.closeCirculars)

        # Hides window after use
        self.root.withdraw()
        self.circularsWindow.deiconify()

    def closeCirculars(self):
        self.circularsWindow.withdraw()
        self.root.deiconify()

    def openPolygons(self):
        if self.polygonsWindow is None:
            self.polygonsWindow = tk.Toplevel(self.root)
            self.polygonsWindow.title("Polygons")
            self.polygonsWindow.configure(bg="#DCCBF5")

            # Set the dimensions of the polygons window to match the parent window
            self.polygonsWindow.geometry(self.root.geometry())

            polygonsLabel = tk.Label(self.polygonsWindow, text="Kindly enter number of sides:", font=("Ubuntu", 16), bg="#DCCBF5", fg="#3D0F29")
            polygonsLabel.pack(pady=(50,10))

            self.sidesEntry = tk.Entry(self.polygonsWindow)
            self.sidesEntry.pack(pady=10)

            submitButton = tk.Button(self.polygonsWindow, text="Submit", command=self.calculate, bg="#A190BA", fg="white")
            submitButton.pack(pady=10)
    
            self.polygonsWindow.protocol("WM_DELETE_WINDOW", self.closePolygons)

            self.resultLabel = tk.Label(self.polygonsWindow, text="", bg="#DCCBF5")
            self.resultLabel.pack(pady=10)
            
            self.shapeName = tk.Label(self.polygonsWindow, text="", bg="#DCCBF5")
            self.shapeName.pack(pady=10)

        self.root.withdraw()
        self.polygonsWindow.deiconify()

    def calculate(self):
        sides = int(self.sidesEntry.get())

        def printName(sides):
            polygonNames = ["Triangle", "Square", "Pentagon", "Hexagon", "Heptagon", "Octagon", "Nonagon", "Decagon",
                            "Hendecagon", "Dodecagon", "Triskaidecagon", "Tetradecagon", "Pentadecagon", "Hexadecagon",
                            "Heptadecagon", "Octadecagon", "Enneadecagon", "Icosagon", "Icosikaihenagon", "Icosikaidigon",
                            "Icosikaitrigon", "Icosikaitetragon", "Icosikaipentagon", "Icosikaihexagon", "Icosikaiheptagon",
                            "Icosikaioctagon", "Icosikaienneagon", "Triacontagon", "Triacontakaihenagon",
                            "Triacontakaidigon", "Triacontakaitrigon", "Triacontakaitetragon", "Triacontakaipentagon",
                            "Triacontakaihexagon", "Triacontakaiheptagon", "Triacontakaioctagon", "Triacontakaienneagon",
                            "Tetracontagon", "Tetracontakaihenagon", "Tetracontakaidigon", "Tetracontakaitrigon",
                            "Tetracontakaitetragon", "Tetracontakaipentagon", "Tetracontakaihexagon", "Tetracontakaiheptagon",
                            "Tetracontakaioctagon", "Tetracontakaienneagon", "Pentacontagon", "Pentacontakaihenagon",
                            "Pentacontakaidigon", "Pentacontakaitrigon", "Pentacontakaitetragon", "Pentacontakaipentagon",
                            "Pentacontakaihexagon", "Pentacontakaiheptagon", "Pentacontakaioctagon", "Pentacontakaienneagon",
                            "Hexacontagon", "Hexacontakaihenagon", "Hexacontakaidigon", "Hexacontakaitrigon",
                            "Hexacontakaitetragon", "Hexacontakaipentagon", "Hexacontakaihexagon", "Hexacontakaiheptagon",
                            "Hexacontakaioctagon", "Hexacontakaienneagon", "Heptacontagon", "Heptacontakaihenagon",
                            "Heptacontakaidigon", "Heptacontakaitrigon", "Heptacontakaitetragon", "Heptacontakaipentagon",
                            "Heptacontakaihexagon", "Heptacontakaiheptagon", "Heptacontakaioctagon", "Heptacontakaienneagon",
                            "Octacontagon", "Octacontakaihenagon", "Octacontakaidigon", "Octacontakaitrigon",
                            "Octacontakaitetragon", "Octacontakaipentagon", "Octacontakaihexagon", "Octacontakaiheptagon",
                            "Octacontakaioctagon", "Octacontakaienneagon", "Enneacontagon", "Enneacontakaihenagon",
                            "Enneacontakaidigon", "Enneacontakaitrigon", "Enneacontakaitetragon", "Enneacontakaipentagon",
                            "Enneacontakaihexagon", "Enneacontakaiheptagon", "Enneacontakaioctagon", "Enneacontakaienneagon",
                            "Hectagon"]

            if 3 <= sides <= 100:
                self.resultLabel.config(text=f"\nName of polygon with {sides} sides:", font=("Ubuntu", 17, "bold"), bg="#DCCBF5", fg="#3D0F29")
                self.shapeName.config(text=f"{polygonNames[sides-3]}", font=("Ubuntu", 21, "bold"), bg="#DCCBF5", fg="#317773")
            else:
                self.resultLabel.config(text="\nInvalid number of sides. Please enter a value between 3 and 100.")

        printName(sides)

        lengLabel = tk.Label(self.polygonsWindow, text="\nKindly enter length of sides:", font=("Ubuntu", 16), bg="#DCCBF5", fg="#3D0F29")
        lengLabel.pack(pady=20)
        self.leng = tk.Entry(self.polygonsWindow)
        self.leng.pack(pady=(0,40))
        
        self.resultArea = tk.Label(self.polygonsWindow, text="Area: 0.00", font=("Ubuntu", 18, "bold"), bg="#DCCBF5", fg="#3D0F29")
        self.resultArea.pack(pady=10)
        self.resultPeri = tk.Label(self.polygonsWindow, text="Perimeter: 0.00", font=("Ubuntu", 18, "bold"), bg="#DCCBF5", fg="#3D0F29")
        self.resultPeri.pack(pady=10)
        
        submitButton = tk.Button(self.polygonsWindow, text="Submit", command=self.polygonArea, bg="#A190BA", fg="white")
        submitButton.pack(pady=(20,10))

    def polygonArea(self):
        sides = int(self.sidesEntry.get())
        leng = int(self.leng.get())
        area = (leng ** 2 * sides) / (4 * math.tan(math.pi / sides))
        perimeter = leng * sides
        self.resultArea.config(text=f"Area: {area:.2f}")
        self.resultPeri.config(text=f"Perimeter: {perimeter:.2f}")
    
    def closePolygons(self):
        self.polygonsWindow.withdraw()	
        self.root.deiconify()

    def validInput(self):
        selection = self.radioVar.get()
        if selection == "":
            self.errorLabel.config(text="Please make a selection.", bg="#F5CBE3")
        elif selection == "Sector":
            angleSect = self.angleVar.get()
            if angleSect.isdigit():
                angle = int(angleSect)
                if 0 <= angle <= 360:
                    self.errorLabel.config(text="")
                    self.openSect(angle)
                else:
                    self.errorLabel.config(text="Invalid sector angle. Please retry.", bg="#F5CBE3")
            else:
                self.errorLabel.config(text="Invalid sector angle. Please retry.", bg="#F5CBE3")
        else:
            self.errorLabel.config(text="")
            self.resultWin(selection)

    def openSect(self, angle):
        sectorWindow = tk.Toplevel(self.circularsWindow)
        sectorWindow.title("Sector Window")
        sectorWindow.configure(bg="#D6FCC7")

        # Set the dimensions of the sector window to match the parent window
        sectorWindow.geometry(self.circularsWindow.geometry())

        label = tk.Label(sectorWindow, text=f"Sector Angle: {angle}", bg="#D6FCC7", fg="#185202", font=("Ubuntu", 23, "bold"))
        label.pack(pady=(70,30))

        radiusLabel = tk.Label(sectorWindow, text="Kindly enter a radius:", bg="#D6FCC7", fg="#185202", font=("Ubuntu", 27, "bold"))
        radiusLabel.pack(pady=10)
        radiusEntry = tk.Entry(sectorWindow)
        radiusEntry.pack(pady=10)

        resultArea = tk.Label(sectorWindow, text="Area: 0.00", bg="#D6FCC7", fg="#185202", font=("Ubuntu", 18, "bold"))
        resultArea.pack(pady=10)
        resultPeri = tk.Label(sectorWindow, text="Perimeter: 0.00", bg="#D6FCC7", fg="#185202", font=("Ubuntu", 18, "bold"))
        resultPeri.pack(pady=(10,40))

        def areaPeri():
            radius = float(radiusEntry.get())
            area = angle / 360 * (math.pi * radius ** 2)
            perimeter = angle / 360 * (math.pi * radius + 2 * radius)
            resultArea.config(text=f"Area: {area:.2f}")
            resultPeri.config(text=f"Perimeter: {perimeter:.2f}")

        submitButton = tk.Button(sectorWindow, text="Submit", command=areaPeri, bg="#4E6945", fg="white")
        submitButton.pack(pady=10)

        closeButton = tk.Button(sectorWindow, text="Close", command=sectorWindow.destroy, bg="#4E6945", fg="white")
        closeButton.pack(pady=10)

    def resultWin(self, selection):
        resultWindow = tk.Toplevel(self.circularsWindow)
        resultWindow.title("Result Window")
        resultWindow.geometry(self.circularsWindow.geometry())
        resultWindow.configure(bg="#D6FCC7")

        if selection in ["Circle", "Semi-circle", "Quarter"]:
            radiusLabel = tk.Label(resultWindow, text="Kindly enter a radius:", font=("Ubuntu", 27, "bold"), bg="#D6FCC7", fg="#185202")
            radiusLabel.pack(pady=(250, 20))
            radiusEntry = tk.Entry(resultWindow)
            radiusEntry.pack(pady=10)

            resultArea = tk.Label(resultWindow, text="Area: 0.00", font=("Ubuntu", 18, "bold"), bg="#D6FCC7", fg="#185202")
            resultArea.pack(pady=10)
            resultPeri = tk.Label(resultWindow, text="Perimeter: 0.00", font=("Ubuntu", 18, "bold"), bg="#D6FCC7", fg="#185202")
            resultPeri.pack(pady=(10,40))

            def areaPeri():
                radius = float(radiusEntry.get())
                if selection == "Circle":
                    area = math.pi * radius ** 2
                    perimeter = 2 * math.pi * radius
                elif selection == "Semi-circle":
                    area = 0.5 * math.pi * radius ** 2
                    perimeter = math.pi * radius + 2 * radius
                else:  # Quarter
                    area = 0.25 * math.pi * radius ** 2
                    perimeter = 0.5 * math.pi * radius + 2 * radius
                resultArea.config(text=f"Area: {area:.2f}")
                resultPeri.config(text=f"Perimeter: {perimeter:.2f}")

            submitButton = tk.Button(resultWindow, text="Submit", command=areaPeri, bg="#4E6945", fg="white")
            submitButton.pack(pady=10)

        else:
            resultLabel = tk.Label(resultWindow, text="Invalid selection. Please try again.")
            resultLabel.pack(pady=20)

        closeButton = tk.Button(resultWindow, text="Close", command=resultWindow.destroy, bg="#4E6945", fg="white")
        closeButton.pack(pady=10)

if __name__ == "__main__":
    app = ShapeCalculatorApp()
    app.root.mainloop()