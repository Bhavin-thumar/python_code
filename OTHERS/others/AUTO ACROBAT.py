import subprocess, time, pyautogui, os, datetime

class Auto_acrobat:

	def __init__(self):
		self.ignore_file_list = set()


	def open_acrobat(self):
		with subprocess.Popen(r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe") as p:
			start = time.time()
			while not pyautogui.pixelMatchesColor(585,154,(250,250,250)):
				time.sleep(1)
				if int(time.time() - start) > 20:
					p.kill()
					self.open_acrobat()
			status = True
			files_to_look = self.file_details()
			hits_break = False
			for file_name in files_to_look: 
			# def multi_thread(file_name):
				if status == False:
					hits_break = True
					break
				status, ignore_file = self.open_file(file_name)
				if status == False:
					self.ignore_file_list.add(file_name)
					p.kill()
					continue
				status, ignore_file = self.process_file(file_name)
				if status == False:
					self.ignore_file_list.add(file_name)
					p.kill()
					continue
				status, ignore_file = self.close_file(file_name,status)
				if status == False:
					self.ignore_file_list.add(file_name)
					p.kill()
					continue
				self.display_status(file_name)
			
			if hits_break:
				self.open_acrobat()
			
			p.kill()
		# with concurrent.futures.ProcessPoolExecutor() as executor:
		# 	executor.map(multi_thread, files)


	def file_details(self):
		all_files = set(os.listdir(r'C:\Users\hardip thummar\Desktop\New folder (2)'))
		files_done = set(os.listdir(r'C:\Users\hardip thummar\Desktop\New folder (3)'))
		return all_files - files_done - self.ignore_file_list


	def open_file(self,file_name):
		pyautogui.click(585,150)
		pyautogui.press(['alt', 'f', 'o'])
		start = time.time()
		while not pyautogui.pixelMatchesColor(278,90,(255,255,255)):
			time.sleep(1)
			if int(time.time() - start) > 20:
				ignore_file = file_name
				open_status = False
				break
		else:
			ignore_file = None
			open_status = True
			time.sleep(2)
			pyautogui.click(444,123)
			time.sleep(1)
			pyautogui.press('delete')
			open_path = 'C:\\Users\\hardip thummar\\Desktop\\New folder (2)'
			pyautogui.typewrite(open_path)
			pyautogui.press('enter')
			pyautogui.click(472,492)
			pyautogui.typewrite(file_name)
			pyautogui.press('enter')

		return open_status, ignore_file

	def process_file(self,file_name):
		start = time.time()
		while not pyautogui.pixelMatchesColor(159,51,(250,250,250)):
			time.sleep(1)
			if int(time.time() - start) > 20:
				ignore_file = file_name
				process_status = False
				break
		else:
			pyautogui.click(434,181, button = 'right')
			time.sleep(1)
			pyautogui.press('r')
			pyautogui.press(['alt', 'f', 'a'])
			start = time.time()
			while not (pyautogui.pixelMatchesColor(75,59,(250,250,250)) and pyautogui.pixelMatchesColor(829,508,(33,117,200))):
				time.sleep(1)
				if int(time.time() - start) > 40:
					ignore_file = file_name
					process_status = False
					break
			else:
				time.sleep(2)
				pyautogui.click(730,515)
				start = time.time()
				while not pyautogui.pixelMatchesColor(117,86,(233,31,0)):
					time.sleep(1)
					if int(time.time() - start) > 20:
						ignore_file = file_name
						process_status = False
						break
				else:
					time.sleep(1)
					pyautogui.click(439,122)
					pyautogui.press('delete')
					time.sleep(1)
					save_path = 'C:\\Users\\hardip thummar\\Desktop\\New folder (3)'
					pyautogui.typewrite(save_path)
					time.sleep(1)
					pyautogui.press('enter')
					pyautogui.click(552,524)
					process_status = True
					ignore_file = None
					time.sleep(1)

		return process_status, ignore_file

	def close_file(self,file_name,status):
		if status:
			pyautogui.click(585,150)
			pyautogui.press(['alt', 'f', 'c'])
			time.sleep(2)
			status = True
			ignore_file = None
		else:
			status = False
			ignore_file = file_name
		return status, ignore_file

	def display_status(self, file_name):
		pyautogui.alert(f'{file_name} done', timeout = 700)


	def summary(self):
		today = datetime.datetime.today()

		with open(f'{today.day}-{today.month}-{today.year}-{today.hour}-{today.minute}.txt', 'w') as f:
			for index, i in enumerate(self.ignore_file_list):
				f.write(f'{index+1}-{i}')
				f.write('\n')


auto = Auto_acrobat()
# auto.open_acrobat()
print(auto.__dict__)
