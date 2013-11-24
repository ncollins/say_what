say what
========

Say What was a project started at the New York Times Developers Hack Day
on Nov 16, 2013.

sunlight-foundation
===================

Goal; Compute the complexity of each bill in congress. As a first crack, measure the number of references to laws. Usually, such references are particularly obscure.
There is  not an easily-recognizable grammar to recognize legal citations inline, but a few common words will suffice for startsers;
"United States Code", "Federal Register", U.S.C., "Public Law", "Private Law"

setup
=====

First make sure you have Pip installed and run `pip install -r requirements.txt`.

Next run `db_setup.py`.

Finally you need to obtain keys for the APIs and set them up in `login.py` (does
not exist by default):

```
keys = {
    'nyt_article_search': '***',
    'nyt_campaign_finance': '***',
    'nyt_congress': '***',
    'sunlight': '***',
}
```

You can get a key from [developer.nytimes.com/register](developer.nytimes.com/register)
and [http://sunlightfoundation.com/api/](http://sunlightfoundation.com/api/).
