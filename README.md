# Research-Data-Australia-API

researchdata.ands.org.au Python 3 API

## How To 

#### Simple Query of Research Data Australia

```python
from researchdata_au import ResearchData

rd = ResearchData()

j = rd.query(q='unemployment')

```

#### A little more complex query 

```python
from researchdata_au import ResearchData

rd = ResearchData()

j = rd.query(q='unemployment', 
    rows = 30, 
    year_from=1991, 
    year_to=2016, 
    group=['Central Queensland University', 'Australian National Corpus'])

```

#### Get a generator of 100 document items

```python
from researchdata_au import ResearchData

rd = ResearchData()

gen = rd.query_for_docs(q='unemployment', rows=100)


```

#### Get a list of title/id tuples


```python
from researchdata_au import ResearchData

rd = ResearchData()

l = rd.get_titles_and_ids(q='income', rows=30)


```
#### Look at an items details

```python
from researchdata_au import ResearchData

rd = ResearchData()

j = rd.object_details(object_id=444926)

```

#### Get external link of article

```python
from researchdata_au import ResearchData

rd = ResearchData()

tup = rd.get_external_link(object_id=444926)

```


#### Filter by subject/area of research

```python
from researchdata_au import ResearchData

rd = ResearchData(q='income')

j = rd.filter_by_subject()

```

##### Note: Object Id is the id for each article

