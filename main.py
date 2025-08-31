import tkinter as tk

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronómetro")
        self.root.geometry("650x350")
        self.root.config(bg="#1e1e2f")

        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0
        self.corriendo = False

   
        self.canvas_min = tk.Canvas(root, width=200, height=200, bg="#1e1e2f", highlightthickness=0)
        self.canvas_seg = tk.Canvas(root, width=200, height=200, bg="#1e1e2f", highlightthickness=0)
        self.canvas_mili = tk.Canvas(root, width=200, height=200, bg="#1e1e2f", highlightthickness=0)

        self.canvas_min.grid(row=0, column=0, padx=20, pady=20)
        self.canvas_seg.grid(row=0, column=1, padx=20, pady=20)
        self.canvas_mili.grid(row=0, column=2, padx=20, pady=20)

      
        self.texto_min = self.canvas_min.create_text(100, 80, text="0", font=("Arial", 32, "bold"), fill="#ff4444")
        self.etq_min = self.canvas_min.create_text(100, 150, text="Minutos", font=("Arial", 12, "bold"), fill="white")

        self.texto_seg = self.canvas_seg.create_text(100, 80, text="0", font=("Arial", 32, "bold"), fill="#44ff88")
        self.etq_seg = self.canvas_seg.create_text(100, 150, text="Segundos", font=("Arial", 12, "bold"), fill="white")

        self.texto_mili = self.canvas_mili.create_text(100, 80, text="0", font=("Arial", 32, "bold"), fill="#aa55ff")
        self.etq_mili = self.canvas_mili.create_text(100, 150, text="Milisegundos", font=("Arial", 12, "bold"), fill="white")

       
        botones = tk.Frame(root, bg="#1e1e2f")
        botones.grid(row=1, column=0, columnspan=3, pady=20)

        self.boton_iniciar = tk.Button(botones, text="▶ Iniciar", command=self.iniciar, width=10, bg="#44ff88", fg="black", font=("Arial", 12, "bold"))
        self.boton_iniciar.grid(row=0, column=0, padx=10)

        self.boton_pausar = tk.Button(botones, text="⏸ Pausar", command=self.pausar, width=10, bg="#ffaa44", fg="black", font=("Arial", 12, "bold"))
        self.boton_pausar.grid(row=0, column=1, padx=10)

        self.boton_reiniciar = tk.Button(botones, text="🔄 Reiniciar", command=self.reiniciar, width=10, bg="#ff4444", fg="white", font=("Arial", 12, "bold"))
        self.boton_reiniciar.grid(row=0, column=2, padx=10)

    def actualizar(self):
        if self.corriendo:
            self.milisegundos += 1
            if self.milisegundos == 100:
                self.milisegundos = 0
                self.segundos += 1
            if self.segundos == 60:
                self.segundos = 0
                self.minutos += 1

            self.canvas_min.itemconfig(self.texto_min, text=str(self.minutos))
            self.canvas_seg.itemconfig(self.texto_seg, text=str(self.segundos))
            self.canvas_mili.itemconfig(self.texto_mili, text=str(self.milisegundos))

            self.root.after(10, self.actualizar)

    def iniciar(self):
        if not self.corriendo:
            self.corriendo = True
            self.actualizar()

    def pausar(self):
        self.corriendo = False

    def reiniciar(self):
        self.corriendo = False
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0
        self.canvas_min.itemconfig(self.texto_min, text="0")
        self.canvas_seg.itemconfig(self.texto_seg, text="0")
        self.canvas_mili.itemconfig(self.texto_mili, text="0")



root = tk.Tk()
app = Cronometro(root)
root.mainloop()
