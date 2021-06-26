import PySimpleGUI as sg
from time import sleep, time
from threading import Thread


class Pomodoro:
    def __init__(self):
        self.time = {
            "minutes": 20,
            "seconds": 00
        }
        self.running = False
        self.main()

    def change_time(self, window):
        while self.running:
            sleep(1)
            if self.time["seconds"] > 0:
                self.time["seconds"] -= 1
            elif self.time["seconds"] <= 0 and self.time["minutes"] > 0:
                self.time["minutes"] -= 1
                self.time["seconds"] = 59
            else:
                self.running = False
                try:
                    import winsound
                    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
                except ImportError:
                    from beepy import beep
                    beep(sound="ping")
                break
            window["test"].update(f"{self.time['minutes']}:{self.time['seconds']}")
        sg.popup("The pomodoro has been ended!")

    def define_time(self, window):
        self.time["minutes"] = int(window["minutes"].get())

    def main(self):
        sg.theme("DarkAmber")
        
        layout = [[sg.Text(f"{self.time['minutes']}:{self.time['seconds']}", key="test", size=(4,1), font=("arial", 48))],
                  [sg.InputText(key="minutes", size=(17, 10))],
                  [sg.Button("Start", size=(14, 2))]
                  ]

        window = sg.Window("Pomodoro", layout)

        while True:
            event, value = window.read()
            if event == sg.WIN_CLOSED or event == "OK":
                break

            if event == "Start" and self.running == False:
                self.running = True
                self.define_time(window)

            if self.running:
                Thread(target=self.change_time, args=[window]).start()

        window.close()


Pomodoro()
