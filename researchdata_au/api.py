from itertools import count
import requests


class ResearchData:
	def __init__(self, **kwargs):
		self.header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'}
		self.possible_keys = ['rows', 'sort', 'p', 'q', 'group', 'license_class', 'access_rights', 'year_from', 'year_to']
		self.default_payload = {"filters":
			{"rows":"15",
			"sort":"score desc",
			"class":"collection",
			"p":"1",
			"q":""}
			}
		if kwargs:
			self.set_payload(**kwargs)

	def set_payload(self, **kwargs):
		for key, value in kwargs.items():
			if key in self.possible_keys:
				self.default_payload['filters'][key] = value
			elif 'anzsrc' in key:
				self.default_payload['filters']['anzsrc-for'] = value
			elif 'class_type' in key:
				self.default_payload['filters']['class'] = value
			else:
				print('{} is not a valid keyword'.format(key))

	def query(self, **kwargs):
		if kwargs:
			self.set_payload(**kwargs)
		api_uri = 'https://researchdata.ands.org.au/registry_object/filter'
		r = requests.post(api_uri, json=self.default_payload, headers=self.header)
		assert(r.ok)
		return r.json()

	def query_for_docs(self, **kwargs):
		json_object = self.query(**kwargs)
		try:
			gen = (each_doc for each_doc in json_object['response']['docs'])
			return gen
		except Exception as e:
			print('Error querying for docs: {}'.format(e))

	def get_titles_and_ids(self, gen=False, **kwargs):
		json_object = self.query(**kwargs)
		counter = count(1)
		try:
			if gen:
				titles_and_ids = ((each_doc['title'],each_doc['id']) for each_doc in json_object['response']['docs'])
			else:
				titles_and_ids = [(each_doc['title'],each_doc['id']) for each_doc in json_object['response']['docs']]
			return titles_and_ids
		except Exception as e:
			print('Error getting titles and ids: {}'.format(e))

	def object_details(self, object_id):
		api_uri = "https://researchdata.ands.org.au/api/registry/object/{}/".format(object_id)
		r = requests.get(api_uri, headers=self.header)
		assert(r.ok)
		return r.json()

	def object_core(self, object_id):
		api_uri = 'https://researchdata.ands.org.au/registry_object/get/{}/core'.format(object_id)
		r = requests.get(api_uri, headers=self.header)
		assert(r.ok)
		return r.json()

	def get_external_link(self, object_id):
		json_object = self.object_details(object_id)
		try:
			title = json_object['data'][0]['connectiontrees'][0]['title']
			link = json_object['data'][0]['directaccess'][0]['access_value']
			return (title, link)
		except Exception as e:
			print('Error getting links: {}'.format(e))

	def filter_by_subject(self, **kwargs):
		if kwargs:
			self.set_payload(**kwargs)

		api_uri = 'https://researchdata.ands.org.au/registry_object/vocab/anzsrc-for/'
		r = requests.post(api_uri, json=self.default_payload, headers=self.header)
		assert(r.ok)
		return r.json()

	def resolve_subjects(self, subject_id):
		payload = {'data':subject_id}
		api_uri = 'https://researchdata.ands.org.au/registry_object/resolveSubjects/anzsrc-for'
		r = requests.post(api_uri, json=payload, headers=self.header)
		assert(r.ok)
		return r.json()


	def identifier_match(self, object_id):
		api_uri = 'https://researchdata.ands.org.au/registry/services/api/registry_objects/{}/identifiermatch'.format(object_id)
		r = requests.get(api_uri, headers=self.header)
		assert(r.ok)
		return r.json()

