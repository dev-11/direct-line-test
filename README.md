# fork-and-code-python

[![Build Status](https://travis-ci.org/dev-11/direct-line-test.svg?branch=master)](https://travis-ci.org/dev-11/direct-line-test)
[![codecov](https://codecov.io/gh/dev-11/direct-line-test/branch/master/graph/badge.svg)](https://codecov.io/gh/dev-11/direct-line-test)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/62b05d1ff2b6409cbf80fbced63993f3)](https://www.codacy.com/manual/dev-11/direct-line-test?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dev-11/direct-line-test&amp;utm_campaign=Badge_Grade)

## Software Engineer Python Test

Create a REST endpoint that returns the sum of a list of numbers e.g. `[1,2,3] => 1+2+3 = 6`. You are free to use any Python 3 framework, however, try and keep the usage of the third-party library to a minimum.

The list of numbers is expected to arrive from a backend service and for this test you can hard code the list using the following line.
```python
numbers_to_add = list(range(10000001))
```
The url of the endpoint and the sample response is as follows: Request: <http://localhost:5000/total>

Response:
```json
{
"total": 6
}
```

Please provide the source code, tests, documentations, and any assumptions you have made.

_Note: We are looking for the candidate’s “Software Engineering” ability not just the Python programming skills._
