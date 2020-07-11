import os, subprocess, time, pyautogui, datetime

skip_files = set()

def file_details():
	galaxy_file =  r'D:\New folder'
	bv_run_file = r'D:\B_V_RUN\Startstones1'
	galaxy_file = set(os.listdir(galaxy_file))
	bv_run_file = set(os.listdir(bv_run_file))
	missing_file = galaxy_file - bv_run_file - skip_files
	total_files = len(galaxy_file)
	file_done = len(bv_run_file.intersection(galaxy_file))

	return missing_file, file_done, total_files


def advisor_open():
	hits_break = False
	adviser_path = r"C:\Program Files\Sarin Technologies\Advisor\Advisor.exe"
	with subprocess.Popen(adviser_path) as p:
		start = time.time()
		while not (pyautogui.pixelMatchesColor(1112,300,(255,255,255))):  # pixel for advisor open
			time.sleep(1)
			if int(time.time() - start) > 20:
				p.kill()
				advisor_open()
		status_ok = True
		time.sleep(1)
		files_to_look, file_done, total_files = file_details()
		for file in files_to_look:
			file_name, extension = os.path.splitext(file)
			if status_ok == False:
				hits_break = True
				break
			file_done += 1
			status_ok, ignore_file = open_files(file)
			if status_ok == False:
				skip_files.add(ignore_file)
				p.kill()
				continue
			status_ok, ignore_file = load_files(file)
			if status_ok == False:
				skip_files.add(ignore_file)
				p.kill()
				continue
			status_ok, ignore_file = process_files(file)
			if status_ok == False:
				skip_files.add(ignore_file)
				p.kill()
				continue
			# status_ok, ignore_file = check_completed_process(file)
			# if status_ok == False:
			# 	skip_files.add(ignore_file)
			# 	p.kill()
			# 	continue
			display_status(file_done, total_files)
		
		if hits_break:
			advisor_open()

		p.kill()


def open_files(file):
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
	    status_ok == True
	    ignore_file = None
		time.sleep(1)
		pyautogui.click(517,720, button = 'left')
		# pyautogui.keyDown('shift')
		# pyautogui.press('left', presses = 30)
		# time.sleep(1)
		pyautogui.press('backspace',presses =30)
		# pyautogui.keyUp('shift')
		time.sleep(1)
		file_name, extension = os.path.splitext(file)
		split_name, split_name_2 = file_name.split('(') # comment this if file name not enter properly
		split_name_2 = split_name_2.split(')')[0] # comment this if file name not enter properly
		pyautogui.typewrite(split_name) # comment this if file name not enter properly
		time.sleep(0.5) # comment this if file name not enter properly
		pyautogui.press('(') # comment this if file name not enter properly
		time.sleep(0.5) # comment this if file name not enter properly
		pyautogui.typewrite(split_name_2) # comment this if file name not enter properly
		time.sleep(0.5) # comment this if file name not enter properly
		pyautogui.press(')') # comment this if file name not enter properly
		time.sleep(1) # comment this if file name not enter properly


		# split_name = file_name.split('(')[0] # uncomment this out if file name not enter properly
		# time.sleep(1) # uncomment this out if file name not enter properly
		# pyautogui.typewrite(split_name) # uncomment this out if file name not enter properly
		# time.sleep(3) # uncomment this out if file name not enter properly
		pyautogui.press('enter')

	return status_ok, ignore_file


def load_files(file):
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


def process_files(file):
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
	pyautogui.press(['alt', 's', 's', 's', 'enter'])
	time.sleep(2)
	while not (pyautogui.pixelMatchesColor(1027,473,(195,203,214))): # pixels for save as dialog box
		time.sleep(1)
	pyautogui.press('enter')
	time.sleep(2)
	pyautogui.press('enter')
	if pyautogui.pixelMatchesColor(727,393,(240,240,240)): # pixels for error window
		status_ok = False
		ignore_file = file
	else:
		status_ok = True
		ignore_file = None
		
	return status_ok, ignore_file


# def check_completed_process(file):
# 	time.sleep(2)
# 	if (pyautogui.pixelMatchesColor(727,393,(240,240,240))): # pixels to check complete process
	# 	status_ok = False
	# 	ignore_file = file
	# else:
	# 	status_ok = True
	# 	ignore_file = None

	# return status_ok, ignore_file

def display_status(file_done, total_files):
	pyautogui.alert(f'{file_done} Done\n {total_files - file_done} Remaining', timeout = 700)


status = False

if status == False:
	advisor_open()

today = datetime.datetime.today()
with open(f'{today.day}-{today.month}-{today.year}-{today.hour}-{today.minute}.txt', 'w') as f:
	files_missing, *  = file_details() 
	for index, file in enumerate(files_missing):
		f.write(f'{index+1}-{file}')
		f.write('\n')