# coding=utf-8    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from enum import Enum

import re, time, os, json, requests, traceback, random


DRIVER_PATH = "E:/InstallPackages/chromedriver_win32/chromedriver.exe";

"""
# 菁优账号
	'jyean': 'p2_SyR-E5vs7Cx5lVFqxSmOmZVRcLovx9qta4Q_0yVaaulz6IDIOmVqcE6AHzFLKjYm209kHlyQ_xip1ORqi8s2Q6z5eMP19xaIAm8H83dtF4QCUuIYNXEPPG80Ied8d0',
	'jye_cur_sub':'chinese2',
	'UM_distinctid':'16a71fb093252-0c3f9bcb638a84-b79183d-144000-16a71fb09333e',
	'CNZZDATA2018550':'cnzz_eid%3D1027833966-1556689497-%26ntime%3D1557165618',
	'jy_user_lbs_chinese2': '',
	'jy_user_lbs_math2': '',
	'jy' : '117CE7EE40245E9600E462E6B2416AC07C0D68A010748F3A074EF84821B834A0843D6C034D7579D3806DDA63AD38C09200BF85F0355436CB8DD404D2AD6541790A69FA9AA55EE1AA9C2BF7091686AADEEF4482BA6D24178B4187E84076943805BFC51BB6DF8F946F068F15B0CA7678A04DFA49B8CBEB884ACF264ECE4B72D40388BEEDD6ABEC77983DBD9BD3A7429FF7C7C118B419D12EB273828D3C4AEDB7C9C389F1A910574E0D7BB951916492C335EB8CF182943971B995A5150A534CFAC6FE77CD9DBE2CE8A72B15013F891421B4E01C7510101F685F7200E0A633675AA64AAE778AC44B400C251871F2591347333DBE32519EECEC676E1B1F7F1FC6E0288055C2B0958C1DEDA67338BDF885DF0FFF8C2ACECEEFB9230EAEDDB8D30AF5FB0E01A202C378930CD7EB2A23591E8681C7AA900C175038850FD0320C899A79528475D939E744D9D2F5E68162BEAAB454',
	'__RequestVerificationToken' : 'R-8l1irB9d-fWAYTKPaSluftncu-jy0jsEE-EENZrIfJjNMebZwzTg-IrCKuzF4pPBmPPvp_qN1W_RU0jyBp91oeIXVFUzYaZ73FIiCy2Dc1'
#	'jye_notice_yd_notenough' : '1|2019/5/7 02:42:52|0|false'
# 俪菌俺的小号
	'jyean': 'p2_SyR-E5vs7Cx5lVFqxSmOmZVRcLovx9qta4Q_0yVaaulz6IDIOmVqcE6AHzFLKjYm209kHlyQ_xip1ORqi8s2Q6z5eMP19xaIAm8H83dtF4QCUuIYNXEPPG80Ied8d0',
	'jye_cur_sub':'chinese2',
	'UM_distinctid':'16a71fb093252-0c3f9bcb638a84-b79183d-144000-16a71fb09333e',
	'CNZZDATA2018550':'cnzz_eid%3D1027833966-1556689497-%26ntime%3D1557227272',
	'jy_user_lbs_chinese2': '',
	'jy_user_lbs_math2': '',
	'jy' : 'F1AEAAAA2AA0A8AE235DCA28112CFC750AAFDBA5D7F9EEAF64E9FDEEF22CB99027949EF412A911084D852A7C0FD273FA422845924276EA08967A227CCC0BEB108A10D1698230CF7649A0323C05BE1863DC1A7630A4CB96DAD90129D7E34629DCDDF3687C2726E4A9A7719B7C8978523364FD56FDE44C6C1A102792D777819B45E6D5DED3750C6651C5AD52AF31DD5FD32E3663DFFC0E77F9A8C19F926635622679D1B6C9A9D5C34FC6C18A0BAE501635D8DDB46FC01A29C42C30FE9FB3CE08E8DBACC81929F17C8CB947C5D4DCBF4E6DF2F21F87B8B14B62FD30920D74FE162902B6B73B82BEE49A11CB9AC16AC420E3F8E56CBA3C58F9747A18032AD977A3F6E4A8AF7AE0D28AA92F6F81B2A6E5C2AA8A04B697CD1AD44769B3E873AF2AFD11A26D685DA42DBEBA1531485A5ACBB2161BCBB36F7CCE0EA2C2BB53058C72FBB3A3887ACACC13DB339A77FEF1866F137C',
# 大号
	'jyean': 'p2_SyR-E5vs7Cx5lVFqxSmOmZVRcLovx9qta4Q_0yVaaulz6IDIOmVqcE6AHzFLKjYm209kHlyQ_xip1ORqi8s2Q6z5eMP19xaIAm8H83dtF4QCUuIYNXEPPG80Ied8d0',
	'jye_cur_sub':'history2',
	'UM_distinctid':'16a71fb093252-0c3f9bcb638a84-b79183d-144000-16a71fb09333e',
	'CNZZDATA2018550':'cnzz_eid%3D1027833966-1556689497-%26ntime%3D1557227272',
	'jy_user_lbs_chinese2': '',
	'jy' : '748E6273CB03B0988B0BA356763731F705219DE74942E93271D543AAD360F6B5F5509BC4340C86AA86EF1E3280BCAEB7E5B3902A300F20F71433CB25BA9807679BA361BB2A4CFEDD250B245DB799843060FEF0A35458DEFBE7A9132F6BBFDB29B90803B947E256BA6FCC89DCC4750142DE90E9E253B5945BCD685A3CB4897EF3C2D16B5B7B5110F056AE1AA4733448C4FBCD2E45590344D64211EDD2503825A1A56FF0684F2D98965A70243A8E26DB91D66CB03F4249CD444C18A0968A27946274629759A905DD644884C1D9B12C19D1D343D93B21BEF090109707B300E648360126A24D6379FE8B8C94BD43CB55BC9A9C0E8830000AEF4FB38CE98B978592BD7E002DC86DDD12B74F2541F638B61D9716D41CFC19930AD9B3CA6C4E05A7A0DFA96E46D47417F8B6B9E05C6A7E6C057869083891F83661536F0E147D1B4ECA0984DBC675DCC6D78581078B92737F6F20',
	'jye_notice_yd_notenough' : '1|2019/5/7 20:04:47|0|false'
"""

COOKIES = {	
	'jyean': 'p2_SyR-E5vs7Cx5lVFqxSmOmZVRcLovx9qta4Q_0yVaaulz6IDIOmVqcE6AHzFLKjYm209kHlyQ_xip1ORqi8s2Q6z5eMP19xaIAm8H83dtF4QCUuIYNXEPPG80Ied8d0',
	'jye_cur_sub':'chinese2',
	'UM_distinctid':'16a71fb093252-0c3f9bcb638a84-b79183d-144000-16a71fb09333e',
	'CNZZDATA2018550':'cnzz_eid%3D1027833966-1556689497-%26ntime%3D1557227272',
	'jy_user_lbs_chinese2': '',
	'jy_user_lbs_math2': '',
	'jy' : 'F1AEAAAA2AA0A8AE235DCA28112CFC750AAFDBA5D7F9EEAF64E9FDEEF22CB99027949EF412A911084D852A7C0FD273FA422845924276EA08967A227CCC0BEB108A10D1698230CF7649A0323C05BE1863DC1A7630A4CB96DAD90129D7E34629DCDDF3687C2726E4A9A7719B7C8978523364FD56FDE44C6C1A102792D777819B45E6D5DED3750C6651C5AD52AF31DD5FD32E3663DFFC0E77F9A8C19F926635622679D1B6C9A9D5C34FC6C18A0BAE501635D8DDB46FC01A29C42C30FE9FB3CE08E8DBACC81929F17C8CB947C5D4DCBF4E6DF2F21F87B8B14B62FD30920D74FE162902B6B73B82BEE49A11CB9AC16AC420E3F8E56CBA3C58F9747A18032AD977A3F6E4A8AF7AE0D28AA92F6F81B2A6E5C2AA8A04B697CD1AD44769B3E873AF2AFD11A26D685DA42DBEBA1531485A5ACBB2161BCBB36F7CCE0EA2C2BB53058C72FBB3A3887ACACC13DB339A77FEF1866F137C',
}

SUBJECT_CONFIG = {
	'Chinese': {
		'BASE_URL' : "http://www.jyeoo.com/chinese2/ques/search?f=0&q=1dc14bc4-ddf8-4ea9-9c7a-b767c29c3043~01525d06-ed64-4403-ac49-1b8c93b38f2a~&lbs=&ct=1&pd=1",
		'START_PAGE' : 8,
		'END_PAGE' : 10,
		'OUT_FILE' : "subject_0.que",
	},
	'Math': {
		'BASE_URL' : "http://www.jyeoo.com/math2/ques/search?f=0&q=b6174fb4-1c52-4186-a1d0-a79ec6087045~acfe19cd-7319-4d79-8409-54462213d84d~&lbs=&ct=1&pd=1",
		'START_PAGE' : 10,
		'END_PAGE' : 15,
		'OUT_FILE' : "subject_1.que",
	},
	'English': {
		'BASE_URL' : "http://www.jyeoo.com/english2/ques/search?f=0&q=917ff14b-88db-498e-a1be-df2d139a5f48~c86b243a-69fd-4fa4-8f83-f5ec7e88b690~&lbs=&ct=1&pd=1",
		'START_PAGE' : 8,
		'END_PAGE' : 10,
		'OUT_FILE' : "subject_2.que",
	},
	'Physics': {
		'BASE_URL' : "http://www.jyeoo.com/physics2/ques/search?f=0&q=18497ca3-5cd5-4cb4-8e9c-fc1fba93c48a~565d51da-3874-4ea9-b1c1-4ce31dbb7f00~&lbs=&pd=1",
		'START_PAGE' : 6,
		'END_PAGE' : 10,
		'OUT_FILE' : "subject_3.que",
	},
	'Chemistry': {
		'BASE_URL' : "http://www.jyeoo.com/chemistry2/ques/search?f=0&q=732ab9a0-615a-45ea-a1b1-9a1d3383ff9c~e2678114-6989-4b1e-b03c-869a7d16979d~&lbs=&ct=1&pd=1",
		'START_PAGE' : 6,
		'END_PAGE' : 10,
		'OUT_FILE' : "subject_4.que",
	},
	'Biology': {
		'BASE_URL' : "http://www.jyeoo.com/bio2/ques/search?f=0&q=6d0fd80e-4c56-4362-8465-74f7f1907795~8fe66559-614a-4bfa-b2f2-6245f6580f61~&lbs=&ct=1&pd=1",
		'START_PAGE' : 6,
		'END_PAGE' : 10,
		'OUT_FILE' : "subject_5.que",
	},
	'Politics': {
		'BASE_URL' : "http://www.jyeoo.com/politics2/ques/search?f=0&q=c9981b65-3413-4ac2-a16d-972687981f36~50d705e5-9365-428b-a4a8-08982d0ae88e~&lbs=&ct=1&pd=1",
		'START_PAGE' : 6,
		'END_PAGE' : 10,
		'OUT_FILE' : "subject_6.que",
	},
	'History': {
		'BASE_URL' : "http://www.jyeoo.com/history2/ques/search?f=0&q=c6c3584c-5bc2-46c3-86e9-229624073f6b~5a8a4048-bea1-4afe-83ad-2971bb312937~&lbs=&ct=1&pd=1",
		'START_PAGE' : 6,
		'END_PAGE' : 10,
		'OUT_FILE' : "subject_7.que",
	},
	'Geography': {
		'BASE_URL' : "http://www.jyeoo.com/geography2/ques/search?f=0&q=726fb396-f7a1-4c0a-8f8d-3e6233835363~ffab8dde-74ed-4304-a3fc-c82dadd934e9~&lbs=&ct=1&pd=1",
		'START_PAGE' : 6,
		'END_PAGE' : 10,
		'OUT_FILE' : "subject_8.que",
	}
}

def LOAD_CONFIG(subject):

	BASE_URL = SUBJECT_CONFIG[subject]['BASE_URL']
	START_PAGE = SUBJECT_CONFIG[subject]['START_PAGE']
	END_PAGE = SUBJECT_CONFIG[subject]['END_PAGE']
	OUT_FILE = SUBJECT_CONFIG[subject]['OUT_FILE']

	return BASE_URL,START_PAGE,END_PAGE,OUT_FILE 

SUBJECT = 'History'

BASE_URL,START_PAGE,END_PAGE,OUT_FILE = LOAD_CONFIG(SUBJECT)

SHOW_LOG = True

# 定位节点
# Chinese:
# BASE_URL = "http://www.jyeoo.com/chinese2/ques/search?f=0&q=1dc14bc4-ddf8-4ea9-9c7a-b767c29c3043~01525d06-ed64-4403-ac49-1b8c93b38f2a~&lbs=&ct=1&pd=1"
# Math:
# BASE_URL = "http://www.jyeoo.com/math2/ques/search?f=0&q=b6174fb4-1c52-4186-a1d0-a79ec6087045~acfe19cd-7319-4d79-8409-54462213d84d~&lbs=&ct=1&pd=1"

# 设定
# 获取解析
GET_DESC = False

# 获取图片题目
GET_IMG = True

# 获取公式题目
GET_FORMAT = False

# 图片缩放
IMG_SIZE_RATE = 0.8

# 页范围（左开右闭）
# Chinese:
# START_PAGE = 6
# END_PAGE = 10
# Maths
# START_PAGE = 1
# END_PAGE = 10

# 输出文件
# Chinese
# OUT_FILE = "subject0.que"
# Math:
# OUT_FILE = "subject1.que"

IMG_FILE_PATH = "pictures"

# 等待
FIRST_DELTA_STOP = 5

GET_DELTA_STOP = 3

NEXT_PAGE_STOP = 2

DESC_CLOSE_DELTA_STOP = 0.5

SPACE_REGEXP = r'(&nbsp;)'

FILTER_REGEXP = r'</?(br|input|a|div|em|label|span|table|td|font|tbody|tr|img|!--).*?/?>'

IMAGE_REGEXP = r'< *(img).+?src="(.*?)"/?>'

MATH_FORMAT_REGEXP = r'< *(span)[^>]+?class="MathJye".*?>(.*?)</span>'

QUAD_REGEXP = r'('+IMAGE_REGEXP+r'|'+MATH_FORMAT_REGEXP+r')'

# 元素获取
SHOWANSWER_ID = "isAnswer"

CONTENT_CLASS = "mid-content"

DESC_CONTENT_CLASS = "body-content"

QUESTION_ELEMENT_CLASS = "QUES_LI"

BOTTOM_LAYER_CLASS = "fieldtip"

NEXT_PAGE_XPATH = "//a[@class='next']"

CLOSE_DESC_BUTTON_CLASS = "smbtn hclose" #"//input[@class='smbtn hclose']"

ANSWER_XPATH_FOR_OUTTER_Q = ".//label[@class='s']"

ANSWER_XPATH_FOR_DESC_Q = ".//input[@checked='checked']"

class ErrorType(Enum):
	# Common
	NotGetImage		= 1 # 不取图片题目
	NotGetFormat	= 2 # 不取公式题目


class ErrorException(Exception):

	error_dict = {
		# Common
		ErrorType.NotGetImage:   "题目包含图片",
		ErrorType.NotGetFormat:  "题目包含公式",
	}

	def __init__(self, error_type: ErrorType):
		self.error_type = error_type
		self.msg = ErrorException.error_dict[error_type]

	def __str__(self):
		return self.msg

def setupDriver(driver_path, base_url, cookies):

	driver = webdriver.Chrome(driver_path)

	driver.get(base_url)

	time.sleep(FIRST_DELTA_STOP)
	setupCookies(driver, cookies)
	time.sleep(FIRST_DELTA_STOP)

	driver.get(base_url)

	return driver

def setupCookies(driver, cookies):

	for key in cookies:
		driver.add_cookie({'name':key, 'value':cookies[key]})

def waitForClass(base, name, timeout=10):
	return WebDriverWait(base, timeout).until(
		EC.presence_of_element_located((By.CLASS_NAME, name))
	)

def getContent(driver):

	waitForClass(driver, CONTENT_CLASS)
	contents = driver.find_elements_by_class_name(CONTENT_CLASS)
	return contents[len(contents)-1]

def showAnswer(driver):

	btn = driver.find_element_by_id(SHOWANSWER_ID)
	btn.click()

def getNextPage(driver):

	return driver.find_element_by_xpath(NEXT_PAGE_XPATH)

def getAllQuestions(driver, start, end):
	if SHOW_LOG: print("Getting questions from "+str(start)+" to "+str(end)+" :")

	showAnswer(driver)

	questions = []
	page = start
	try:
		while page < end:
			if SHOW_LOG: print("Current page: "+str(page))
			driver.execute_script("goPage("+str(page)+")")
			questions.extend(getQuestions(driver))
			page += 1

		#for i in range(end-start+1):
		#	next = getNextPage(driver)
		#	next.click()
			#time.sleep(NEXT_PAGE_STOP)

	except Exception as e:
		traceback.print_exc()
		if SHOW_LOG: print("ERROR: "+str(e))

	return questions

def getQuestions(driver):

	content = getContent(driver)

	questions = content.find_elements_by_class_name(QUESTION_ELEMENT_CLASS)

	question_objs = []
	for question in questions:
		try:
			question_objs.append(getQuestion(driver, question))
		except Exception as e:
			traceback.print_exc()
			if SHOW_LOG: print("ERROR: "+str(e))

	return question_objs
	
def getQuestion(driver, question):

	question_obj = {}

	bottom = question.find_element_by_class_name(BOTTOM_LAYER_CLASS)

	loadOuterQuestion(question, bottom, question_obj)

	#close = driver.find_element_by_xpath(CLOSE_DESC_BUTTON_XPATH)
	if GET_DESC:
		desc_btn = bottom.find_element_by_tag_name("a")
		desc_btn.click()

		desc_content = waitForClass(driver, DESC_CONTENT_CLASS)

		try:
			loadDescription(desc_content, question_obj)
			if SHOW_LOG: print ("Success to get description!")
		except:
			if SHOW_LOG: print ("Fail to get description!")

		driver.execute_script("document.getElementsByClassName('"+CLOSE_DESC_BUTTON_CLASS+"')[0].click();")

		time.sleep(DESC_CLOSE_DELTA_STOP)

	if SHOW_LOG: print(question_obj)

	return question_obj

def loadOuterQuestion(question, bottom, question_obj):
	pt1 = question.find_element_by_class_name("pt1")
	pt2 = question.find_element_by_class_name("pt2")

	infos = bottom.find_elements_by_tag_name("span")

	choices = pt2.find_elements_by_tag_name("td")
	choice_objs = []

	question_obj['pictures'] = []

	question_obj['title'] = convert2Text(pt1, question_obj)

	for choice in choices:

		ans = choice.find_elements_by_xpath(ANSWER_XPATH_FOR_OUTTER_Q)
		text = convert2Text(choice, question_obj)

		choice_objs.append({'text':text,'ans':len(ans) > 0})

	question_obj['choices'] = choice_objs

	if len(infos) >= 4:
		question_obj['level'] = infos[3].text

	return question_obj

def loadDescription(content, question_obj):

	question = waitForClass(content, QUESTION_ELEMENT_CLASS)

	pt1 = question.find_element_by_class_name("pt1")
	pt2 = question.find_element_by_class_name("pt2")
	pt5 = question.find_element_by_class_name("pt5")
	pt6 = question.find_element_by_class_name("pt6")
	pt7 = question.find_element_by_class_name("pt7")

	choices = pt2.find_elements_by_tag_name("td")
	choice_objs = []

	question_obj['title'] = convert2Text(pt1, question_obj)

	for choice in choices:

		ans = choice.find_elements_by_xpath(ANSWER_XPATH_FOR_DESC_Q)
		text = convert2Text(choice, question_obj)

		choice_objs.append({'text':text,'ans':len(ans) > 0})

	question_obj['choices'] = choice_objs

	question_obj['description'] = convert2Text(pt5, question_obj)+'\n'
	question_obj['description'] = convert2Text(pt6, question_obj)+'\n'
	question_obj['description'] = convert2Text(pt7, question_obj)+'\n'

	return question_obj

def convert2Text(obj, question_obj):
	html = obj.get_attribute("innerHTML")
	if SHOW_LOG: print("Origin: " + str(html))

	html_list = list(html)

	formats = obj.find_elements_by_class_name("MathJye")
	format_cnt = 0

	if SHOW_LOG: print("Formats len:"+str(len(formats)))

	if len(formats) > 0 and not GET_FORMAT:
		raise ErrorException(ErrorType.NotGetFormat)

	imgs = obj.find_elements_by_tag_name("img")
	img_cnt = 0

	if SHOW_LOG: print("Images len:"+str(len(imgs)))

	if len(imgs) > 0 and not GET_IMG:
		raise ErrorException(ErrorType.NotGetImage)

	pictures = question_obj['pictures']
	quad_cnt = len(pictures)

	search_objs = re.finditer(QUAD_REGEXP, html, re.I)

	for search_obj in search_objs:
		if search_obj:

			if SHOW_LOG: print(search_obj)

			size = 96
			quad_id = quad_cnt

			if search_obj.group(2) == 'img':
				if not GET_IMG:
					raise ErrorException(ErrorType.NotGetImage)

				img = imgs[img_cnt]
				url = img.get_attribute("src")
				img_name = str(random.randint(0, 9999))+url.split('/')[-1]
				size = img.size['width']*IMG_SIZE_RATE

				path = download(url, img_name)

				if path in pictures:
					quad_id = pictures.index(path)
				else:
					pictures.append(path)
					quad_cnt += 1
				
				img_cnt += 1

			else:
				if not GET_FORMAT:
					raise ErrorException(ErrorType.NotGetFormat)

				fmt = formats[format_cnt]

				format_cnt += 1

			index = search_obj.span()[0]

			quad_txt = '<nbr><quad id=%d size=%d width=1 />'%(quad_id, size)
			html_list.insert(index, quad_txt)

	#for ft in formats:
	html = ''.join(html_list)

	text = re.sub(FILTER_REGEXP, '', html)
	text = re.sub(SPACE_REGEXP, ' ', text)

	text = text.replace('<nbr>','<br>')

	question_obj['pictures'] = pictures

	if SHOW_LOG: print("Processed: " + str(text))
	return text

def download(url, filename):

	path = os.path.join(IMG_FILE_PATH, filename)
	
	if os.path.exists(path):
		if SHOW_LOG: print('file exists!')
		return path

	try:

		r = requests.get(url, stream=True, timeout=60)
		r.raise_for_status()
		
		with open(path, 'wb') as f:
		
			for chunk in r.iter_content(chunk_size=1024):
		
				if chunk:  # filter out keep-alive new chunks
					f.write(chunk)
					f.flush()
		
		return path
	except KeyboardInterrupt:

		if os.path.exists(filename):
			os.remove(filename)
		raise KeyboardInterrupt

	except Exception:

		traceback.print_exc()

		if os.path.exists(filename):
			os.remove(filename)


driver = setupDriver(DRIVER_PATH, BASE_URL, COOKIES);

time.sleep(GET_DELTA_STOP)

questions = getAllQuestions(driver, START_PAGE, END_PAGE)

print(questions)

total = len(questions)

questions_data = {
	'subject': SUBJECT,
	'from': START_PAGE,
	'to': END_PAGE-1,
	'data': questions
}

json_data = json.dumps(questions_data, ensure_ascii=False)

with open(OUT_FILE, 'w', encoding='utf-8') as file:
	file.write(json_data)

print("Total: "+str(total))

"""
[{"title": "（2018秋•玉泉区校级期末）填写在下面横线上的语句，最恰当的一项是（　　）\n     余光中坦言，他一度自称“右手写诗，左手写散文”，意思是____________．但没想到的是，更多人却对他的 散文表示更多的好评。于是他就改变了初衷，把诗歌和散文当成自己的两只眼睛，双眼并用，更加立体形象地 看事物，看人生。", "choices": [{"text": "A．散文是自己最擅长的主要文学体裁，诗歌是自己的最爱", "ans": False}, {"text": "B．诗歌是自己主要创作的文学体裁，散文也时有问世", "ans": True}, {"text": "C．散文和诗歌是自己创作的两类文体，左右皆能开弓", "ans": False}, {"text": "D．诗歌和散文是自己创 作的两大领域，两者不可偏废", "ans": False}], "level": "难度：0.7", "description": "【分析】\n本题考查了学生表达简明、连贯、得体的能力，考生做该题前，要认真读题，分析空白处与前后语句的关系，做到 瞻前顾后，准确填写。\n【解答】\n本题需要结合上下文来判断，结合上文“右手写诗，左手写散文”，应先 谈诗，再谈散文，结合下文“于是他就改变了初衷，把诗歌和散文当成自己的两只眼睛，双眼并用”，可知原 来余光中是注意诗而不注重散文的，因此，可以确定答案为B项。\n\n答案：\nB。\n【点评】\n本题以补写句 子的形式考查学生语言表达简明、连贯、准确的能力，学生应联系前后文语境来思考。解答时注意：①阅读全 段，了解文段性质和内容，确定中心；②要分清句间上下文的逻辑关系，确定句子的性质；③注意标点符号的 暗示作用：含义、选词、句式；④结合文本，根据字数要求，概括答案。\n"}
,{"title": "（2018•广西模拟）下列对联描写的内容与使用场合对应正确的一组是（　　）\n①音乐室：阳春白雪虽然和寡，流水高山但觅知音。\n②科技馆：究古今往事之踪迹，昭人类社会之兴衰。\n③书 画室：心驰山水一窗闲情，笔走龙蛇满室墨香。\n④档案室：纳百川之流成大海，通千古之典显文才。\n⑤实 验室：纸上得来始终觉浅，绝知此事定要躬行。", "choices": [{"text": "A．①②④", "ans": False}, {"text": "B．①③④", "ans": False}, {"text": "C．③④⑤", "ans": False}, {"text": "D．①③⑤", "ans": False}], "level": "难度：0.9"}
,{"title": "（2018秋•蚌山区校级期中）对下面这首诗的赏析，不恰当的一项是（　　）\n偶  然\n 徐志摩\n我是天空里的一片云，\n偶尔投影在你的波心--\n你不必讶异，\n更无须欢喜--\n在转瞬间消灭了踪 影。\n\n你我相逢在黑夜的海上，\n你有你的，我有我的，方向；\n你记得也好，\n最好你忘掉，\n在这交会 时互放的光亮！", "choices": [{"text": "A．这首诗把“偶然”这样一个极为抽象的时间副词形象化，充满 情趣，富有哲理，不但珠圆玉润，朗朗上口，而且余味无穷，溢于言外。", "ans": False}, {"text": "B．此诗写的是两件比较实在的事情，一是天空里的云偶尔投影在水里的波心，二是“你”“我”（都是象征性的意 象）相逢在海上。", "ans": False}, {"text": "C．如果我们用“我和你”“相似”之类的标题，当会富有诗味。", "ans": True}, {"text": "D．“云”、“波”、“你”、“我”、“黑夜的海”、“互放的光亮”等 意象及其之间的关系构成，都可以因为读者个人情感阅历的差异，及体验强度的深浅而进行不同的理解。", "ans": False}], "level": "难度：0.7", "description": "【分析】\n考查学生对于文章标题的理解，标题要 解释主旨思想，要结合全诗内容，把握诗歌主旨。\n\n赏析：\n        徐志摩这首《偶然》，很可能仅仅是 一首情诗，是写给一位偶然相爱一场而后又天各一方的情人的。不过，这首诗的意象已超越了它自身。我们完 全可以把此诗看作是人生的感叹曲。人生的路途上，有着多少偶然的交会，又有多少美好的东西，仅仅是偶然 的交会，永不重复。无论是缠绵的亲情，还是动人的友谊，无论是伟大的母爱，还是纯真的童心，无论是大街 上会心的一笑，还是旅途中倾心的三言两语，都往往是昙花一现，了无踪影。那些消逝了的美，那些消逝的爱 ，又有多少能够重新降临。时间的魔鬼带走了一切。对于天空中的云影偶尔闪现在波心，实在是“不必讶异， 更无须欢喜。”更何况在人生茫茫无边的大海上，心与心之间有时即使跋涉无穷的时日，也无法到达彼岸。每 一个人都有每一个人的方向，我们偶然地相遇，又将匆匆地分别，永无再见的希望。那些相遇时互放的“光亮 ”，那些相遇时互相倾注的情意，“记得也好，最好你忘掉”。 诗人领悟到了人生中许多“美”与“爱”的消逝，书写了一种人生的失落感。这就是这首诗深含的人生奥秘与意蕴。\n         诗人的感情是节制的，情态是潇洒的。把最难以割舍、最可珍贵的东西消逝后，而发生的失落感，用了貌似不经意的语调予以表现，使这 首诗不仅在外观上，达到了和谐的美，更在内在的诗情上，特别地具有一种典雅的美。诗的上下两段中的中间 两句，“你不必讶异，更无须欢喜”与“你记得也好，最好你忘掉”，蕴涵了非常曲折的心态，非常细腻入微 的情意。一方面，有克里丝荻娜•罗塞提（1830-1894年，英国维多利亚时代的女诗人）在《记住我》中所写的 “我情愿你忘记而面带笑容，也不愿你记住而愁容戚戚”之韵味；另一方面，也可体会到一种在命运面前无可 奈何的、故作达观的苦涩情调。这两方面，构成了一个立体的、模糊的审美体，不断的思索、体会，不同侧面 的观赏、玩味，都会有新鲜的感悟。显示了相当典雅的情趣。\n       徐志摩在这样短短的小诗中，用了那么单纯的意境，那么谨严的格式，那么简明的旋律，点化出一个朦胧而晶莹，小巧而无垠的世界。我们漫步在这 个世界之中，生发出多少人生的慨叹，多少往事的追怀，多少往事的回味，……但，并不如泣如诉，更不呼天 抢地。我们只是缓缓而有点沉重地漫步，偶尔抬头仰望，透过葡萄架或深蓝的云彩，恰有一朵流星飞逝而过， 我们心中，升起了缕缕淡淡的哀伤。但仍然漫步，那缓缓而又有点沉重的足音，如一个“永恒”，驻留在夜的 天空。\n        不失轻盈，不失飘逸，却总是掩饰不住现实的悲伤，情感深处隐伏着一丝淡淡的失落。诗人 对于美，对于人生，并不是看得可有可无的，而是怀着深深的眷恋，执着的追求，只是“美”抑或人生的其他 ，都像天空中的云影，黑夜海上的光亮，在瞬间都无影无踪。他有憧憬，同时又无法摆脱一丝淡淡的哀伤。“ 你记得也好，最好你忘掉”似乎达观，超脱。但在审美心理上，却并非如此，“最好你忘掉”，其实是最不能 忘掉。没有一点超脱，没有一点可有可无。有的是现实的哀伤，是一个真实的人，执着于生活的人，执着于理 想的人，在屡遭失意中唱出的歌。憧憬与绝望，悲哀与潇洒，奇妙地交织在一起。是一个纯诗人的哀感。他的 潇洒与飘逸，也多半是他为了追求典雅的美，节制自己的感情而来的。\n        徐志摩处在一个贫困的国度 最黑暗的年代，他满怀着“美”的希望，在时代的夹缝中苦苦追寻着理想的光芒，但都如海滩上的鲜花，一朵 朵在瞬间枯萎。他的歌喉，在“生活的阴影”逼迫下，最后变得暗哑、干涩。即使早期一些诗，如“我不知道 风在哪一个方向吹”等，虽然那么轻柔，那么飘逸，但仔细体味，也无不让人感伤。写于1926年的《偶然》， 也是一样，诗的深层信息中荡漾着淡淡的哀伤。诗人无意投身时代火热的斗争，也无意于表现所谓的“时代本 质”，但时代的苦难，也同样曲曲折折地映射在一个真纯诗人的心灵深处。\n【解答】\nC．“如果我们用‘我和你’‘相似’之类的标题，当会富有诗味”错，徐志摩这首诗歌是写给一位偶然相爱一场而后又天各一方的 情人的，这首诗的意象已超越了它自身。我们完全可以把此诗看作是人生的感叹曲。人生的路途上，有着多少 偶然的交会，又有多少美好的东西，仅仅是偶然的交会，永不重复。诗人领悟到了人生中许多“美”与“爱” 的消逝，书写了一种人生的失落感。根据对诗歌的主题分析，可知，用“偶然”可以更好的揭示诗歌的主要思 想内容。\n故选：C。\n【点评】\n如何鉴赏诗歌：\n一、看类型。\n从诗歌内容的角度来看，古典诗歌的考查基本类型有以下几类。①送别类。②怀古类。③思乡怀人类。表达对家乡或亲人思念为主。④战争或边塞类。 ⑤闲适类。⑥借景抒情类。⑦托物言志类。⑧爱情类。⑨民生类。 以上九种类弄，只要学生掌握住基本的阅读水平，在认真阅读原诗二至三遍后，基本可以定住类型。\n二、定感情。\n意象找到之后，全诗感情自然显现 。能够表现诗歌感情色彩的词语有：愉悦、欢快、激愤、沉痛、悲愤、哀伤、悲凉、赞美、仰慕、惜别、依恋 、豪迈、闲适、恬淡、迷恋、热爱、忧愁、寂寞、伤感、孤独、烦闷、坚守节操、忧国忧民等。\n三、定主旨 。\n即确定诗歌所表现的思想内容，这是诗歌创作的核心，同时也是诗歌鉴赏的核心。诗歌的思想内容不外乎 以下几个方面：热爱祖国大好河山、忧国忧民、怀古伤今、反对战争、追求和平、蔑视权贵、愤世嫉俗、怀才 不遇、寄情山水、归隐田园、登高览胜、惜春悲秋、忆友怀旧、思乡念亲、相知相亲、别恨离愁等。\n四、找 意象（典故）。\n诗歌鉴赏的重点从某种意义上说就是正确把握诗歌所描写的意象，即诗歌中所描写的形象（ 人、物、景、事）。而古代诗歌当中许多的意象都是有它们各自的喻意的。虽然这种意象的喻意在不同的意境 当中有可能有不同，但多数情况之下却是有其共通之处的\n五、找技巧。\n一首诗歌写的好坏，与它所采用的 表达技巧有着密不可分的关系，而表达技巧又要从表达方式、修辞手法，表现手法等三个方面去分析。\n"}
,{"title": "（2018春•秦州区校级月考）下列句子中，没有语病的一项是（　　）", "choices": [{"text": "A．为适应人民群众对高校招生信息公开工作的新要求，进一步推进高校招生“阳光工程”，教育部决定大力推进高校招生信息公开工作，增强社会对招生工作的监督", "ans": False}, {"text": "B．食品安全，直接关系到人们的生活质量和身体健康。政府应该对假冒伪劣和黑心食品坚决进行查处，并且让不法分子付出 昂贵的代价", "ans": False}, {"text": "C．网络购物之所以如此蓬勃兴起，原因很多，包括新一代互联网技术的推动，传统企业电子商务的转型，以及消费者年龄结构的年轻化和消费习惯的变化等等", "ans": True}, {"text": "D．习近平主席带领新一届中央领导集体，接过历史的接力棒，以稳健扎实、积极进取推进各项工作，一项项重大举措陆续出台", "ans": False}], "level": "难度：0.9", "description": "【分析】\n本题考查病句的辨析及修改能力，要结合常见病句类型来分析语句。常见的病句类型有语序不当、搭配不当、成分残 缺或赘余、结构混乱、表意不明、不合逻辑。如果遇到难以辨别错误类型的句子，可以按病句类型一一衡量， 也可以通过划分句子结构来辨明错误类型，同时结合语感以及一些常见语病的特征进行判断。\n【解答】\nA．搭配不当，“增强…监督”搭配不当，“增强”改成“加强”；\nB．并列不当，“假冒伪劣和黑心食品”概念交叉，删去“和黑心食品”；\nC．正确；\nD．成分残缺，在“权极进取”后加“的姿态”；\n故选：C。\n【点评】\n搭配不当：\n这类病句中最常见的句式是“是否（能否、有无）……是……”，即前面用肯定+否定的选择形式，后面只用肯定的或否定的形式。修改的原则是使前后一致。\n专家认为成分搭配不当的现象主要有 ：主谓搭配不当、动宾搭配不当、主宾搭配不当、修饰成分与中心词搭配不当、关联词搭配不当、一面与两面 搭配不当。\n1、主谓搭配不当\n主要表现为谓语不能陈述主语，有时主语或谓语由联合短语充当，其中一部分不搭配。\n2、动宾搭配不当\n3、主宾搭配不当\n4、修饰成分与中心词搭配不当\n（1）定语和中心语搭配不 当\n（2）状语和中心语搭配不当\n（3）补语和中心语搭配不当\n5、关联词搭配不当\n6、一面与两面搭配不 当\n"}
,{"title": "（2017秋•天门期末）下列各句中加点成语的使用，全都正确的一项是（　　）\n①进入 大学，很多学生不适应新的节奏，平时功课抓得不紧，考前复习拿起书感觉八面受敌，怎么也读不明白。\n② 和张先生打过交道的人，都知道他做研究很扎实，性格外圆内方，为人处世注重一个“度”字，所以都敬佩他 、尊重他。\n③在第九届城市运动会男子篮球决赛中，国税局代表队在比分落后的情况下奋力拼搏，最后反戈 一击，以68：56的比分战胜对手。\n④许多练习书法的人都有过这样的感受，如果有机会和同道中人一起坐而 论道，认真听取名家的建议，是提高自身书法水平的一条捷径。\n⑤有些刚开始创业的人，对功成名就的企业 家盲目崇拜，对大企业、名企业模式亦步亦趋，结果吃了不少苦头。\n⑥在世界格局多极化的今天，那些惯于 以邻为壑、给周边地区带来麻烦的国家，在国际社会中注定交不到真朋友。", "choices": [{"text": "A．① ②⑤", "ans": False}, {"text": "B．②⑤⑥", "ans": True}, {"text": "C．③④⑥", "ans": False}, {"text": "D．①③④", "ans": False}], "level": "难度：0.7", "description": "【分析】\n本题考查正确 使用成语的能力。成语的考查是命题的一个常项。主要侧重同义成语的选择、成语使用正误等两种方式。考查 重点是测试那些常见但又容易用错的成语。\n【解答】\n①八面受敌：是指功力深厚，能应付各种情况。这里 是说考前复习使感觉面对的问题很多，而不是说自己功力深厚，不合语境；\n②外圆内方：指表面随和，内心 严正。此处使用正确；\n③反戈一击：调转矛头，向自己原来的阵营进攻，这里说的是国税局代表队在比分落 后的情况下奋力拼搏，最后反败为胜，没用谁调转了矛头进攻自己的阵营，使用此成语望文生义；\n④坐而论 道：原指坐着议论政事，后泛指空谈大道理，这里是说要和同样热爱书法的人交流心得，不是空谈大道理，用 在此句中不当；\n⑤亦步亦趋：比喻由于缺乏主张，或为了讨好，事事模仿或追随别人。此处使用正确；\n⑥ 以邻为壑：拿邻国当做大水坑，把本国洪水排泄到那里去。比喻把灾祸推给别人。此处使用正确；\n故选：B。\n【点评】\n成语辨析题的设错角度：\n一、望文生义。有些成语可以直接从字面去理解；而绝大部分成语需 要透过字面意义去深刻地理解，如果对成语意义不加认真推敲，仅从字面去简单、肤浅地理解，就会造成望文 生义的毛病。\n二、断词取义。成语的意义具有完整性。如果只注意某些语素，而忽视其他语素，就会破坏整 个成语的意义。\n三、轻重失度。有些成语词义有轻重之别，切不可大词小用，或小词大用。\n四、语义重复 。成语的意义比较精练，使用得当，可以收到言简意赅的效果。但如果不注意成语意义和整个句子语义的比照 ，就可能造成成语意义和句子语义的重复。\n五、自相矛盾。如果不注意成语的意义和整个句子语义的比照， 也极有可能使成语的意义和句子的语义矛盾。\n六、形近混淆。有些成语与其他成语由于读音、字形相近或具 有某些共同的语素，在使用上极可能混淆。\n七、不合对象。有些成语的使用有其特定的对象和范围，不能随 意搬用。\n八、褒贬颠倒。成语往往含有不同的感情色彩，一般说来，褒词不能贬用，贬词不能褒用，否则会 影响感情的正确表达。\n九、谦敬错位。有些成语是谦词，只能用于己方，不能用于对方；有些成语是敬词， 只能用于对方，不能用于己方。如果辨别不清，就会造成谦敬错位。\n十、语法不通。各个成语的词性是不同 的，所以其语法功能也不同。如果对成语的词性把握不清，就会造成句子的语法错误。\n十一、性别色彩 有些成语有特定的使用对象，或只能用于男性，或只能用于女性，或共用于两性。如果把握不准，就会造成误用。\n十二、数量色彩 在表数量的成语中，有的只能用于多数，用在表单数的句子中就成了误用。\n"}
,{"title": "（2018•河南一模）下列各句中加点成语的使用，全都不正确的一项是（　　）\n①在国 家全面实施二孩政策的背景下，女教师过度集中生二胎，会让教育管理部门在人事安排上捉襟见肘，不少地方 不得不采取应对措施。\n②共产党人只有做到与国家和人民休戚与共、把个人荣辱置之度外，才会得到人民的 口碑，得到人民的拥戴。\n③阳关，一个让人生情的地方，从第一次起，阳关就在我的心里占据了挥之不去的 地位，这里的一动一静总关我情。\n④小时候的张衡夜半数星星，说自己长大后要成为一名科学家，没想到一 语成谶，后来，他成了汉代著名的天文学家。\n⑤职业资格考试项目的大幅瘦身，既是对证书泛滥、挂证乱象 的釜底抽薪，也是对人才活力、行业活力的巨大解放。\n⑥今年的跨年晚会，节目令观众耳目一新，绘声绘色 的歌曲，行云流水的舞蹈，赢得了现场观众的热烈掌声。", "choices": [{"text": "A．①③⑥", "ans": False}, {"text": "B．①②④", "ans": False}, {"text": "C．②⑤⑥", "ans": False}, {"text": "D．③④ ⑥", "ans": True}], "level": "难度：0.7", "description": "【分析】\n考查正确使用成语，要熟记成语 含义，结合语境准确辨析。\n【解答】\n①捉襟见肘：比喻顾此失彼，穷于应付。使用正确。\n②休戚与共： 忧喜、祸福彼此共同承担。形容关系密切，利害相同。同欢乐共悲哀。使用正确。\n③挥之不去：（事务）压 在心头，无法排解；指某些事情已经发生过了但没有办法挽回，但一直会在脑海中回想，怎么也忘不掉。句子 指阳关，对象错误。\n④一语成谶：指别人说了一句不吉利的话，这句话却变成了真的，句子指实现理想，是 好事，不合语境。\n⑤釜底抽薪：把柴火从锅底抽掉，才能使水止沸。比喻从根本上解决问题。使用正确。\n ⑥绘声绘色：形容叙述、描写生动逼真。句子指歌曲，对象误用。\n\n\n故选：D。\n【点评】\n解答成语题，第一、逐字解释词语，把握大意；第二、注意词语潜在的感情色彩和语体色彩；第三、要注意词语使用范围， 搭配的对象；第四、弄清所用词语的前后语境，尽可能找出句中相关联的信息；第五、从修饰与被修饰关系上 分析，看修饰成分跟中心词之间是否存在前后语义矛盾或者前后语义重复的现象。\n"}
,{"title": "（2018•河南一模）下列各句中，表达得体的一句是（　　）", "choices": [{"text": "A．我们公司刚成立不久，欢迎各界朋友前来垂询，我们将在提供就业策略方面鼎力相助", "ans": False}, {"text": "B．李大爷每天坚持锻炼身体，他说：“身体是革命的本钱，身体不好了，谁垂怜我呢！”", "ans": False}, {"text": "C．多年不见的老乡捎来了家乡的土产，我推辞不了，最好只好笑纳了", "ans": False}, {"text": "D．您嘱咐我给您的大作写一篇序言，我恨自己赐墙及肩，恐怕难以胜任", "ans": True}], "level": "难度：0.7", "description": "【分析】\n考查语言得体，要熟记谦辞敬辞，结合语境准确辨析。\n【解 答】\nA．“鼎力相助”指别人对自己的大力帮助。敬辞，一般用于请托或表示感谢。不能用于自己。\nB．“ 垂怜”是敬辞，称对方（多指长辈或上级）对自己的怜爱或同情。不能用于自己。\nC．“笑纳”是客套话，用于请人收下自己的礼物。不能用于自己。\nD．“大作”，敬辞，指别人的作品，正确。\n\n故选：D。\n【点 评】\n语言得体主要有文体得体和语体得体，文体得体注意一般应用的格式的规定，语体得体注意说话者的身 份，对象的身份，重点注意谦敬词语的运用。\n"}
,{"title": "（2018•河南一模）下列各句中，没有语病的一句是（　　）", "choices": [{"text": "A．中国载人航天工程办公室主任透露，中国将在2020年前后计划完成中国载人空间站的建造。在此期间，根据需要会发射一系列货运飞船，向空间站提供物资补给", "ans": False}, {"text": "B．京州市发布政策规定，暂停向拥有本市三套及以上住宅的本市户籍家庭出售新建商品住房及手住房；取得本市居住证的非本市户籍居 民家庭，方可允许在本市购买一套住房", "ans": True}, {"text": "C．周梅森创作的《人间正道》《至高利 益》《我主沉浮》和《绝对权力》等政治小说闻名全国，被誉为“中国政治小说第一人”，最近热播的《人民 的名义》是他的又一部反腐力作", "ans": False}, {"text": "D．食品生产厂的选址和建设要根据当地的环境条件和国家相关法律法规出发，既要有利于企业的发展，也要保证当地的生态环境不受影响", "ans": False}], "level": "难度：0.7", "description": "【分析】\n辨析并修改病句，能力层级为表达运用E．解答此类题，需要在理解句意的基础上，熟练掌握《考试大纲》明确提出的六种常见病句类型，即语序不当、搭配不当、 成分残缺或赘余、结构混乱、表意不明、不合逻辑。\n【解答】\nA．语序不当，把“将在2020年前后”中“将在”语序不当，可改为“计划将在2020年前后”；\nB．没有语病；\nC．搭配不当，“政治小说”不能被誉为 “中国政治小说第一人”，可改为“周梅森被誉为”；\nD．句式杂糅，“根据……出发”句式杂糅，应该改为“根据……”或“从……出发”。\n故选：B。\n【点评】\n病句辨析的几种方法：\n①语感检查法。辨析病句，可以依靠预估，一般说来，按习惯的说法觉得别扭的地方，常常是有语病的地方，病句类型中的搭配不当。 语序不当、语意重复都可用此法；\n②主干枝叶法，按照先找句子主干，再看句子枝叶的步骤来确定病句，搭 配不当、成分残缺都可用此法；\n③类比检查法，就是仿造一个结构类似的句子同原句作比较，如果仿写句子 有问题则说明原句不正确；\n④逻辑分析法，就是从事理上分析句子，看概念的使用、判断、推理是否得当， 语句的前后顺序、句间关系是否合适，前后语句是否呼应等。\n"}
,{"title": "（2018•桃城区校级模拟）下列各句中，没有语病的一句是（　　）", "choices": [{"text": "A．这些从地方“车改”中冒出来的问题有的是技术性的，有的则是体制性的。随着“车改”的深入推进，更多的利益会被触动，困难也会更多", "ans": True}, {"text": "B．当前，绝大多数数党员干部是清廉的 ，节俭的，但也有一些党员干部身上还存在不清廉的问题，突出表现就是在公款旅游和超标准接待上", "ans": False}, {"text": "C．在广大群众的支持、理解和配合下，已经结束了的四次国庆演练均收到了预期的效果 ，及时发现和解决了筹备工作中的有关问题", "ans": False}, {"text": "D．矿难发生后，大批子弟兵在前往救援时，许多专业心理救助人员也赶赴救援现场，第一时间对获救矿工及遇难旷工家属进行心理治疗", "ans": False}], "level": "难度：0.9", "description": "【分析】\n本题考查辨析病句的能力。此类题目要在理 解句意的基础上，仔细分析病句的类型，如语序不当、搭配不当、成分残缺或赘余、结构混乱、表意不明、不 合逻辑等。\n【解答】\nA．正确；\nB．结构混乱，尾句句式杂糅，可改为“突出表现在公款旅游和超标准接 待上”；\nC．语序不当，“支持、理解和配合”语序不合理，改为“理解、支持和配合”；\nD．偷换主语， “大批子弟兵在前往救援时”还没有出现谓语动词，主语就偷换成了“许多专业心理救助人员”，将“在”提 到“大批子弟兵”的前面；\n故选：A。\n【点评】\n语序不当主要有下列类型：\n1、名词附加语的多项定语 次序不当\n例如：许多附近的妇女、老人和孩子都跑来看他们。\n（“附近的”移到“许多”前面。）  \n2、动词的附加语的多项状语次序不当\n例如：美国有十五个州禁止黑人在娱乐场所与白人享有平等的地位。\n（ “与白人”移到“平等”的前面。）  \n3、虚词的位置安排得不恰当；特别是“把”字短语位置不当 \n例如 ：留在幼儿园的孩子们，都一个一个甜蜜地睡在新钉起来的木版床上。\n（表范围的副词“都”应放到表数量 的“一个一个”后。）\n"}
,{"title": "（2018•江苏模拟）依次填入下面一段文字横线处的语句，衔接最恰当的一组是（　　） \n    年轻时不擅长把握自己，做什么事都走极端显得过度。太急切地表现，_____，_____，_____．太过于胆怯，_____，_____，_____．一审势，看准了再做，二适度，得体地表现。古语说：“放者流为猖狂，收者入于孤寂。惟善操身心者，把柄在手，收放自如。”\n①不太得体                    ②就容易太夸张激昂      ③就害怕见人\n④机会来了也显不出你   ⑤常滥情失控                ⑥连一句整话都说不出。", "choices": [{"text": "A．③①②⑤⑥④", "ans": False}, {"text": "B．②①③⑤④⑥", "ans": False}, {"text": "C．②⑤①③⑥④", "ans": True}, {"text": "D．③②①⑤④⑥", "ans": False}], "level": "难度：0.7", "description": "解答本题既要考生知大纲规的1个虚词的意和用法又要回到上下文利用语言环境帮助解虚词，同时还好课内知迁移。\n【分析】\n言的答题，最关键的能够翻出全文理解全文的础，对具体题型，采 用不同的题方法，解决相关问题。\n句子解，把句子带入原文。\n本查对文章内容的把握。\n误选项A，文中“等待“这个思是原文中没有的。犯了中生有的错误。\nD\nD\n宋聚集药材四，所烧掉的债券，人中有十人有的 人做了，人接连管理几个，的俸丰厚，要送礼物给清的一户接着一户。宋清虽然不能刻得到他们的回报且赊死 账的有百人，但是并不妨碍成富有的人。宋清获取的眼长远所以能成就广大的利益，像那些小商人呢旦要不债 ，勃变色，第二次就相互骂而成为仇人。那些赚钱不是很小气吗？我看来正的白痴，有人在啊！清在是凭借样 获大利，又不胡作非为，坚持种风不停，最凭借这个成为富人。来向他求药的人愈愈应人之来。斥责抛弃、沉 沦颓废的人，亲戚朋友冷漠对待他，宋不会因为这样就怠慢对待对方，也一定平常那给的药材。这些人一旦再 权用事，就会更加地厚答宋清。清赚利看得长远，大都像这个样子。\nA\nA选项考的是虚词词两个““，一个 是代词，一个是助；B选项的虚的实词意义，个“以“是动词；第二个“是介词。C仍在考虚词词性，两个其“ ，个副词，一个是代词有的两个“”都是“更加”的意思。\n错误选是B，这是对文中人物的度拔高，可以过正文宋的自白找这选项问。用中朱清说总控“非有道”，来证明选项所朱认为自是“追求高尚做人的境界的误不 够恰当。\n阅读伸是新题型，它是在在阅读的基础上做延伸，既要考阅读能力是读题的一，又考写力，结合自 己的积累。文言文延伸题是关于取利长远，先让考生言文篇目中举例子，再去联系生活行发。要求先解文中的 题，再的体。\nB\n【解答】\nD项：“复”应为“”。A-C项为常用词生僻义或偏僻词，D项为常用词的常用命 意在增大读能力的检测。其中C项“”的在《桃源记》中出现过。实题中的生词或僻义项一般来讲正确的至少现在出现过例外。\n译文：\n我观察现今人与人之的交往都依附得势的人、抛弃贫寒人，很少有能像宋清这样子 做了。世之言，只是“用买方来交往”唉！宋清商人，现今人与交有人能像宋清那样希望得到远回报的吗？假 能有，么天下穷困潦倒。废受辱人得死亡的多了。柳先生说：“宋清身不做市侩的行为，然而居朝、官府，待 在乡里、学校，以士大自我标的人，反而先恐后地做侩行为，真是悲啊。\n【点评】\n此题考查的考点有以下 的几个：1理解常文言实在文中的含义；2、虚词运用3、理解并译文中子；4归内要。平时的学习中，要培养阅 浅易古代诗文能力，注重文实、虚意义和用法积累，解并掌握的文言特殊句式，握文言文翻的技。\n"}
,{"title": "（2018春•东平县期中）下列各句中，表达得体的一句是（　　）", "choices": [{"text": "A．我常光顾这家小餐厅，因为这里的就餐环境非常雅致，老板也很热情", "ans": False}, {"text": "B ．中秋节快到了，您日前对犬子多有照顾，特请您到我府上小酌，以示谢意", "ans": False}, {"text": "C．您老是知名的教育家、文学家，当我得知忝列门墙之时，心中狂喜", "ans": True}, {"text": "D．您在报告 中的一得之见，于我而言都是金玉良言，令我茅塞顿开", "ans": False}], "level": "难度：0.7", "description": "【分析】\n汉字因意定形，此题的关键在于首先正理解词语的意，断字形的误．\n卷券；\n-绌，\n【解答】\n正确。\n故选：。\n【点评】\n本题查确书写汉字的能力平的学习复习中要养良好的写习惯，意累一 些常见错、易混字的读音及写．\n51．兴高彩（采  15张灯结采（  153．惨绝圜（）  15然一笑（粲）  155 ．苍海桑田沧） 15．沧茫大海（苍）  157．藏纳污（  1．草官人命（菅）   59．测隐心（恻  60．出不穷 （）  161．层迭（叠  162．层峦叠障（嶂）   163插打浑（诨）   164．蝉连冠军（联   165．陈陈相应（ 因）   166词烂调滥）   16．学成才（材）   1惩前毙后（   69．禁百（儆  17里爬外（扒）   17．之鼻（嗤）  12．耳不闻（充）   17．当充（冲）  74忧冲（忡  175．峦重迭（叠）   16．重整旗鼓振）   177．愁莫展（筹）   18出类拔粹（萃）79．出奇不（其）  1．出奇致胜（）   81．出人投地（头） 182．除旧补新（布）   13．处心虑（积） 184．穿不息（川）  85．传颂一时（诵） ．吹毛求（疵  187．常议（长）  188．粗枝（） 18．粗制烂造（滥）  190．措火薪（厝）   11错手不及（措）   92．大小用（材）   19大 放獗（厥）  19．大声呼（疾  195廷（庭）  196．虎视耽耽（眈）   197．当人不让仁） 198．倒打把耙）   199．得不尝失（）  200．望蜀（陇）\n"}
,{"title": "（2018秋•石河子校级月考）下列加点的字注音全都正确的一项是（　　）", "choices": [{"text": "A．百舸（gě）    青荇（xìng）    荡漾（yàng）     峥嵘（zhēngróng）", "ans": True}, {"text": "B．彷徨（páng） 深邃（shuì）    漫溯（sù）       彳亍（chìchù）", "ans": False}, {"text": "C．百侣（lǚ）    惆怅（zhōu）    倾（qīng）听     佝偻（gōulóu）", "ans": False}, {"text": "D ．寥廓（guō）  跫（qióng）音   忸（niǔ）怩      颓圮（tuípǐ）", "ans": False}], "level": "难度：0.9", "description": "【分析】\n此题考默写常见的句名篇．要答好此类题，时就注意积．只弄懂意才有利于记住字形，尤其是那些容易的字，要加注．\n【解答】\n山重疑无，柳暗明又一村（重点字：疑）\n白以直兮 固前圣之所厚（重点字：清、固）\n5．诗怨恨怀王昏聩，轻信谣言语句是怨灵修之浩荡，终察夫民心．\n6． 《骚》中表明自己到不公正待的原因一上位者的荒的两怨灵之浩荡兮，终不察夫民心．\n7．《离骚》表明自因德行美好而到人诽的两：众女余之蛾眉兮，谣诼谓余善淫．\n1《离骚》一文以博大的胸怀，对劳寄予深同情的语句是：长太息以掩，哀民生之多艰．\n8．离骚》中表明自所处的会来就是善于投取巧，背规矩现状的两句固时俗之工巧兮，偭矩改错．\n【点评】\n《离》\n．《离》用草做比说自己遭贬黜是因为德行高尚的两句既替 余以蕙兮，又申以揽茝．\n0．离骚》表明作者在黑暗混乱社中烦闷意，走投无的两句忳郁余侘傺兮吾独穷困此时也．\n"}
,{"title": "（2018秋•石河子校级月考）对下列句子中加点词语的解释，不正确的一项是（　　）", "choices": [{"text": "A．晋军函陵                        军：军队", "ans": True}, {"text": "B．阙秦以利晋，唯君图之     唯：希望", "ans": False}, {"text": "C．秦伯说，与郑人盟            说：通 “悦”，高兴", "ans": False}, {"text": "D．秦之遇将军，可谓深矣。  遇：对待", "ans": False}], "level": "难度：0.9", "description": "内容意全理解，姑可把断．联全文前后看，先后难细分辨．\n习惯句式掌握住固定结莫拆散词性要精研，法结构帮助判．\n．口诀：\n1．步骤：通读所给材清文段大意，并标出关键划分分．\n紧紧住“曰”“云”言”，对话易发现常用虚词是标志更有规律供参．\n古文断莫畏难，仔琢磨只 等闲．文休问长与短读精思是关．\n题目做完回头看，据要求细验．牢基础看课本，养感读经典．操，千剑， 断句也要实践．\n参考答：\n根据词”进断句：一法修一病随/病尽而法完心不期中/目不存鹄十发十矣．\n结 构相同语意相关要顿“”“目“手”尝学射矣/始也心志于中/目存乎鹄手/十发而九其一/幸也．  法不一病随 之病尽而法完则心不期中/目不存鹄十发十中矣．\n吾学射矣/始心志于中目乎/手往从之/十九失/其一中也/幸 也．\n法修/一病随之尽而法完/则心不期中/目不存鹄/发十中．\n【点评】\n本题考查言断句能力．做“断题 ”通全文，段主要意，在此上再根据文意和常用的句方法加以判读．见的断句方有：语分析、对标、常见虚词 、结构对称、固定式等．\n"}
,{"title": "（2018秋•尤溪县校级月考）给下列诗歌分类不正确的一项是（　　）\n①《再别康桥》 ②《沁园春•长沙》③《大堰河--我的保姆》④《木兰诗》⑤《雨巷》⑥《七律•长征》⑦《春夜喜雨》⑧《石 壕吏》", "choices": [{"text": "A．①③⑤⑥是现代诗歌，④⑦⑧是古典诗歌", "ans": False}, {"text": "B．②③⑥是现代诗歌，⑦⑧是古典诗歌", "ans": False}, {"text": "C．①③⑤是新体诗，②④⑥是旧体诗，⑦是律诗，⑧古体诗", "ans": False}, {"text": "D．①③⑤是抒情诗，④⑧是叙事诗，②⑥是古代诗歌", "ans": True}], "level": "难度：0.7", "description": "【分析】\n本题是很有生活味的题目，题目给定 的是一个师生对话的情境，要补充是学的话语，要据李老师的揣摩说的话，意简明的要求，注意学生身份要有 貌等．\n【解答】\n李老师，您好！是风．\n老师．我和同学去拜访您．您行吗？\n好的．我们一准时访您．\n【点评】\n要解好此题要考生有较好的分析能语言概括能力．解答题时要指学生揣摩的谈话内容，问答要一致，得体．\n"}
,{"title": "（2018春•金华期中）\n昨夜雨疏风骤，浓睡不消残酒。试问卷帘人，却道海棠依旧。\n知否？知 否？应是绿肥红瘦。\n（李清照《如梦令》）\n对李清照《如梦令》分析不当的一项是（　　）", "choices": [{"text": "A．“不消”表面是指酒意未消，实际指的是消不尽的伤感和烦闷情绪", "ans": False}, {"text": "B．“绿肥红瘦”中，“绿”“红”分别代指叶和花，“肥”“瘦”分别形容叶的茂盛和花的凋零", "ans": False}, {"text": "C．这首词从一般叙述，转入到一问一答，然后是设问和慨叹，层层拓展、深入", "ans": False}, {"text": "D．作者采用直抒胸臆的手法，表达对春光留恋和惜别的一种伤感情绪", "ans": True}], "level": "难度：0.9", "description": "其，精心构。“，我想为你献上一首歌”是比喻性题， 应化虚为实，化大为小，系实由此及彼行想象。构思首先通加入限制语的方法来缩小范。着问题来实具体的素 ，赋予“你”确的现内。譬“为谁首歌”就虚为实，确定了相对集中写作素材，我们以怀感恩的心，为他们-父师长、亲、历史人、乡情故里、同学情谊等唱首歌。其次围绕中心选体写作容譬如总想为祖国唱首赞美的歌” 这个素材，我们要理解相问：“我为什么要赞祖”“哪些方值得我来赞美”、“通过哪些具体内容体现我的赞 美之情”等最后可以点三方内容：对祖国历史礼、祖国丰厚文底蕴的感悟、对民勇创造精神歌颂。样一歌翔实 的内容具体地加以体现，避免了生硬的抒情和空的议论。\n【分析】\n“，我为一首歌”，主题活，时代性。 写好这道题必着重把握三点：\n其三，抒发真情。“歌”，自已有。礼记》（卷三十九：“歌为言也，也，说 故言之。言之不足，故言之。”这句话明确说明“歌就是“长言”；“言”乃是畅言的意“畅言”，对一般来 ，表达无阻碍，吐痛快，情感更放。由此可见，“总想为唱首，在“我手写我心”，吐露真重在畅言实感，抒 真之情。情真处方人，情到深处“想你上一歌”。\n【解答】\n南，我想为献上一首歌。\n江南，是有味道的 春天，各种花开放，引蝴蝶蜜蜂翩翩起舞。，中弥是团味，糯滑甘甜，满口生津。夏天的瓜果香气葡萄梅、桃 、甜…数不胜数秋天，麦香稻香带光的道弥漫南空冬，人们忙于腌制味儿，肉香馋人，哪里都是江南绽放笑容 …江南，我想为你献一曲，香气醉人的歌。\n江，你的色彩让人醉。青石板街，雾氤氲蓝花印布温和熨帖老树 轮回，古春浅红门联晕黄灯。细雨飘落似白纱，海棠落轻拂面南，我想为献上一曲彩明丽的歌。\n江南，你如 此让我魂牵梦萦。你用你胧、、水墨美，我的心深在你的古中，是你，我在城市喧闹中麻木的心，得到了宁静 与救。\n江，有“达达的马蹄声是美丽误”的绻情；江南有“桂子十里荷花的美丽画有充满人间火气息的味道 ；江南，你让人沉醉人连江南，我为你献上一首歌！\n【点评】\n范文评：考场作文，题材新是出奇胜的方法 一此文首先以其不人的文题引人意其是分别从“色”“声音”味道”等方面分缕析地对江南美作具阐释解读。 语言极抒，句整散错，对偶排比的修俯皆是。诗讲究“”，本文也有三美语言，意美，情感美。的唱给江南一 首赞歌！\n"}
,{"title": "（2018秋•平邑县校级月考）下列语句中加点成语的使用错误的一项是（　　）", "choices": [{"text": "A．电视剧《恰同学少年》以毛泽东在湖南第一师范的读书生活为背景，展现了以毛泽东等为代表的一批优秀青年风华正茂的学习和生活故事．", "ans": True}, {"text": "B．细数2017的无锡搜房博客 ，有多少新锐博主在谈笑间指点江山，预见楼市风云．", "ans": False}, {"text": "C．以毛泽东为代表的那个时代的热血青年，写出了不少激浊扬清的好文章．", "ans": False}, {"text": "D．今日，幸福苑社区和万里学院团委邀请了经历过峥嵘岁月的老红军、老党员，与社区的暑期学生一起重温了红军长征艰苦卓绝的光荣 历史．", "ans": False}], "level": "难度：0.7", "description": "【分析】\n这2008年上海的高考命题作文．“他们”这一命题命题的理念都集中体现在引导考生学会关注生活、察并且学会考生中的人和事，及对自 己影，要“手写口，从作文传达出自己的受和生活体验．此，从审题角度来看难不大般考生都不会跑．但是如 何选材从怎样视角去感悟生活，提炼，且做到具一格，富有个性，这需要下夫的．只有选、题立意、谋篇布言 表方面具备了自己的亲悟理，才能从全方位映出考生的能力和慧．\n“们”与“我们”都是两个集代名词．我 们”和“他们”共同在一片蓝天之下，各的身份、职业、地位，以及所处的生活境精状等方面的不同罢了．因 此“们”与我们”彼此间关系十分切，谁离不开谁说到底只不过社的工不一样而“他”“我们”在同社会交往 活中，免了因为各种利益和矛盾既相又相摩擦，由此构成了复的社会关系．所以，此命具有很的开放性和包容 性．生可以不一格确题思想和立要点．以用爱、赞美的笔调去褒扬“他们”的崇高人和坚强的信念以不屈的精 格；可以用同或的目光去捕捉生中的势群体的生活状况和人的不幸遭遇等，思他们的命运、处境，提出解决的 措施、办法；也以站批判的角度，用厌恶、批的贬义感，写“他”庸俗与琐生活，或用在德底线上徘徊的危险 实与行为分等．但是，不管是褒扬贬抑还站在不褒不立场上，都不得单地对生活进行拍照、翻版或，一定得透 过现，而挖掘生中蕴藏理，品味生中的甜苦，品味出闪烁着性的光辉和情美好．\n【解答】\n他们\n我如今是 否知道的生日？知道他们的鞋码？知道他们最大的心愿？…也我们只知自他们会烧我们最爱的，知道们会在我 们的生日时送最贴心的，知道他要们好读书…\n他，永远如此沉，不们看到悲伤，不我们看到．他把他的一切 都给予我们，却从不说我们．\n我道他们一定在外面着．他们不母亲们那样焦急地聚集在一起，谈地．们一就 那么静静坐在落旁，抽着根烟，不看看学校大门．微微一下眼，考虑自己孩子是一切顺．他们不说话只抽着那 害了们一子的烟，粗糙有着烟熏的迹，脸上刻着令人生月迹．他，是父亲．\n他是父亲，伟大隐忍．是亲，这 世上最爱我们的人．也许，们出考场时，该给他们个拥我想们一定会尴尬一下，然后至老去铭刻于心．\n【点 评】\n时主要注下面几点：\n1．写真实--以情动．者文之经”，带着情感描述人和事能够打动读者．\n．角新-口要小．我们常，一个人的“视野要开阔”，那是要宏观上去观察活、泛了解人事和识社的要求，而文则大相径庭作文的切入角一定要小．“开口小”能写深、写透，就像《桃花源记》中渔人不觉发现了桃花源进口的一 个小洞门一样，“初极狭，才通人复行数十步豁然开朗．作文是此，要达到“进隘，再上幻而旷”的艺术境界 ，写作角度要小．如写“他”，绝对泛泛去，定得某些人、某场景、主表达要具体到些人、一件事一情景上千 万能什么写，结果么也写平淡．\n总之，“他们”文题本身意着引导考生学会注他人，把转“们”，从而避开 自我这个“小”．并会采用取景的视野和炼感点多元主关会，现人物．此文题的开放性定得落实在对材、体裁 、思等个层面．《他们这个考题启示我，阔生活视野、学会情感体运用性思辨，是作文备考的练方向．\n"}
,{"title": "（2018秋•洮北区校级期中）依次填入下面一段文字横线处的语句，衔接最恰当的一组是（　　）\n这时你少有的是“采菊东篱下，悠然见南山”式的静穆，你的诗因之而多怨、多愤，义侠的崇高，勇武的抗争，都进入了你的视域，超越了你笔下那些以贫困自守为尚的隐士的地位。在晋宋易代之际，________ ，___________，_______，______．__________，________。\n①你在《咏荆轲》中复活了他当日的英雄气概\n②你怅恨敢以捐躯为死士的正义之人的稀少\n③深为他的慷慨豪情所动\n④你在血性义侠之人里标出了勇士荆轲\n⑤在千载之后犹为这失败的英雄而悲悼\n⑥你为荆轲未能刺杀成秦始皇而遗憾。", "choices": [{"text": "A．①③⑤②④⑥", "ans": False}, {"text": "B．②④③①⑥⑤", "ans": True}, {"text": "C．②⑤① ③⑥④", "ans": False}, {"text": "D．④②③⑤①⑥", "ans": False}], "level": "难度：0.5", "description": "【分析】\n人一看科”二字就担心文章会深奥难，实际上，科普普及一定科学知识，把科学王国里的最信息传递给读者，从而读能够解世界万物变化、运动等规．因此，常会选用科学品文考查的是我们语文力． 我拨开云雾，明确技小品文的查特点积累文点的有知识，授予法与实练相结合，我们复习就会收到实际性效果 ．\n客观因：权威、会见、背哲理的常规．\n社会构如校等涉个内自由的发展并通过益的活动促使个体实现内 心的自由．\n人们获得活必需品而工作之余有间和精去人事个人动．\nC颠倒条件与结的系．原文说的是“合理的工问题解决，的进步就会提供这种自由的可能性”．\n创造使人能不受限制地交换一切结和意的社条件使人 们在切力劳动领具有言论自和育自由．\n答案：\nC\n【解答】\nB项“就能够得”绝对；完全能够达到”错， 原文说“这种在的自由的理想永远不全达到的”．\nB、E\n个体能断地、自地争取在的自和心的自由．\n【点 评】\n对于实用类问题题解答最主要的就是要注重对原文的挖掘，问答案与原文的系基本就是中花水中关系， 甚至答案就直接现在文中，在用类文阅我们先要做的就是要细读文章，每一段落所讲述的内容有所了解．回答 问时回到原以原文为根，捕捉文中目相的关键语，文中的关键词句实际上是案要点同时还注问题的分值，如果 一道题2分要求概回答，一般概括一个要点即；要求用原文句回答，则一要在原中出两个恰当的词果4分或6题，一般一点，案要点就两到三个．题目的分值，答题要点的重要．\n"}
,{"title": "（2018秋•临海市校级月考）对《沁园春•长沙》中的语句解释不正确的一项是（　　）", "choices": [{"text": "A．“层林尽染”是说山上一层层的枫树叶经霜变红，象是染过一样", "ans": False}, {"text": "B．“万类霜天竞自由”是说一切生物都在秋光中争过自由自在的生活", "ans": False}, {"text": "C．“书生意气，挥斥方遒”是说，读书人最讲意气，非常豪爽。挥洒自如，一点都不吝惜", "ans": True}, {"text": "D．“到中流击水，浪遏飞舟”，是说当年我们在江中游泳，激起的波浪，几乎阻止了飞快前进的船", "ans": False}], "level": "难度：0.7", "description": "2“”的知识，抓住关键词分析．\n构思 、思路”表达方面，应从全诗来分归纳，说出理由．\n“又”出了下雨前后景色变化，牧童因雨停而松的心情 ．\n【解答】\n答时首先要不句任何一字都无所好坏优分，但一进具体的中，则显示出高下来．所以所谓某字 用得好，是说某字在句作用发挥得要联句分析．答案有以几部分：形式上点明或辞、用、或手法等内容上要分 所表达的主题思想．“卷”字是看到，骤雨来袭的状态．\n“”从听觉角度写出骤雨声势大．\n“骤晴写雨来 得、得，暗扣诗题．\n    三 四句一步用多种比喻写风雨之势言来势，“万军声”状声之．“怒涛卷”上“沙滩”，借潮水汹，奔腾．声吼”如鸣瀑”以“鸣瀑瀑布）”喻“军声，又以“”喻风雨之声．三是补笔．“溪 西指西南，“北”应指西北，即修学上所谓互文”．牧童迎着风雨向西南走，故牛头已经下雨，而牛后还只是 乌云．点清楚，得必．尤妙的第句忽一，写出雨晴山绿，夏日晴瞬息化奇观．\n说这类习题一定的主观性，但 是，主流的分析、专家观点我绝不可弃之一．分析要结合全进行，整体考虑，顺整诗或、好．\n     这是一写景诗．写农村中夏急雨之壮观：一家住西牧一就着牛去溪北放．正在牧，忽然乌云翻，风骤至．牧童慌雨向南 方向渡溪回村，可是雨又“晴”，山又绿”了．\n不好．开篇写暴骤雨至，先声夺人和的骤形成呼应，体现作 谋篇布局的艺术匠．如果把五、六句放开头，牧童就成了写重，冲淡了诗的艺术效．\n答案：\n全诗析：\n   作刻画壮观，自见豪气，折自如，用口语朴素清，富有生气息．\n【点评】\n此考的考点下几个：1、炼字；2 、炼；3、构思、思路时学习们培养赏浅显诗文的能力，注分析诗歌中的点词子．记住一些常用的手法．\n"}
,{"title": "（2018秋•蓝田县校级月考）填入下面文段空白处的词语，最恰当的一组是（　　）\n    当我们提到歌剧时，首先想到的是什么呢？宏大的场面、巨大的篇幅、复杂的情节展开与人物关系、强烈的戏剧冲突……当然，__①__意大利古典浪漫派歌剧，__②__有一连串情感丰富的咏叹调，__③__引人入胜，__④__全剧一口气听下来未必轻松；__⑤__一些短小轻松的歌剧形式便应运而生，其中意大利的喜歌剧最为人熟知，__⑥__这里要说的是奥地利和匈牙利的轻歌剧。\n  ① ② ③ ④ ⑤ ⑥\nA / 还会 虽然 如果 因此 不过\nB 若是 一定 虽然 但 因此 其实\nC / 一定 尽管 如果 于是 其实\nD 若是 还会 尽管 但 于是 不过", "choices": [{"text": "A．A", "ans": False}, {"text": "B．B", "ans": False}, {"text": "C．C", "ans": False}, {"text": "D．D", "ans": True}], "level": "难度：0.7", "description": "【分析】\n古诗文默写先要能够背诵相关古词，不能字或者字，多字或字都不得分；次更重要的是能正书，只有错字就不得，因此，答 时写一定仔细，能出错误最后要真审题，看清要求“两题任选一题，如题答，只取前一题分”．\n【解答】\n 磐石方且厚据亿丈之 临不测之渊 千村万落生荆杞  陇亩无东西\n注意磐”“荆杞”陇亩“金风“窈窕”字形 ．\n【点评】\n此题考查点为“默写见的名句名篇”平时学中一是真背诵考规定的篇目二是对纲涉及的篇名句 要有积累，三是要正确书写，注意一些易错的字．\n"}
,{"title": "（2018春•双流区校级月考）依次填入下面一段文字横线处的语句，衔接最恰当的一组是（　　）\n    低碳经济是以低能耗、低污染、低排放为基础的经济模式，__________，__________，__________，__________，__________，__________。\n①旨在促进人类的可持续发展\n②也是中国实现科学发展的必 然要求\n③从长远看，发展低碳经济是全球可持续发展的必然选择\n④是能源消费方式、经济发展方式和人类 生活方式的一次新变革\n⑤涵盖了低碳能源、低碳技术、低碳生活等多种经济形态\n⑥也是从化石燃料为特征 的工业文明走向生态文明的又一次巨大进步。", "choices": [{"text": "A．⑤①④⑥③②", "ans": True}, {"text": "B．②③④⑥⑤①", "ans": False}, {"text": "C．⑥④⑤②①③", "ans": False}, {"text": "D．③②⑥①④⑤", "ans": False}], "level": "难度：0.7", "description": "所考查的虚词均出自大规定的1个文文虚词．对句出教材或选文对者可以此句该词的意义法代一句子，看讲的通还是讲不通后者，则需要先找到句子在原文的所，整个句乃至一段的意思而．\n【分析】\n文文实的断，本方法代入原文据上下文的文进排 或筛选，于据结构、语等进行分析，不如平时多一些文言文短文（难度不要大），积累一定文文形成语感．\n 一要有原文意识，找备选项在原的所在，据上文读懂大再据题干行查．\n对于需要读懂个句子或是一段乃全篇 才能答的这类概括，比犯难．其实，只要牢把握，就是找到信息进比较、纳、括，也就刃而解了．\n译文：\nA均为介词“”B项：到（词）的（词）．C项：按（介词/在介词）．D项：所字结，助词，可译为”或不译被（ 介），被动句固句式“为…所”\n叔孙通是薛县人．等项到了薛县，孙通便投了他．后来项梁在定陶战死，叔 孙通就跟随了怀王熊心．怀王被项羽封为义帝迁长沙去了，叔通留下奉事项． 汉帝二年205），汉刘邦领诸侯 王攻进城，叔通就投降王汉战西孙通也跟了终于投靠了汉王．\nC“车骑”翻成“战车兵错\n答案：\nD\nC\nA\nB\nC\n汉高帝五（前02），天下统一，们定陶共同尊推汉帝，叔通负责拟定式节．当时汉高帝秦朝的那些严苛的礼法规部取消，只是拟定一些简单易的规矩．可群臣在朝廷酒乐论劳，醉的狂呼乱叫，甚至拔出剑来坎削庭 中立柱高帝为这事感到头疼．叔孙通知帝来愈讨厌这类，就劝说：“些儒生很难为您攻夺取，可是帮您成．我 希征召鲁的一些生，我的子弟们一朝廷的礼．高帝说：“只怕会像过那样的烦琐难行？”叔孙说：“我愿意用 古代礼节与朝的礼仪糅起来制定礼节．皇帝说“可以试着办下，但要让易晓，考虑我能做得到的．”于是叔孙 通奉命征召了鲁地儒生三十多人．地有两个儒生不愿走，说：您侍奉将近十主，都当面阿谀奉承得亲近、显贵 的．我们不违心替您办这种．办的事合古，我们走．您还是去吧，不玷辱我们！孙通笑着“你们真是鄙的儒生 啊点不懂时世的变化”\n的是高帝的做法，据此可、C项；写的叔通帮助恢复古后的效，不能说其“识时务，有眼光”，据可排D项．\n是帝坐“龙辇”从宫房里来，百官起旗呼警，然后引诸侯王以下至六石以上的各级官员依次毕毕地向帝施礼道贺．诸侯王下所有员有一个不因严仪式而惊惧．等到仪式完，再设宴大．诸侯百官等坐 在上都敛声屏气地低头，按照尊卑次站来向皇帝祝敬．斟酒巡，谒者宣“宴会结束”．后监察员行仪法，找那 些不合礼仪规定的人把们带走．从朝见到会的全部过程，没有一个敢大声说话行动失当的．大典之后，高常得 意地说：“我今才知道当皇的贵啊．”于授给叔孙通太常的职，赏赐黄金百斤叔孙来后把五百斤黄送给各位儒 生．儒生们于是都高兴地说：叔孙先生实是圣人啊，知道当世的务”\n【点评】\n此题考查的考点有下的几：1、理解常文词在文中的含义；虚词的；、意思的理；4、归纳内容点5、文意解．时学习中，我要培养阅读浅易 古文的能，注重文言实词、虚词的意义和用的积累，了解并掌握常见的文言特殊句式，文言文的技巧．\n"}
,{"title": "（2018秋•石河子校级月考）下列语句中加点的词语与现代汉语意思相同的一项是（　　 ）", "choices": [{"text": "A．吾不能早用子，今急而求子，是寡人之过也．", "ans": True}, {"text": "B．行李之往来，共其乏困．", "ans": False}, {"text": "C．微夫人之力不及此．", "ans": False}, {"text": "D．樊将军以穷困来归丹．", "ans": False}], "level": "难度：0.5", "description": "【分析】\n此题考查容为名篇典，故涉要人物故事及节发展审时一定要熟悉章内容，做理性分析．\n【解答】\nB项“刘知道这是飞的迷惑敌之计，特意延送酒”误。刘知是计而担忧，诸亮知道，所诸葛亮派魏延送酒。\n故选B。\n3． 甲的事、语言、肖像动作说成乙，将甲的性、功过、典型义说成的，这错误选中常出现的张冠李戴的陷阱考必 须多加注意，别其中的陷阱；\n6．熟记名常的相关内容，熟记小说人物象、情节；\n．意准确交代主要人物与核事件，理清人物间的系，出重细；\n2题者在设置错误选项时，往往意变更情发生的地将此发事情成是彼地发生事情．解答这类题时，应注意选项中表示地点词语别地点变更的陷阱；\n【点评】\n考查对名著名篇的识记 能力．平的复中，我应以下几点：\n7．对人思想性的识以及典型情节的识记和复能，生应注意扣紧题干的要求，抓人物主要思想性，从典型事例、要故事情节概括．\n"}
,{"title": "（2018秋•蓝田县校级月考）依次填入下面一段文字横线处的语句，衔接最恰当的一组是（　　）\n    “社会情绪能力”是继“情商”之后，目前国际上脑研究的前沿课题和热点。人对客观世界的认知和对人与人之间关系的认知是不一样的。_____________，______________，_____________．_________________．________________，_________________．过去我们认为，这些问题说教就可以解决，但其实不然，这些都与脑的发展基础相关。\n①人的智商一直是可以完善、可以发展的\n②而智商的高低，至多影响你的生活质 量，而不至于毁灭你的生活\n③只要你不断学习，知识就会长进，智商就会提高\n④你过得快不快乐，都取决 于这五个方面\n⑤但社会情绪能力是决定人一生幸福的关键\n⑥社会情绪能力包括正确地评价自己、能了解别 人的情感、善于处理人际关系等五个方面。", "choices": [{"text": "A．①③②⑤④⑥", "ans": False}, {"text": "B．①③②⑤⑥④", "ans": True}, {"text": "C．⑥②③⑤④①", "ans": False}, {"text": "D．⑥④⑤①③②", "ans": False}], "level": "难度：0.9", "description": "【分析】\n此题查了正确使用词语对成语考查主要是我们能根据具的语判断成语的用是否恰当而要正成语运用是否恰当，须了成语的意思明确 成语使围、对褒贬色彩等情况．在复习中，只要针对些况，从了解成语的特点出，强练习，勤于积累，可收到 较好的效果．\n重复，当之，当任中最急切的事。与“眼前”重复；\n语相，望其项，望他的颈项和后背。比 赶得上。该用“难以望其项；\n正，流连忘，玩乐时留恋不愿离开。留恋得记了；\n选：D。\n色不当\n文生义\n用错象\n轻重当\n"}
,
"""


"""
content = driver.find_elements_by_xpath("//div[@class='mid-content']")
if SHOW_LOG: print(content)
cnt = 0
for c in content:
	ques = c.find_elements_by_class_name("QUES_LI")
	for q in ques:
		cnt += 1
		#if SHOW_LOG: print(str(cnt)+":\n"+q.text)
		bottom = q.find_elements_by_class_name("fieldtip")[0]
		btn = bottom.find_element_by_tag_name("a")
		#for btn in btns:
		if SHOW_LOG: print(btn.text)
		btn.click()
		ctx = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.CLASS_NAME, "body-content"))
		)
		time.sleep(2)
		#ctx = driver.find_elements_by_xpath("//div[@class='body-content']")[0]
		close = driver.find_elements_by_xpath("//input[@class='smbtn hclose']")[0]

		try:
			q2 = ctx.find_element_by_class_name("QUES_LI")

			if SHOW_LOG: print(ctx.text)

			pt1 = q2.find_element_by_class_name("pt1")

			pt2 = q2.find_element_by_class_name("pt2")
			choices = []
			answers = []
			chos = pt2.find_element_by_tag_name("table").find_element_by_tag_name("tbody").find_elements_by_tag_name("td")
			for cho in chos:
				choices.append(cho.text)
				ans = cho.find_elements_by_xpath(".//input[@checked='checked']")
				answers.append(len(ans) > 0)


			pt5 = q2.find_element_by_class_name("pt5")
			pt6 = q2.find_element_by_class_name("pt6")
			pt7 = q2.find_element_by_class_name("pt7")


			with open('question'+str(cnt)+'.que', 'w', encoding='utf-8') as file:
				file.write('TIT:'+pt1.text)
				file.write('\nCHO:\n')
				for choice in choices:
					file.write(choice+'\n')
				file.write('\nANS:')
				for i in range(len(answers)):
					if answers[i]:
						file.write(chr(ord('A')+i))
				file.write('\nDES:\n')
				file.write(pt5.text+'\n')
				file.write(pt6.text+'\n')
				file.write(pt7.text+'\n')
			if SHOW_LOG: print("success")
		except:
			if SHOW_LOG: print("fail")

		close.click()
		time.sleep(0.5)

"""