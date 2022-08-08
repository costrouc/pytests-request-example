# Testing APIs with Python

There are a ton of ways to test APIs in python. What I am suggesting
here is correct and what I think think the most intuitive python combo
to use.

There are three important libraries we are going to leverage:
 - [pytest](https://docs.pytest.org/en/7.1.x/) :: this is a test
   framework that makes it easy to write tests. pytest will run any
   function in `tests/test_*.py` with a name that starts with
   `test_*`.
 - [request](https://requests.readthedocs.io/en/latest/) a great
   default choice for alibrary to make HTTP/REST API requests.
 - [yarl](https://github.com/aio-libs/yarl/) a library I'm quite fond
   of that makes writing api urls easier to construct.

# Introduction

Install python requirements

```shell
pip install -r requirements.txt
```

Run the tests. Make sure you are running the command in the root of
the repository.

```shell
pytest
```

Now make some modifications to `tests/test_api.py` and run `pytest`
again to watch tests run. Some useful options to know with pytest.

```shell
pytest    # normal usage
pytest -s # show all print statements output within tests
pytest -x # stop the tests on the first one that fails
```
