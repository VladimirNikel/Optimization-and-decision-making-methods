 
```bash
nikel@Aspire-A717-71G:~/dev/University/Optimization & decision-making methods/laba3/whatIsYearNow$ python3 -m pytest --cov . testWhatIsYearNow.py 
======================================================== test session starts ========================================================
platform linux -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: /home/nikel/dev/University/Optimization & decision-making methods/laba3/whatIsYearNow
plugins: cov-2.11.1, metadata-1.11.0, html-3.1.1, Faker-6.5.0
collected 3 items                                                                                                                   

testWhatIsYearNow.py ...                                                                                                      [100%]

----------- coverage: platform linux, python 3.8.5-final-0 -----------
Name                   Stmts   Miss  Cover
------------------------------------------
testWhatIsYearNow.py      27      0   100%
what_is_year_now.py       24      4    83%
------------------------------------------
TOTAL                     51      4    92%


========================================================= 3 passed in 0.16s =========================================================
```


```bash
nikel@Aspire-A717-71G:~/dev/University/Optimization & decision-making methods/laba3/whatIsYearNow$ python3 -m pytest --cov . --cov-report=html testWhatIsYearNow.py 
======================================================== test session starts ========================================================
platform linux -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: /home/nikel/dev/University/Optimization & decision-making methods/laba3/whatIsYearNow
plugins: cov-2.11.1, metadata-1.11.0, html-3.1.1, Faker-6.5.0
collected 3 items                                                                                                                   

testWhatIsYearNow.py ...                                                                                                      [100%]

----------- coverage: platform linux, python 3.8.5-final-0 -----------
Coverage HTML written to dir htmlcov


========================================================= 3 passed in 0.15s =========================================================
```