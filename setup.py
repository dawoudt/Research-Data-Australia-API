
desc = """
# Research-Data-Australia-API

researchdata.ands.org.au Python 3 API

## How To 

#### Simple Query of Research Data Australia

from researchdata_au import ResearchData

rd = ResearchData()

json_ = rd.query(q='unemployment')


#### A little more complex query 


from researchdata_au import ResearchData

rd = ResearchData()

json_ = rd.query(q='unemployment', 
    rows = 30, 
    year_from=1991, 
    year_to=2016, 
    group=['Central Queensland University', 'Australian National Corpus'])


#### Get a generator of 100 document items


from researchdata_au import ResearchData

rd = ResearchData()

gen_ = rd.query_for_docs(q='unemployment', rows=100)


#### Get a list of title/id tuples


from researchdata_au import ResearchData

rd = ResearchData(q='income', rows=30)

list_ = rd.get_titles_and_ids()



#### Look at an items details


from researchdata_au import ResearchData

rd = ResearchData()

json_ = rd.object_details(object_id=444926)



#### Get external link of article


from researchdata_au import ResearchData

rd = ResearchData()

tup_ = rd.get_external_link(object_id=444926)



#### Filter by subject/area of research


from researchdata_au import ResearchData

rd = ResearchData(q='income')

json_ = rd.filter_by_subject()



##### Note: Object Id is the id for each article"""

import os
from setuptools import setup


setup(
    name = "ResearchDataAU",
    version = "0.1.0",
    author = "Dawoud Tabboush",
    author_email = "dtabboush@gmail.com",
    description = ("A Python 3 API for researchdata.ands.org.au"),
    license = "MIT",
    keywords = "research data Australia academic university",
    url = "https://github.com/dawoudt/Research-Data-Australia-API",
    packages=['researchdata_au'],
    long_description=desc,
    platforms='any',
    install_requires=[
        'requests>=2.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)