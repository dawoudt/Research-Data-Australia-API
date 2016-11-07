
# {"filters":
# 	{"rows":"15",
# 	"sort":"score desc",
# 	"class_type":"collection",
# 	"p":"1",
# 	"q":"dataset",
# 	"anzsrc-for":"07",
# 	"group":"Commonwealth Scientific and Industrial Research Organisation",
# 	"license_class":"open licence",
# 	"access_rights":"open",
#  "year_to": 1980,
#  "year_from": 2012,
# 	}


# sort - sort order
# -------------------
# list_title_sort (asc, desc)
# record_created_timestamp (asc, desc)
# score (asc, desc)

# p - page number 
# ------------------
# integer
# get query for particular page
# Note: If rows parameter is set to a high number, p becomes redundant

# q - query
# ---------------------
# e.g: unemployment, incomes, salary, etc.

# year_from 
# ----------
# integer

# year_to
# ----------
# integer



# anzsrc --- subject (api takes codes as input)
# ----------------------------------------
# {'01': 'MATHEMATICAL SCIENCES'
# {'02': 'PHYSICAL SCIENCES'}
# {'03': 'CHEMICAL SCIENCES'}
# {'04': 'EARTH SCIENCES'}
# {'05': 'ENVIRONMENTAL SCIENCES'}
# {'06': 'BIOLOGICAL SCIENCES'}
# {'07': 'AGRICULTURAL AND VETERINARY SCIENCES'}
# {'08': 'INFORMATION AND COMPUTING SCIENCES'}
# {'09': 'ENGINEERING'}
# {'10': 'TECHNOLOGY'}
# {'11': 'MEDICAL AND HEALTH SCIENCES'}
# {'12': 'BUILT ENVIRONMENT AND DESIGN'}
# {'13': 'EDUCATION'}
# {'14': 'ECONOMICS'}
# {'15': 'COMMERCE, MANAGEMENT, TOURISM AND SERVICES'}
# {'16': 'STUDIES IN HUMAN SOCIETY'}
# {'17': 'PSYCHOLOGY AND COGNITIVE SCIENCES'}
# {'18': 'LAW AND LEGAL STUDIES'}
# {'19': 'STUDIES IN CREATIVE ARTS AND WRITING'}
# {'20': 'LANGUAGE, COMMUNICATION AND CULTURE'}
# {'21': 'HISTORY AND ARCHAEOLOGY'}
# {'22': 'PHILOSOPHY AND RELIGIOUS STUDIES'}


# group ---  data provider
# -------------------------
# Advanced Ecological Knowledge and Observation System
# AMMRF
# ARC Centre of Excellence for Climate System Science
# ARCCSS
# Atlas of Living Australia
# AuScope
# AusStage: Gateway to the Australian Performing Arts
# AustLII
# Australian Antarctic Data Centre
# Australian Catholic University
# Australian Coastal Ecosystems Facility
# Australian Ecological Knowledge and Observation System
# Australian Institute of Health and Welfare
# Australian Institute of Marine Science
# Australian National Corpus
# Australian Nuclear Science and Technology Organisation
# Australian Ocean Data Network
# Australian Synchrotron
# Australian Water Research and Development Coalition
# BioGrid Australia Ltd
# Bioplatforms Australia
# Bond University
# Breast Cancer Tissue Bank
# Bureau of Meteorology
# Central Queensland University
# Centre for Magnetic Resonance
# Charles Darwin University
# Charles Sturt University
# Commonwealth Scientific and Industrial Research Organisation
# Curtin University
# DaRIS_1004___Centre_for_Neuroscience
# DaRIS_1047___Melbourne_Neuropsychiatry_Centre,_Department_of_Psychiatry
# data.gov.au
# data.nsw.gov.au
# data.qld.gov.au
# data.vic.gov.au
# Deakin University
# Desert Ecology Research Group
# eAtlas
# Ecosystem Modelling and Scaling Infrastructure
# Edith Cowan University
# EOAS_OHRM
# Federation University Australia
# Flinders University
# Geoscience Australia
# Global Proteome Machine Organization
# Griffith University
# Human Protein Atlas Consortium
# Hydrology and Catchment Management
# Integrated Marine Observing System
# International_Centre_for_Classroom_Research
# James Cook University
# La Trobe University
# La Trobe University, Australia
# Long Term Ecological Research Network
# Macquarie University
# Michael Chang PhD
# Monash University
# Murdoch University
# Museum Metadata Exchange
# N2O Network
# National Computational Infrastructure
# National Environmental Information Infrastructure
# NICTA
# OzFlux: Australian and New Zealand Flux Research and Monitoring
# OzTrack
# PARADISEC
# Polar Information Commons
# Public Record Office Victoria
# Publish My Data
# QFAB
# Queensland Department of Agriculture, Fisheries and Forestry
# Queensland University of Technology
# RMIT University
# RMIT University, Australia
# Southern Cross University
# State Records Authority of New South Wales
# Swinburne University of Technology
# Tasmanian Partnership for Advanced Computing
# TERN Australian SuperSite Network
# Terrestrial Ecosystem Research Network
# The Australian National University
# The University of Adelaide
# The University of Melbourne
# The University of Newcastle, Australia
# The University of Queensland
# The University of Sydney
# The University of Western Australia
# University of Canberra
# University of New England
# University of New South Wales
# University of South Australia
# University of Southern Queensland
# University of Tasmania, Australia
# University of Technology, Sydney
# University of the Sunshine Coast
# University of Wollongong
# University_of_Melbourne
# Victoria University
# Western Sydney University


# license_class
# -------------- 
# open licence: A licence bearing broad permissions that may include a requirement to attribute the source, or share-alike (or both), 
# requiring a derivative work to be licensed on the same or similar terms as the reused material.

# non-commercial licence: As for the Open Licence but also restricting reuse only for non-commercial purposes.

# non-derivative licence: As for the Open Licence but also prohibits adaptation of the material,
# and in the second case also restricts reuse only for non-commercial purposes.

# restrictive licence: A licence preventing reuse of material unless certain restrictive conditions are satisfied.
# Note licence restrictions, and contact.

# no licence: All rights to reuse, communicate, publish or reproduce the material are reserved, with the exception of specific rights contained within the Copyright Act 1968 or similar laws.  Contact the copyright holder for permission to reuse this material.
# Other: No value or user defined custom value.

# access_rights 
# -----------------
# open
# conditional
# restricted
# other 






"""

TODO:
	convert functions in to class

"""


from itertools import count
import requests
import json


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

