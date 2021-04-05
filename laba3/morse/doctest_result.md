```bash
nikel@Aspire-A717-71G:~/dev/University/Optimization & decision-making methods/laba3/morse$ python3 -m doctest -o NORMALIZE_WHITESPACE -v morse.py
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('TEST MESSAGE')
Expecting:
    '- . ... -   -- . ... ... .- --. .'
ok
Trying:
    encode('Nikel') #doctest: +ELLIPSIS
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: 'i'
ok
2 items had no tests:
    morse
    morse.decode
1 items passed all tests:
   3 tests in morse.encode
3 tests in 3 items.
3 passed and 0 failed.
Test passed.
 ```
