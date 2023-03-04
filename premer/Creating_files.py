import os

class Num:
	def __init__(self, full_derectore_replese, num = None, number = None):
		self.full_derectore_replese = full_derectore_replese
		self.num = num
		self.number = number

	def number_two(self):
		with open(os.path.join(f'{self.full_derectore_replese}', f'Example_{self.num}.py'), 'w', encoding='utf-8') as file:
			file.write("# Задача №  Ответ \nprint('x y z w')\nfor x in range(2):\n \tfor y in range(2):\n \t\tfor z in range(2):\n \t\t\tfor w in range(2):\n \t\t\t\tif pass:\n \t\t\t\t\tprint(x,y,z,w)")

	def number_add(self):
		der = os.path.join(f'decision_dan#{self.num}')
		self.full_derectore_replese = os.path.join(f'{self.full_derectore_replese}', f'{der}')
		os.makedirs(self.full_derectore_replese)
		with open(os.path.join(f'{self.full_derectore_replese}', f'Example.py', ), 'w', encoding='utf-8') as file:
			file.write(f'# Задача №  Ответ \na = open("/home/kukuruzka-vitya/CODE/Inform/Task#{self.number}/decision_dan#{self.num}/{self.number}.txt").readline()\n')

	def number_add_six(self):
		der = os.path.join(f'decision_dan#{self.num}')
		self.full_derectore_replese = os.path.join(f'{self.full_derectore_replese}', f'{der}')
		os.makedirs(self.full_derectore_replese)
		with open(os.path.join(f'{self.full_derectore_replese}', f'Example.py', ), 'w', encoding='utf-8') as file:
			file.write('')

	def number_img(self):		
		der = os.path.join(f'decision_img#{self.num}')
		os.makedirs(os.path.join(f'{self.full_derectore_replese}', f'{der}'))

	def number_tabl(self):
		der = os.path.join(f'decision_tabl#{self.num}')
		os.makedirs(os.path.join(f'{self.full_derectore_replese}', f'{der}'))

	def number_twenty(self):
		der = os.path.join(f'decision_dan#{self.num}')
		self.full_derectore_replese = os.path.join(f'{self.full_derectore_replese}', f'{der}')
		os.makedirs(self.full_derectore_replese)
		with open(os.path.join(f'{self.full_derectore_replese}', f'Example.py', ), 'w', encoding='utf-8') as file:
			file.write('# Задача №  Ответ 19) 20) 21)')
		with open(os.path.join(f'{self.full_derectore_replese}', f'Example_txt.txt', ), 'w', encoding='utf-8') as file:
			file.write('# Задача №  ')

def check_result():
	while True:
		print(f'<{"="*30}>', 'Какая задача?: 1-27 или 0(любая задача) или #(выход)', f'<{"="*30}>', sep='\n')
		result = input()
		if result in [str(i) for i in range(1,28)] or result == '0':
			return result
		if result == '#':
			return 9**9
		print('Неправельный ввод, попробуйте заново')
		continue

def create_file(number ,replay = 1):
	while True:
		clear_derectore = os.getcwd()
		derectore_replese = clear_derectore[:-clear_derectore[::-1].index('//'[0])-1]
		full_derectore_replese = os.path.join(f'{derectore_replese}', 'CODE', 'Inform', f'Task#{number}')
		control_derect_replese = os.path.join(f'{derectore_replese}', 'CODE', 'Inform', 'Control', 'Creating_files.py')

		if number in ['19', '20', '21']:
			full_derectore_replese = os.path.join(f'{derectore_replese}', 'CODE', 'Inform', 'Task#19-21')
		if not os.path.isdir((f'{full_derectore_replese}')):
			os.makedirs(full_derectore_replese)
		if not os.path.isdir(os.path.join(f'{derectore_replese}', 'CODE', 'Inform', 'Control')):
			os.makedirs(os.path.join(f'{derectore_replese}', 'CODE', 'Inform', 'Control'))
		if not os.path.isdir(control_derect_replese):
			try:
				os.replace(os.path.join(clear_derectore, 'Inform', 'Control', 'Creating_files.py'), control_derect_replese)
			except:
				os.replace(os.path.join(clear_derectore, 'Creating_files.py'), control_derect_replese)
				
		for _ in range(replay):
			num = len(os.listdir(full_derectore_replese))+1

			if number == '2':
				Num(full_derectore_replese, num).number_two()
				continue

			if number in ['1', '4', '11', '13']:
				Num(full_derectore_replese, num).number_img()
				continue

			if number in ['3', '9', '18', '22']:
				Num(full_derectore_replese, num).number_tabl()
				continue

			if number in ['17', '24', '26', '27']:
				Num(full_derectore_replese, num, number).number_add()
				continue

			if number == '6':
				Num(full_derectore_replese, num, number).number_add_six()
				continue

			if number in ['19', '20', '21']:
				Num(full_derectore_replese, num).number_twenty()
				continue

			#0, 5, 7, 8, 10, 12, 14, 15, 16, 23, 25
			with open(os.path.join(f'{full_derectore_replese}', f'Example_{num}.py', ), 'w', encoding='utf-8') as file:
				file.write('# Задача №  Ответ ')
		break

while True:
	number = check_result()
	if number == 9**9:
		break
	print('Сколько? Количество(число > 0) или Выйти(0)')
	newly = int(input())
	if newly > 0:
		create_file(number, newly)
	break
