#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""

Simples DojoTimer


"""
from Tkinter import *
import tkSimpleDialog
from time import sleep

class Clock(object):
    """

    Classe principal para o aplicativo.

    """

    def __init__(self, master, default_time=1):

        # Cria o frame
        self.frame = Frame(master)
        self.frame.pack()

        # Obtém a janela TopLevel 
        self.top = self.frame.winfo_toplevel()

        # Change some of it's attributes
        self.top.title("DojoTimer") # Modifica o Título
        self.top.attributes('-topmost', 1) # Sempre no topo
        self.top.resizable(0, 0) # Tornar não redimensionável

        # Método responsável por criar os outros widgets
        self.__create_widgets()

        # Some default values
        self.running = False
        self.default_time = default_time # defaul time (in minutes)
        self.seconds = 60 * self.default_time

        self.labelstr.set(
            '%02d:%02d' % ((self.seconds /60), (self.seconds % 60))
        )

    def __create_widgets(self):
        """ Cria o widgets para o tempo."""        
        self.labelstr = StringVar()
        self.label = Label(
            self.frame,
            textvariable=self.labelstr,
            fg='#198931',
            font=('Helvetica', '40')
        )
        self.label.pack()

        # Some buttons
        self.start_btn = Button(self.frame, text="Iniciar", command=self.start)
        self.start_btn.pack(side=LEFT)

        self.stop_btn = Button(self.frame, text='Pause', command=self.stop)
        self.stop_btn.pack(side=LEFT)

        self.reset_btn = Button(self.frame, text='Reiniciar', command=self.reset)
        self.reset_btn.pack(side=LEFT)

        self.set_time_btn = Button(
            self.frame,
            text = 'Config Tempo',
            command = self.set_time,
            )
        self.set_time_btn.pack(side=LEFT)

        self.quit_btn = Button(self.frame, text='Quit', command=self.frame.quit)
        self.quit_btn.pack(side=LEFT)

    def start(self):
        """
        Start the clock
        """
        if not self.seconds:
            self.top.deiconify()
            self.reset()
        if not self.running:
            self.top.deiconify()
            self.running = True
            self.top.title("*DojoTimer*")
            self.update()

    def update(self):
        """
        Update the display
        """

        if self.running:
            if 0 < self.seconds <= 60:
                self.label['fg'] = '#efbf16'                
                new_str_ap = 'Sugestões'
            elif self.seconds <= 0:                
                self.label['fg'] = '#d70505'
                self.stop()     
            else:
            	new_str_ap = ' '       	
            new_str = '%02d:%02d \n %s' % ((self.seconds / 60), (self.seconds % 60), new_str_ap)
            self.labelstr.set(new_str)
            self.label.after(1000, self.update)
            if self.seconds:
                self.seconds -= 1        			

    def stop(self):
        """
        Para o relógio
        """
        self.top.title("DojoTimer")
        self.running = False

    def reset(self):
        """
        Para o relógio e reinicia o tempo
        """
        self.stop()
        self.seconds = 60 * self.default_time
        self.label['fg'] = '#198931'
        new_str = '%02d:%02d' % ((self.seconds /60), (self.seconds % 60))
        self.labelstr.set(new_str)

    def ocultar(self):
        """
        Ocultar
        """
        self.top.deiconify()
        sleep( 2 )
        self.top.iconify()
        sleep( 2 )
        self.top.deiconify()

    def aparecer(self):
        """
        Aparecer
        """
        

    def set_time(self):
        """
        Caixa de diálogo
        """
        try:
            self.default_time = tkSimpleDialog.askfloat(
                'Set time',
                'Specify the time (in minutes)',
                parent=self.top
            )
            self.reset()
        except TypeError:
            pass

if __name__ == '__main__':
    root = Tk()
    clock = Clock(root, 1)

    root.mainloop()
