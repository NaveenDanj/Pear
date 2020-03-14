sys_commands = ['display' , 'exit' , 'set' , 'get' , 'calc' , 'add' , 'sub' , 'var_calc' , 'if' , 'else' , ':' , 'endif' , 'nonevar' , 'var']
command_order = []
var_list = []
key_list = {
	'add':'+',
	'sub':'-',
	'div':'/',
	'mult':'*'
}

def run(filepath):
	file = open(filepath , 'r')
	lines = file.readlines()
	file.close()
	return lines

def fetcher(commands):
	LINE_NUM = 0
	for command in commands:

		res = command.split(' ')
		for item in res:
			item = item.replace('\n', '')
			if item in sys_commands:
				command_order.append([item , LINE_NUM])

		LINE_NUM += 1

def executer(command_order):
	for command in command_order:
		if command[0] == 'display':
			mystring = commands[command[1]]
			res = mystring[ mystring.find("[")+1 : mystring.find("]") ]
			print(res)

		if command[0] == 'exit':
			exit()

		if command[0] == 'set':
			command_str = commands[command[1]]
			var_com = command_str.split(" ")


			if len(var_com) == 3:
				var_name = var_com[1]
				var_val = var_com[2].replace("\n" , "")

				var_list.append([var_name , var_val])

			elif len(var_com) > 3 and var_com[2] == 'calc':
				var_name = var_com[1]
				operator = var_com[3]
				mystring = var_com[4]
				operand = mystring[ mystring.find("<")+1 : mystring.find(">") ].split(key_list[operator])

				# print(operator , operand)
				val = calc(key_list[operator] , operand)
				if check_var(var_name , var_list) :
					update_var(var_name , val , var_list)
				else:
					var_list.append([var_name , val])

			elif len(var_com) > 3 and var_com[2] == 'var_calc':
				var_name = var_com[1]
				operator = var_com[3]
				op_str = var_com[4].replace('\n' , '')
				op_str = op_str[ op_str.find("(")+1 : op_str.find(")") ].split(key_list[operator])

				var1_name = op_str[0]
				var2_name = op_str[1]

				number_list = [get_data(var1_name , var_list)[1].replace('}' ,'').replace('{' , '') , get_data(var2_name , var_list)[1].replace('}' ,'').replace('{' , '')]

				res = calc(key_list[operator] , number_list)
				update_var(var_name , res , var_list)

		if command[0] == 'get':
			command_str = commands[command[1]].replace('\n' , '')
			res = command_str.split(" ")
			var_name = res[1]
			out = get_data(var_name , var_list)
			print(out[1])

		if command[0] == 'calc' and not (check_exist(command[1] , sys_commands)):
			command_str = commands[command[1]].replace('\n' , '')
			res = command_str.split(" ")
			operator = res[3]
			mystring = res[4]
			
			# print('operator is' , operator , key_list[operator] , operand)
			operand = mystring[ mystring.find("<")+1 : mystring.find(">") ].split(key_list[operator])
			result =  calc(key_list[operator] , operand)

			var_name = res[2]
			update_var(var_name , result , var_list)


		if command[0] == 'var_calc' and len(commands) == 3:
			command_str = commands[command[1]].replace('\n' , '').split(" ")
			operator = command_str[1]
			op_str = command_str[2]
			op_str = op_str[op_str.find("(")+1 : op_str.find(")") ].split(key_list[operator])
			
			var1_name = op_str[0]
			var2_name = op_str[1]

			number_list = [get_data(var1_name , var_list)[1].replace('}' ,'').replace('{' , '') , get_data(var2_name , var_list)[1].replace('}' ,'').replace('{' , '')]
			res = calc(key_list[operator] , number_list)
			print(res)


		if command[0] == ':':
			condition = commands[command[1]].replace("\n" , "").split(" ")
			if condition[1] == 'start' and condition[2] == 'if':
				print(condition)
				mstring = condition[3]
				cond = condition[4][ condition[4].find("[")+1 : condition[4].find("]") ]
				operator =  mstring[ mstring.find("[")+1 : mstring.find("]") ]

				if cond == 'nonvar':
					conditions = condition[5][ condition[5].find("[")+1 : condition[5].find("]") ].split("|")
					if_line_number = command[1]
					print(if_line_number)
					else_line_number = 

def check_exist(item , array):
	for i in range(len(array)):
		if item == array[i]:
			return True
	return False

def update_var(var_name , new_value , var_list):
	for i in range(len(var_list)):
		if var_list[i][0] == var_name :
			var_list[i][1] = new_value

def check_var(var_name , var_list):
	for i in range(len(var_list)):
		if var_list[i][0] == var_name :
			return True
	return False

def get_data(target , listt):
	for item in listt:
		# print(item)
		if target == item[0]:
			return item

def calc(operator , number_list):
	ret = None
	if operator == '+':
		ret = 0
		for number in number_list:
			ret += int(number)

	elif operator == '-':
		ret = int(number_list[0]) * 2
		for number in number_list:
			ret -= int(number)

	elif operator == '/':
		return int(number_list[0]) / int(number_list[1])

	elif operator == '*':
		return int(number_list[0]) * int(number_list[1])

	return ret


def if_operator_controller(condition1 , condition2 , operator ,if_line_number , else_line_number , end_line_number):
	pass



commands = run('test.pr')
fetcher(commands)
executer(command_order)
print("--------------------")
# print(var_list)
print(command_order)