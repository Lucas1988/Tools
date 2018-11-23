import requests
import json
import re
import traceback

try:
	print('Hello') + 8 # This is an example

except Exception as title:
	print(traceback.format_exc())

	result = requests.get('https://api.stackexchange.com/2.2/search/advanced?page=1&pagesize=1&order=desc&sort=relevance&tagged=python&site=stackoverflow&title=' + str(title))

	searchresult = result.json()
	questionID = searchresult['items'][0]['question_id']

	question = requests.get('https://api.stackexchange.com/2.2/questions/' + str(questionID) + '/answers?page=1&pagesize=1&order=desc&sort=votes&filter=withbody&site=stackoverflow')
	question = question.json()

	answer = question['items'][0]['body']
	answer = re.sub('<.*?>', '', answer)

	print(answer)
