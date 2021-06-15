# ボタンの番号割り
# 0〜9 -> 0〜9
# 10 = 小数点
# 11 = 足す
# 12 = 引く
# 13 = 掛ける
# 14 = 割る
# 15 = 正負切替
# 16 = パーセント
# 17 = イコール
# 18 = クリア
# 19 = バックスペース

import tkinter

WIDTH = 232
HEIGHT = 300
resultText = '0'
currentOp = ''
stackedValue = 0
isStacked = False
afterCalc = False
isPressed = False
DARK_GRAY = '#333333'
LIGHT_GRAY = '#c0c0c0'
GRAY = '#666666'

frame = tkinter.Tk()
frame.title("電卓")
frame.resizable(False, False)
frame.update_idletasks()
x = (frame.winfo_screenwidth() // 2) - (WIDTH // 2)
y = (frame.winfo_screenheight() // 2) - (HEIGHT // 2)
frame.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, x, y))

canvas = tkinter.Canvas(frame, width = WIDTH, height = HEIGHT)
canvas.pack()

def mousePressed(event):
	tag = event.widget.gettags('current')[0]
	if 'text' in tag:
		event.widget.itemconfig(str(tag).replace('text', ''), fill = LIGHT_GRAY)
	else:
		event.widget.itemconfig('current', fill = LIGHT_GRAY)

	if tag in ['zero', 'zerotext']:
		SetValueAndCalc(0)
	elif tag in ['one', 'onetext']:
		SetValueAndCalc(1)
	elif tag in ['two', 'twotext']:
		SetValueAndCalc(2)
	elif tag in ['three', 'threetext']:
		SetValueAndCalc(3)
	elif tag in ['four', 'fourtext']:
		SetValueAndCalc(4)
	elif tag in ['five', 'fivetext']:
		SetValueAndCalc(5)
	elif tag in ['six', 'sixtext']:
		SetValueAndCalc(6)
	elif tag in ['seven', 'seventext']:
		SetValueAndCalc(7)
	elif tag in ['eight', 'eighttext']:
		SetValueAndCalc(8)
	elif tag in ['nine', 'ninetext']:
		SetValueAndCalc(9)
	elif tag in ['period', 'periodtext']:
		SetValueAndCalc(10)
	elif tag in ['add', 'addtext']:
		SetValueAndCalc(11)
	elif tag in ['subtract', 'subtracttext']:
		SetValueAndCalc(12)
	elif tag in ['multiply', 'multiplytext']:
		SetValueAndCalc(13)
	elif tag in ['divide', 'dividetext']:
		SetValueAndCalc(14)
	elif tag in ['plusminus', 'plusminustext']:
		SetValueAndCalc(15)
	elif tag in ['percent', 'percenttext']:
		SetValueAndCalc(16)
	elif tag in ['equal', 'equaltext']:
		SetValueAndCalc(17)
	elif tag in ['clear', 'cleartext']:
		SetValueAndCalc(18)

def repaint(event):
	canvas.delete('all')
	paint()

def keyPressed(event):
	repaint(event)
	key = event.keysym
	if key == '0':
		SetValueAndCalc(0)
		canvas.itemconfig('zero', fill = LIGHT_GRAY)
	elif key == '1':
		SetValueAndCalc(1)
		canvas.itemconfig('one', fill = LIGHT_GRAY)
	elif key == '2':
		SetValueAndCalc(2)
		canvas.itemconfig('two', fill = LIGHT_GRAY)
	elif key == '3':
		SetValueAndCalc(3)
		canvas.itemconfig('three', fill = LIGHT_GRAY)
	elif key == '4':
		SetValueAndCalc(4)
		canvas.itemconfig('four', fill = LIGHT_GRAY)
	elif key == '5':
		SetValueAndCalc(5)
		canvas.itemconfig('five', fill = LIGHT_GRAY)
	elif key == '6':
		SetValueAndCalc(6)
		canvas.itemconfig('six', fill = LIGHT_GRAY)
	elif key == '7':
		SetValueAndCalc(7)
		canvas.itemconfig('seven', fill = LIGHT_GRAY)
	elif key == '8':
		SetValueAndCalc(8)
		canvas.itemconfig('eight', fill = LIGHT_GRAY)
	elif key == '9':
		SetValueAndCalc(9)
		canvas.itemconfig('nine', fill = LIGHT_GRAY)
	elif key == 'period':
		SetValueAndCalc(10)
		canvas.itemconfig('period', fill = LIGHT_GRAY)
	elif key == 'plus':
		SetValueAndCalc(11)
		canvas.itemconfig('add', fill = LIGHT_GRAY)
	elif key == 'minus':
		SetValueAndCalc(12)
		canvas.itemconfig('subtract', fill = LIGHT_GRAY)
	elif key == 'asterisk':
		SetValueAndCalc(13)
		canvas.itemconfig('multiply', fill = LIGHT_GRAY)
	elif key == 'slash':
		SetValueAndCalc(14)
		canvas.itemconfig('divide', fill = LIGHT_GRAY)
	elif key == 'percent':
		SetValueAndCalc(16)
		canvas.itemconfig('percent', fill = LIGHT_GRAY)
	elif key in ['equal', 'Return']:
		SetValueAndCalc(17)
		canvas.itemconfig('equal', fill = LIGHT_GRAY)
	elif key == 'c':
		SetValueAndCalc(18)
		canvas.itemconfig('clear', fill = LIGHT_GRAY)
	elif key == 'BackSpace':
		SetValueAndCalc(19)

def keyRelease(event):
	repaint(event)

def SetValueAndCalc(btnNum):
	global isPressed, afterCalc, resultText, currentOp, stackedValue, isStacked
	if btnNum == 0:
		# 0の場合
		if afterCalc or resultText == '0':
			resultText = '0'
		else:
			resultText = resultText + '0'
		isPressed = True
		afterCalc = False
	elif btnNum >= 1 and btnNum <= 9:
		# 1〜9の場合
		if afterCalc or resultText == '0':
			resultText = str(btnNum)
		else:
			resultText = str(resultText) + str(btnNum)
		isPressed = True
		afterCalc = False
	elif btnNum == 10:
		# 小数点の場合
		if '.' not in resultText:
			resultText = resultText + '.'
		if afterCalc:
			resultText = '0.'
		isPressed = True
		afterCalc = False
	elif btnNum >= 11 and btnNum <= 14:
		# +,-,×,÷の場合
		afterCalc = True
		isStacked = True
		stackedValue = float(resultText)
		if btnNum == 11:
			currentOp = '+'
		elif btnNum == 12:
			currentOp = '-'
		elif btnNum == 13:
			currentOp = '*'
		elif btnNum == 14:
			currentOp = '/'
	elif btnNum == 15:
		# プラスマイナスを切り替える
		isPressed = False
		if '-' in resultText:
			resultText = str(resultText).replace('-', '')
		else:
			resultText = '-' + resultText
	elif btnNum == 16:
		# %の場合
		afterCalc = True
		isPressed = False
		resultText = str(float(resultText) / 100)
		if resultText == '0.0':
			resultText = '0'
	elif btnNum == 17:
		# イコールの場合
		afterCalc = True
		isStacked = False
		isPressed = False
		value = float(resultText)
		if currentOp == '+':
			stackedValue += value
		elif currentOp == '-':
			stackedValue -= value
		elif currentOp == '*':
			stackedValue *= value
		elif currentOp == '/':
			if value == 0.0:
				resultText = '数値ではありません'
				return
			else:
				stackedValue /= value
		if stackedValue % 1 == 0:
			resultText = str(int(stackedValue))
		elif stackedValue == '0.0':
			resultText = '0'
		else:
			resultText = str(stackedValue)
	elif btnNum == 18:
		# クリアの場合
		isPressed = False
		afterCalc = False
		isStacked = False
		resultText = '0'
	elif btnNum == 19:
		# バックスペースが押された場合
		if isPressed:
			st = str(resultText)[:-1]
			if st == '' or st == '-':
				resultText = '0'
			else:
				resultText = st

def paint():
	global resultText, currentOp, isStacked

	# 数字表示フィールド
	canvas.create_rectangle(0, 0, WIDTH, 58, fill = 'black')

	# resultText表示
	fs = ''
	if resultText == '数値ではありません':
		fs = 24
	else:
		fs = 40

	if len(resultText) > 10:
		resultText = str(resultText)[:10]

	canvas.create_text(WIDTH - 7, 58 - 3, fill = 'white', text = resultText, font = ('Arial', fs), anchor = 'se')

	# クリアボタン
	canvas.create_rectangle(0, 58, 57, 106, fill = DARK_GRAY, tags = 'clear')
	ct = ''
	if isPressed:
		ct = 'C'
	else:
		ct = 'AC'
	canvas.create_text(30, 83, fill = 'white', text = ct, font = ('Arial', 22), tags = 'cleartext')

	# 正負切替ボタン
	canvas.create_rectangle(58, 58, 115, 106, fill = DARK_GRAY, tags = 'plusminus')
	canvas.create_line(98, 75, 78, 95, fill = 'white', tags = 'plusminustext', width = 2)
	canvas.create_text(80, 80, fill = 'white', text = '+', font = ('Arial', 22), tags = 'plusminustext')
	canvas.create_text(93, 90, fill = 'white', text = '−', font = ('Arial', 22), tags = 'plusminustext')

	# パーセントボタン
	canvas.create_rectangle(116, 58, 173, 106, fill = DARK_GRAY, tags = 'percent')
	canvas.create_text(146, 83, fill = 'white', text = '%', font = ('Arial', 22), tags = 'percenttext')

	# 割るボタン
	canvas.create_rectangle(174, 58, 231, 106, fill = 'orange', tags = 'divide')
	canvas.create_text(203, 83, fill = 'white', text = '÷', font = ('Arial', 36), tags = 'dividetext')
	if isStacked and currentOp == '/':
		canvas.itemconfig('dividetext', fill = 'black')

	# 7ボタン
	canvas.create_rectangle(0, 107, 57, 155, fill = GRAY, tags = 'seven')
	canvas.create_text(29, 131, fill = 'white', text = '7', font = ('Arial', 24), tags = 'seventext')

	# 8ボタン
	canvas.create_rectangle(58, 107, 115, 155, fill = GRAY, tags = 'eight')
	canvas.create_text(87, 131, fill = 'white', text = '8', font = ('Arial', 24), tags = 'eighttext')

	# 9ボタン
	canvas.create_rectangle(116, 107, 173, 155, fill = GRAY, tags = 'nine')
	canvas.create_text(145, 131, fill = 'white', text = '9', font = ('Arial', 24), tags = 'ninetext')

	# 掛けるボタン
	canvas.create_rectangle(174, 107, 231, 155, fill = 'orange', tags = 'multiply')
	canvas.create_text(203, 131, fill = 'white', text = '×', font = ('Arial', 36), tags = 'multiplytext')
	if isStacked and currentOp == '*':
		canvas.itemconfig('multiplytext', fill = 'black')

	# 4ボタン
	canvas.create_rectangle(0, 156, 57, 204, fill = GRAY, tags = 'four')
	canvas.create_text(29, 180, fill = 'white', text = '4', font = ('Arial', 24), tags = 'fourtext')

	# 5ボタン
	canvas.create_rectangle(58, 156, 115, 204, fill = GRAY, tags = 'five')
	canvas.create_text(87, 180, fill = 'white', text = '5', font = ('Arial', 24), tags = 'fivetext')

	# 6ボタン
	canvas.create_rectangle(116, 156, 173, 204, fill = GRAY, tags = 'six')
	canvas.create_text(145, 180, fill = 'white', text = '6', font = ('Arial', 24), tags = 'sixtext')

	# マイナスボタン
	canvas.create_rectangle(174, 156, 231, 204, fill = 'orange', tags = 'subtract')
	canvas.create_text(203, 180, fill = 'white', text = '−', font = ('Arial', 36), tags = 'subtracttext')
	if isStacked and currentOp == '-':
		canvas.itemconfig('subtracttext', fill = 'black')

	# 1ボタン
	canvas.create_rectangle(0, 205, 57, 253, fill = GRAY, tags = 'one')
	canvas.create_text(29, 229, fill = 'white', text = '1', font = ('Arial', 24), tags = 'onetext')

	# 2ボタン
	canvas.create_rectangle(58, 205, 115, 253, fill = GRAY, tags = 'two')
	canvas.create_text(87, 229, fill = 'white', text = '2', font = ('Arial', 24), tags = 'twotext')

	# 3ボタン
	canvas.create_rectangle(116, 205, 173, 253, fill = GRAY, tags = 'three')
	canvas.create_text(145, 229, fill = 'white', text = '3', font = ('Arial', 24), tags = 'threetext')

	# プラスボタン
	canvas.create_rectangle(174, 205, 231, 253, fill = 'orange', tags = 'add')
	canvas.create_text(203, 229, fill = 'white', text = '+', font = ('Arial', 36), tags = 'addtext')
	if isStacked and currentOp == '+':
		canvas.itemconfig('addtext', fill = 'black')

	# 0ボタン
	canvas.create_rectangle(0, 254, 115, 302, fill = GRAY, tags = 'zero')
	canvas.create_text(58, 277, fill = 'white', text = '0', font = ('Arial', 24), tags = 'zerotext')

	# 小数点ボタン
	canvas.create_rectangle(116, 254, 173, 302, fill = GRAY, tags = 'period')
	canvas.create_text(146, 270, fill = 'white', text = '.', font = ('Arial', 36), tags = 'periodtext')

	# イコールボタン
	canvas.create_rectangle(174, 254, 231, 302, fill = 'orange', tags = 'equal')
	canvas.create_text(203, 277, fill = 'white', text = '=', font = ('Arial', 36), tags = 'equaltext')

	canvas.tag_bind('current', '<ButtonPress-1>', mousePressed)
	canvas.tag_bind('current', '<ButtonRelease-1>', repaint)

paint()
frame.bind('<Key>', keyPressed)
frame.bind('<KeyRelease>', keyRelease)
frame.mainloop()