# Research-Data-Australia-API

researchdata.ands.org.au Python 3 API

## Install
``` bash
python3 -m pip install ResearchDataAU
```

## How To 

#### Simple Query of Research Data Australia

```python
from researchdata_au import ResearchData

rd = ResearchData()

json_ = rd.query(q='unemployment')

```

#### A little more complex query 

```python
from researchdata_au import ResearchData

rd = ResearchData()

json_ = rd.query(q='unemployment', 
    rows = 30, 
    year_from=1991, 
    year_to=2016, 
    group=['Central Queensland University', 'Australian National Corpus'])

```

#### Get a generator of 100 document items

```python
from researchdata_au import ResearchData

rd = ResearchData()

gen_ = rd.query_for_docs(q='unemployment', rows=100)


```

#### Get a list of title/id tuples


```python
from researchdata_au import ResearchData

rd = ResearchData(q='income', rows=30)

list_ = rd.get_titles_and_ids()


```
#### Look at an items details

```python
from researchdata_au import ResearchData

rd = ResearchData()

json_ = rd.object_details(object_id=444926)

```

#### Get external link of article

```python
from researchdata_au import ResearchData

rd = ResearchData()

tup_ = rd.get_external_link(object_id=444926)

```


#### Filter by subject/area of research

```python
from researchdata_au import ResearchData

rd = ResearchData(q='income')

json_ = rd.filter_by_subject()

```

##### Note: Object Id is the id for each article

