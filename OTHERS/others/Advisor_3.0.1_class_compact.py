import os, subprocess, time, pyautogui, datetime

class Planning:

    def __init__(self):

        self.skip_files = set()

    def file_details(self):
        pending_file =  r'D:\New folder'
        done_file = r'D:\New folder2'
        pending_file = set(os.listdir(pending_file))

        def proper_name(string):
            parse = string.split('D')
            first = parse[0]
            temp = parse[1].split('.')
            second = '(D' + temp[0] + ')'
            third = '.' + temp[1]
            return first+second+third

        done_file = set(map(proper_name, os.listdir(done_file)))
        missing_file = pending_file - done_file - self.skip_files
        total_files = len(pending_file)
        file_done = len(done_file.intersection(pending_file))

        return missing_file, file_done, total_files

    def check(self, status_ok, ignore_file):
        if not status_ok:
            self.skip_files.add(ignore_file)
            p.kill()
            return continue

    def advisor_open(self):
        hits_break = False
        adviser_path = r"C:\Program Files\Sarin Technologies\Advisor\Advisor.exe"
        with subprocess.Popen(adviser_path) as p:
            start = time.time()
            while not (pyautogui.pixelMatchesColor(1112,300,(255,255,255))):  # pixel for advisor open
                time.sleep(1)
                if int(time.time() - start) > 30:
                    p.kill()
                    self.advisor_open()
            status_ok = True
            time.sleep(1)
            files_to_look, file_done, total_files = self.file_details()
            for file in files_to_look:
                file_name, extension = os.path.splitext(file)
                if status_ok == False:
                    hits_break = True
                    break
                file_done += 1
                status_ok, ignore_file = self.open_files(file)
                self.check(status_ok, ignore_file)
                # if status_ok == False:
                #     self.skip_files.add(ignore_file)
                #     p.kill()
                #     continue
                status_ok, ignore_file = self.load_files(file)
                self.check(status_ok, ignore_file)
                # if status_ok == False:
                #     self.skip_files.add(ignore_file)
                #     p.kill()
                #     continue
                status_ok, ignore_file = self.process_files(file)
                self.check(status_ok, ignore_file)
                # if status_ok == False:
                #     self.skip_files.add(ignore_file)
                #     p.kill()
                #     continue
                self.display_status(file_done, total_files)

            if hits_break:
                self.advisor_open()

            p.kill()


    def open_files(self, file):
        pyautogui.click(650,250)
        pyautogui.press(['alt', 's', 'o'])# code to open dialog box
        start = time.time()
        while not (pyautogui.pixelMatchesColor(1027,473,(195,203,214))): # pixels for open dialog box
            time.sleep(1)
            if int(time.time() - start) > 20:
                status_ok = False
                ignore_file = file
                break
        else:
            status_ok = True
            ignore_file = None
            time.sleep(1)
            pyautogui.click(411,46, button = 'left')
            time.sleep(0.5)
            pyautogui.click(426, 80, button = 'left')
            pyautogui.click(517,720, button = 'left')
            pyautogui.press('backspace',presses =30)
            time.sleep(1)
            file_name, extension = os.path.splitext(file)
            split_name = file_name.split('(')[0]
            time.sleep(1)
            pyautogui.typewrite(split_name)
            time.sleep(3)
            pyautogui.press('enter')

        return status_ok, ignore_file


    def load_files(self,file):
        start = time.time()
        while not (pyautogui.pixelMatchesColor(1040,669,(255,255,255)) and pyautogui.pixelMatchesColor(966,677,(0,0,128))): # pixels for load files
            time.sleep(1)
            if int(time.time() - start) > 20:
                status_ok = False
                ignore_file = file
                break
        else:
            status_ok = True
            ignore_file = None

        return status_ok, ignore_file


    def auto_19(self, file):
        pyautogui.click(488,100, button = 'left')
        start = time.time()
        while not (pyautogui.pixelMatchesColor(336,145,(185,213,244)) and pyautogui.pixelMatchesColor(1016,673,(0,0,128))):
            time.sleep(1)
            if int(time.time() - start) > 200:
                status_ok = False
                ignore_file = file
                break
        else:
            status_ok = True
            ignore_file = None

        return status_ok, ignore_file


    def process_files(self, file):
        # code to start process file until save as dialog box
        time.sleep(1)
        pyautogui.click(822,325, button = 'right')
        time.sleep(1)
        pyautogui.press(['down', 'down', 'right', 'enter'])
        time.sleep(1)
        pyautogui.click(570, 101, button = 'left')
        time.sleep(1)
        pyautogui.press(['enter'])
        time.sleep(1)

        status_ok, ignore_file = self.auto_19(file)
        if status_ok == False:
            return status_ok, ignore_file
        else:
            pyautogui.press(['alt', 's', 's', 's', 'enter'])
            time.sleep(2)
            while not (pyautogui.pixelMatchesColor(1027,473,(195,203,214))): # pixels for save as dialog box
                time.sleep(1)

            pyautogui.click(411,46, button = 'left')
            time.sleep(0.5)
            pyautogui.click(381,96, button = 'left')
            time.sleep(0.5)
            pyautogui.press('backspace',presses =30)
            pyautogui.typewrite(file)

            pyautogui.click(1070,760, button = 'left')
            time.sleep(2)
            if pyautogui.pixelMatchesColor(727,393,(240,240,240)): # pixels for error window
                print('Hit while saving file')
                status_ok = False
                ignore_file = file
            else:
                status_ok = True
                ignore_file = None

            return status_ok, ignore_file


    def display_status(self, file_done, total_files):
        pyautogui.alert(f'{file_done} Done\n {total_files - file_done} Remaining', timeout = 700)


    def write_summary(self):
        today = datetime.datetime.today()
        with open(f'{today.day}-{today.month}-{today.year}-{today.hour}-{today.minute}.txt', 'w') as f:
            files_missing, *a  = self.file_details()
            for index, file in enumerate(files_missing):
                f.write(f'{index+1}-{file}')
                f.write('\n')

auto_planning = Planning()
auto_planning.advisor_open()
auto_planning.write_summary()
