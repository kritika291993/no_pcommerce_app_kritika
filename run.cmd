rem pytest -v -s -m "regression"  --html=reports\report_searchby.html testCases --browser chrome
rem pytest -v -s -m "sanity"  --html=reports\report_chrome.html testCases --browser chrome
rem pytest -v -s -m "sanity or regression"  --html=reports\report_searchby.html testCases --browser chrome
rem pytest -v -s -m "sanity and regression"  --html=reports\report_searchby.html testCases --browser chrome
rem pytest -v -s --html=reports\report_searchby.html testCases --browser chrome

rem pytest -v -s -m "regression"  --html=reports\report_searchby.html testCases --browser edge
rem pytest -v -s -m "sanity"  --html=reports\report_chrome.html testCases --browser edge
rem pytest -v -s -m "sanity or regression"  --html=reports\report_searchby.html testCases --browser edge
rem pytest -v -s -m "sanity and regression"  --html=reports\report_searchby.html testCases --browser edge
rem pytest -v -s --html=reports\report_searchby.html testCases --browser edge

rem pytest -v -s -m "regression"  --html=reports\report_searchby.html testCases --browser firefox
rem pytest -v -s -m "sanity"  --html=reports\report_chrome.html testCases --browser firefox
rem pytest -v -s -m "sanity or regression"  --html=reports\report_searchby.html testCases --browser firefox
rem pytest -v -s -m "sanity and regression"  --html=reports\report_searchby.html testCases --browser firefox
rem pytest -v -s --html=reports\report_searchby.html testCases --browser firefox

start pytest -v -s --html=reports\report_chrome.html testCases\Test_loginPage.py --browser chrome
start pytest -v -s --html=reports\report_edge.html testCases\Test_loginPage.py --browser edge
start pytest -v -s --html=reports\report_firfox.html testCases\Test_loginPage.py --browser firefox