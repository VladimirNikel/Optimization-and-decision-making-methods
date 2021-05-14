 ```bash
nikel@Aspire-A717-71G:~/dev/University/Optimization & decision-making methods/laba6$ python3 -m pytest -v .
======================================================== test session starts ========================================================
platform linux -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- /usr/bin/python3
cachedir: .pytest_cache
metadata: {'Python': '3.8.5', 'Platform': 'Linux-5.4.0-73-generic-x86_64-with-glibc2.29', 'Packages': {'pytest': '6.2.3', 'py': '1.10.0', 'pluggy': '0.13.1'}, 'Plugins': {'cov': '2.11.1', 'metadata': '1.11.0', 'html': '3.1.1', 'Faker': '6.5.0'}}
rootdir: /home/nikel/dev/University/Optimization & decision-making methods/laba6
plugins: cov-2.11.1, metadata-1.11.0, html-3.1.1, Faker-6.5.0
collected 24 items                                                                                                                  

test_functional.py::test_ilen_range PASSED                                                                                    [  4%]
test_functional.py::test_ilen_list PASSED                                                                                     [  8%]
test_functional.py::test_ilen_tuple PASSED                                                                                    [ 12%]
test_functional.py::test_ilen_string PASSED                                                                                   [ 16%]
test_functional.py::test_flatten_list PASSED                                                                                  [ 20%]
test_functional.py::test_flatten_tuple PASSED                                                                                 [ 25%]
test_functional.py::test_flatten_combo PASSED                                                                                 [ 29%]
test_functional.py::test_flatten_to_tuple PASSED                                                                              [ 33%]
test_functional.py::test_flatten_string PASSED                                                                                [ 37%]
test_functional.py::test_distinct_list PASSED                                                                                 [ 41%]
test_functional.py::test_distinct_tuple PASSED                                                                                [ 45%]
test_functional.py::test_distinct_not_repetitions PASSED                                                                      [ 50%]
test_functional.py::test_groupby_correct_key PASSED                                                                           [ 54%]
test_functional.py::test_groupby_key_error PASSED                                                                             [ 58%]
test_functional.py::test_chunks_with_none PASSED                                                                              [ 62%]
test_functional.py::test_chunks_without_none PASSED                                                                           [ 66%]
test_functional.py::test_first_list PASSED                                                                                    [ 70%]
test_functional.py::test_first_tuple PASSED                                                                                   [ 75%]
test_functional.py::test_first_string PASSED                                                                                  [ 79%]
test_functional.py::test_first_none PASSED                                                                                    [ 83%]
test_functional.py::test_last_list PASSED                                                                                     [ 87%]
test_functional.py::test_last_tuple PASSED                                                                                    [ 91%]
test_functional.py::test_last_string PASSED                                                                                   [ 95%]
test_functional.py::test_last_none PASSED                                                                                     [100%]

======================================================== 24 passed in 0.13s =========================================================
```
