## htmltruncate

[![Build Status](https://travis-ci.org/chadpaulson/htmltruncate.png)](https://travis-ci.org/chadpaulson/htmltruncate.py)

Returns a truncated string while preserving HTML markup (which does not count towards length). All tags left open by truncation are closed.

**Example**:

```python
>>> import htmltruncate
>>> str = "<p>You're not gonna lose the house, <b>everybody</b> has three mortgages nowadays.</p>"
>>> htmltruncate.truncate(str, 33)
"<p>You're not gonna lose the house, </p>"
```

**Options**:

```python
>>> htmltruncate.truncate(str, 33, full_word=True, ellipsis="...")
"<p>You're not gonna lose the house, <b>everybody</b></p>..."
```
