from flask import Flask, render_template, request, redirect, url_for
import collections
import json
app = Flask(__name__)
"""
keys = {'test':{'formykids' : "Для моих детей" , 'getmoney' : 'Хочу зарабатывать' , 'interes' : 'Мне интересно' , 'pickpython' : 'Я не знаю, просто выбери за меня'},
				"corp":{'pickpython':'Google','Good':'Microsoft',"ios":'Apple','pickpython':'Facebook'}, 'enterprise':{'Good':'Хорошо','notbad':'Средне','bad':'Плохо'},
				'getmoney':{"getjob":"Получить работу","ihavestartup":"У меня есть стартап"},
				"hardway":{"auto":"Автоматическая", "manual":"Ручная"},
				"interes":{"haveidea":'Да', "nohaveidea":"Нет :C"},
				"mob-platform":{"dm":"Android","ios":"IOS"},
				"money-platform":{"WEB":"WEB","enterprise":"Предприятие","Mobile":"Смартфоны","games":"3D/gamimg","corp":"Я хочу работать в большой корпрации.","dm":"Не имеет значения, я просто хочу денег."},
				"nohaveidea":{"easyway":"Простой путь","bestway":"Лучший путь","hardway":"Сложный путь"},
				"platform":{'WEB':"WEB",'enterprise':'Предприятие',"Mobile":"Смартфоны","games":"3D/gamimg"},
				"WEB":{"Web1":"Нет","jS":"Да"},
				"Web1":{"pickpython":"Конструктор Лего","ruby":"Пластилин","PHP":"Старая, уродливая, но любимая"}
				}
"""
@app.route('/')
def index():
		return render_template(
				'index.html'
		)   

# Vote list
poll_data = {
	 'question' : 'Какой язык программирования стоит выучить первым?',
	 'fields'   : ['C', 'C#', 'C++', 'Go', 'Java', 'JavaScript', 'PHP', 'Python', 'Ruby', 'Swift']
}
filename = 'data.txt'


""" START VOTE """

@app.route('/golos')
def root():
		return render_template(
		'poll.html',
		data=poll_data
		)

@app.route('/poll')
def poll():
		vote = request.args.get('field')
 
		out = open(filename, 'a')
		out.write( vote + '\n' )
		out.close()
 
		return render_template('thankyou.html', data=poll_data)

@app.route('/results')
def show_results():

		counter = collections.Counter()
		with open(filename) as f:
					for line in f:
						review = line.strip()
						if review:
								counter[review] += 1
		votes = dict(counter)
		retush = sorted(votes.items(), key=lambda x: x[1], reverse=True)
		return render_template(
				'results.html',
				data=poll_data,
				votes=retush,
				)

""" END VOTE """

@app.route('/test')
def test():
		return render_template(
				'test.html',
				quest="Почему вы хотите заниматься программированием?",
		)

@app.route('/ans', methods=["POST"])
def anss():
	for key, value in request.form.items():
		if value == 'formykids':
			return redirect('/kids')
		elif value == 'getmoney':
			return redirect('/getmoney')
		elif value == 'interes':
			return redirect('/interes')
		elif value == 'pickpython' or value == 'bestway' or value == 'easyway':
			return redirect('/python')
		elif value == 'getjob':
			return redirect('/money-platform')
		elif value == 'haveidea' or value == 'ihavestartup':
			return redirect('/platform')
		elif value == 'nohaveidea':
			return redirect('/nohaveidea')
		elif value == 'WEB':
			return redirect('/WEB')
		elif value == 'enterprise':
			return redirect('/enterprise')
		elif value == 'Mobile':
			return redirect('/mob-platform')
		elif value == 'hardway':
			return redirect('/hardway')
		elif value == 'manual':
			return redirect('/C')
		elif value == 'games':
			return redirect('/C++')
		elif value == 'corp':
			return redirect('/corp')
		elif value == 'bad' or value == 'notbad' or value == 'dm' or value == 'auto':
			return redirect('/Java')
		elif value == 'Good':
			return redirect('/C#')
		elif value == 'ios':
			return redirect('/Swift')
		elif value == 'jS':
			return redirect('/JS')
		elif value == 'Web1':
			return redirect('/Web1')
		elif value == 'PHP':
			return redirect('/PHP')
		elif value == 'ruby':
			return redirect('/Ruby')
		else:
			return "Error"


@app.route('/plng')
def plng():
	lng_dict= {"C":"/C","C++":"/C++","C#":"/CSharp","Java":"/Java","JS":"/JS","Scratch":"/kids","PHP":"/PHP","Python":"/Python","Ruby":"/Ruby","Swift":"/Swift"}
	return render_template(
		'plng.html',
		lng_dict=lng_dict,
		)

@app.route('/Web1')
def Web1():
	return render_template(
		'Web1.html',
		quest="Какая твоя любимая игрушка?",
		)

@app.route('/corp')
def corp():
	return render_template(
		'corp.html',
		quest="В какую компанию вы хотите устроиться?",
		)

@app.route('/enterprise')
def enterprise():
	return render_template(
		'enterprise.html',
		quest="Как ты отосишься к компании Microsoft?",
		)

@app.route('/getmoney')
def getmoney():
	return render_template(
		'getmoney.html',
		quest="",
		)

@app.route('/hardway')
def hardway():
	return render_template(
		'hardway.html',
		quest="Коробка передач?",
		)

@app.route('/interes')
def interes():
	return render_template(
		'interes.html',
		quest="Есть ли у тебя идея которую ты хочешь реаизовать?",
		)

@app.route('/mob-platform')
def mob_platform():
	return render_template(
		'mob-platform.html',
		quest=" Под какую операционную систему ты хочешь писать?",
		 )

@app.route('/money-platform')
def money_platform():
	return render_template(
		'money-platform.html',
		quest=" На какой платформе?",
		 )

@app.route('/nohaveidea')
def nohaveidea():
	return render_template(
		'nohaveidea.html',
		quest="Выбери путь обучения:",
		)

@app.route('/platform')
def platform():
	return render_template(
		'platform.html',
		quest=" На какой платформе?",
		)

@app.route('/WEB')
def WEB():
	return render_template(
		'WEB.html',
		quest=" Хочешь ли ты делать интерактивные элементы для сайта?",
		)
"""  SSS   """
@app.route('/otziv')
def about():
		return render_template(
				'otziv.html',
		)


@app.route('/reply', methods=['POST'])
def reply():
		answer = ''
		for key, value in request.form.items():
				if key == 'A':
						username = value
				if key == 'B':
						comment = value
				answer += '{}: {}\n'.format(key, value)
		with open('comments.txt', 'a') as f:
				f.write(json.dumps({
						'username': username,
						'comment': comment,
				}) + '\n')
		return render_template(
				'reply.html',
				answer = answer,
				)

@app.route('/replies')
def replies():
		comments = []
		with open('comments.txt', 'r') as f:
				for line in f:
						if line.strip():
								data = json.loads(line)
								comments.append(data)
		# return '{!r}'.format(comments)
		return render_template(
				'replies.html',
				comments=comments,
				title='List of {} comments'.format(len(comments))
		)
"""  SSS   """


""" LANGUAGE START """

@app.route('/kids')
def kids():
	return render_template(
		'lng/kids.html',
		)

@app.route('/Python')
def python():
	return render_template(
		'lng/python.html',
		)

@app.route('/C')
def C():
	return render_template(
		'lng/C.html',
		)

@app.route('/C++')
def Cpp():
	return render_template(
		'lng/Cpp.html',
		)

@app.route('/CSharp')
def CSharp():
	return render_template(
		'lng/CSharp.html',
		)

@app.route('/Java')
def Java():
	return render_template(
		'lng/Java.html',
		)

@app.route('/JS')
def JS():
	return render_template(
		'lng/JS.html',
		)

@app.route('/Ruby')
def Ruby():
	return render_template(
		'lng/Ruby.html',
		)

@app.route('/Swift')
def Swift():
	return render_template(
		'lng/Swift.html',
		)

@app.route('/PHP')
def PHP():
	return render_template(
		'lng/PHP.html',
		)

""" END LANG """




if __name__ == '__main__':
	app.run(
		port=2727,
		debug=True,
		)


			
			