import os

derectore = os.getcwd()
try:
	derectore_repl = derectore[:-derectore[::-1].index('/')-1]
except:
	derectore_repl = derectore[:-derectore[::-1].index('\\'[0])-1]
derect_practic = os.path.join(f'{derectore_repl}', 'CODE', 'Practic')
derect_one_file_Pros = os.path.join(f'{derectore_repl}', 'CODE', 'Practic', "One_file_Pros.txt")
derect_two_file_noPros = os.path.join(f'{derectore_repl}', 'CODE', 'Practic', "Two_file_noPros.txt")
first_pr_file = os.path.join(f'{derectore}', 'Practic', 'first_pr.py')

if not os.path.isdir(f"{derect_practic}"):
	os.makedirs(f'{derect_practic}')
	if not os.path.isdir(derect_one_file_Pros):
		with open((f'{derect_one_file_Pros}'), 'w', encoding='utf-8') as file:
			file.write('')
	if not os.path.isdir(derect_two_file_noPros):
		with open((f'{derect_two_file_noPros}'), 'w', encoding='utf-8') as file:
			file.write('')
	if not os.path.isdir(os.path.join(f'{derect_practic}', '1_pr.py')):
		try:
			os.replace(os.path.join(f'{derectore}', 'first_pr.py'), f'{first_pr_file}')
		except:
			os.replace(os.path.join(f'{derectore}', 'Practic', 'first_pr.py'), f'{first_pr_file}')

class Movies:
	def read_movies_pros(self):
		with open(derect_one_file_Pros, 'r', encoding='utf-8') as file:
			return [line[int(line.find('.')+2):].replace('\n', '').rstrip() for line in file.readlines()]

	def read_movies_nopros(self):
		with open(derect_two_file_noPros, 'r', encoding='utf-8') as file:
			return [line[int(line.find('.')+2):].replace('\n', '').rstrip() for line in file.readlines()]
	
	def read_movies_completely(self):
		movies = []
		with open(derect_one_file_Pros, 'r', encoding='utf-8') as file:
			movies.extend(file.readlines())
		with open(derect_two_file_noPros, 'r', encoding='utf-8') as file:
			movies.extend(file.readlines())
		return [line[int(line.find('.')+2):].replace('\n', '').rstrip() for line in movies]

def check_reg():
	while True:
		print('Просмотренные/Не просмотренные == введите П или НП')
		reg = input()
		if reg == 'П' or reg == 'НП':
			return reg
		print('Не правильно введена запись, попробуйте еще раз')

def check_reg_library():
	while True:
		print('Просмотренные/Не просмотренные/Все == введите П или НП или ВС')
		reg = str(input()).lower()
		prav_reg = ['п', 'нп', 'вс']
		if reg in prav_reg:
			return reg
		print('Не правильный ввод, попробуйте еще раз')

def check_film():
	movies = [line.lower() for line in (Movies().read_movies_completely())]
	while True:
		print('--Введите фильм--||**Закрыть**--> #')
		film = input()
		prov = film.lower()
		if prov == '#':
			return 9**9
		if prov in movies:
			print('Этот фильм уже добавлен, попробуйте другой')
			continue
		return film

def info_neil():
	while True:
		print('Запись?||Удаление?||Перевод?||Выход == З||У||П||#')
		neil = input()
		if neil == 'З' or neil == 'У':
			return neil
		if neil == 'П':
			print('Какой фильм хотите перевести в другую библиотеку?')
			return neil
		if neil == '#':
			return 9**9
		print('Не правельный ввод, пожалйста попробуйде заново')
		continue

def read_rehen():
	while True:
		print('##Посмотреть библиотеку фильмов##||$$Записать/удалить/переместь фильм$$||Выход == введите П или З или #')
		rehen = input()
		if rehen == 'П' or rehen == 'З':
			return rehen
		if rehen == '#':
			return 9**9
		print('Не правельный ввод, пожалйста попробуйде заново')
		continue

while True:
#ПРИВЕТСТВИЕ
	print('ЭТОТ КОД ДЛЯ УЧЕТА ФИЛЬМОВ')
	rehen = read_rehen()
	if rehen == 9**9:
		break
			
#БИБЛИОТЕКА
	if rehen == 'П': #Посмотреть
		file_pros = Movies().read_movies_pros()
		file_nopros = Movies().read_movies_nopros()
		file_completely = Movies().read_movies_completely()
		reg = str(check_reg_library()).upper()
		
		if reg == 'П':  #Библиотека просмотреных
			movies = ['|'+line+'\n' for line in file_pros]
			num = len(file_pros)
		if reg == 'НП':  #Библиотека непросмотреных
			movies = ['|'+line+'\n' for line in file_nopros]
			num = len(file_nopros)
		if reg == 'ВС':  #Библиотека всех
			movies = ['|'+line+'\n' for line in file_completely]
			num = len(file_completely)

		print('-'*30)
		print(f'Всего {num}')
		print(*movies, sep='', end='')
		print('-'*30)
		
#ИЗМЕНЕНИЯ
	if rehen == 'З': 
		neil = info_neil()
		file_pros = Movies().read_movies_pros()
		file_nopros = Movies().read_movies_nopros()
		
	#ПЕРЕНОС
		if neil =='П': 
			for num, line in enumerate(file_nopros):
				print(f'{num+1}. {line}')
			print(f'<{"-"*30}>', 'Введите номер фильма для переноса||# для выхода', f'<{"-"*30}>', sep='\n')
			num_film = input()
			if num_film == '#':
				break
			num_film = int(num_film)
			file_nopros_del = [line for line in file_nopros]
			film_del = file_nopros_del[num_film-1]
			file_nopros_del.remove(film_del)
			with open(derect_two_file_noPros, 'w', encoding='utf-8') as file:
				for num, line in enumerate(file_nopros_del):
					file.write(f'{num+1}. {line}')
					file.write('\n')
			print('='*32)
			print(f'Был перенесен фильм: {film_del}')

			file_pros_dop = [line for line in file_pros]
			file_pros_dop.append(film_del)
			with open(derect_one_file_Pros, 'w', encoding='utf-8') as file:
				for num, line in enumerate(file_pros_dop):
					file.write(f'{num+1}. {line}')
					file.write('\n')

	#УДАЛЕНИЕ
		if neil == 'У': 
			reg = check_reg()
			if reg == 'П': #Просмотренные
				for num, line in enumerate(file_pros):
					print(f'{num+1}. {line}')
				print(f'<{"-"*30}>', 'Введите номер фильма для удаления||# для выхода', f'<{"-"*30}>', sep='\n')
				num_film = input()
				if num_film == '#':
					break
				num_film = int(num_film)
				file_pros_del = [line for line in file_pros]
				film_del = file_pros_del[num_film-1]
				file_pros_del.remove(file_pros_del[num_film-1])
				with open(derect_one_file_Pros, 'w', encoding='utf-8') as file:
					for num, line in enumerate(file_pros_del):
						file.write(f'{num+1}. {line}')
						file.write('\n')
				print('='*32)
				print(f'Был удален фильм: {film_del}')
		
			if reg == 'НП': #Не просмотренные
				for num, line in enumerate(file_nopros):
					print(f'{num+1}. {line}')
				print(f'<{"-"*30}>', 'Введите номер фильма для удаления||# для выхода', f'<{"-"*30}>', sep='\n')
				num_film = input()
				if num_film == '#':
					break
				num_film = int(num_film)
				file_nopros_del = [line for line in file_nopros]
				film_del = file_nopros_del[num_film-1]
				file_nopros_del.remove(film_del)
				with open(derect_two_file_noPros, 'w', encoding='utf-8') as file:
					for num, line in enumerate(file_nopros_del):
							file.write(f'{num+1}. {line}')
							file.write('\n')
				print('='*32)
				print(f'Был удален фильм: {film_del}')

	#ЗАПИСЬ
		if neil == 'З': 
			reg = check_reg()
			film = check_film()

			if film == 9**9: #Выход
				break

			if reg == 'П': #Просмотренные
				file_pros_dop = [line for line in file_pros]
				file_pros_dop.append(film)
				with open(derect_one_file_Pros, 'w', encoding='utf-8') as file:
					for num, line in enumerate(file_pros_dop):
						file.write(f'{num+1}. {line}')
						file.write('\n')

			if reg == 'НП': #Не просмотренные 
				file_nopros_dop = [line for line in file_nopros]
				file_nopros_dop.append(film)
				with open(derect_two_file_noPros, 'w', encoding='utf-8') as file:
					for num, line in enumerate(file_nopros_dop):
						file.write(f'{num+1}. {line}')
						file.write('\n')

	print('Заново? -- Д или Н')
	newly = input()
	if newly == 'Д':
		continue
	elif newly == 'Н':
		break