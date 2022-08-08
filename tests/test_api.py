import yarl

# example uses the github api
# https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api

GITHUB_BASE_API = yarl.URL('https://api.github.com')

# first read about a GET vs. POST vs. PUT vs... request
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods in general
# GET requests are most common and mean "read" typically are methods
# that do not change state of the server e.g. "list all users", "get
# current user". POST and PUT modify the state of the server such as
# "create new user", "add a post".
# POST -> "Create item"
# GET -> "Read item(s)"
# PUT -> "Update item"
# DELETE -> "Delete item"
# This is where the term "CRUD" comes from in REST APIs
# https://developer.mozilla.org/en-US/docs/Glossary/CRUD
# For the most part all REST APIs should follow these "conventions"
# though there are always good reasons to break these rules.

def test_github_get_zen(client):
    # make a GET http request to api.github.com/zen
    # I'm not using yarl yet to make this example explicit
    response = client.get('https://api.github.com/zen')
    # check that api returns a 2XX or 3XX status code
    # which indicates success (4XX and 5XX indicate errors)
    # see https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    response.raise_for_status()


def test_github_get_user_defunkt(client):
    # here we use yarl to simplify url construction
    # equivalent to 'https://api.github.com/users/defunkt'
    response = client.get(GITHUB_BASE_API / 'users/defunkt')
    # again check that this request was successful
    response.raise_for_status()
    # since we know this endpoint returns json (most REST apis do) we
    # get the json from the response (after we know the request was
    # successful)
    data = response.json()
    # one thing we know is that the username is 'defunkt' so lets
    # check one of the fields
    assert data['login'] == 'defunkt'


# now lets test another service
# https://jsonplaceholder.typicode.com/ and make a POST request

JSONPLACEHOLDER_BASE_API = yarl.URL('https://jsonplaceholder.typicode.com')


def test_jsonplaceholder_post_posts(client):
    # notice how we change from `get` -> `post`
    response = client.post(JSONPLACEHOLDER_BASE_API / 'posts', json={
        'title': 'This is a sample title post',
        'body': 'some interesting content',
        'userId': 12345,
    })
    # again check that this request was successful
    response.raise_for_status()
    # here we print the response in the test you will see this output
    # if you run "pytest -s" (the -s option prints output when tests run
    # otherwise it is hidden)
    print(response.json())
    data = response.json()
    # from knowing how the api response we know that 101 will be the
    # post id got this from looking at the print statement above after
    # running the tests
    assert data['id'] == 101
    assert 'This is a sample title' in data['title']
    assert 'This is a sample title post' == data['title']

# similarly you can use `client.put`, `client.delete` etc. for tests
