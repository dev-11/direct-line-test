# fork-and-code-python


[![Build Status](https://travis-ci.org/dev-11/fork-and-code-python.svg?branch=master)](https://travis-ci.org/dev-11/fork-and-code-python)
[![codecov](https://codecov.io/gh/dev-11/fork-and-code-python/branch/master/graph/badge.svg)](https://codecov.io/gh/dev-11/fork-and-code-python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4ea99c7790714259a2339d92c50e3c1d)](https://www.codacy.com/manual/dev-11/fork-and-code-python?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dev-11/fork-and-code-python&amp;utm_campaign=Badge_Grade)

# Software Engineer Python Test


Create a REST endpoint that return the sum of a list of numbers e.g. `[1,2,3] => 1+2+3 = 6`. You are free to use any Python 3 framework, however, try and keep the usage of the third- party library to a minimum.


The list of numbers is expected to arrive from a backend service and for this test you can hard code the list using the following line.
```python
numbers_to_add = list(range(10000001))
```
The url of the endpoint and the sample response is as follows: Request: http://localhost:5000/total

Response:
```json
{
"total": 6
}
```

Please provide the source code, tests, documentations and any assumptions you have made.


Note: We are looking for the candidate’s “Software Engineering” ability not just the Python programming skills.
