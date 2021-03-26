!pip install yfinance
#!pip install pandas
#!pip install requests
!pip install bs4
#!pip install plotly

tesla=yf.Ticker("TSLA")

tesla_data=tesla.history(period="max")

tesla_data.reset_index(inplace=True)
tesla_data.head()

	level_0	index	Date	Open	High	Low	Close	Volume	Dividends	Stock Splits
0	0	0	2010-06-29	3.800	5.000	3.508	4.778	93831500	0	0.0
1	1	1	2010-06-30	5.158	6.084	4.660	4.766	85935500	0	0.0
2	2	2	2010-07-01	5.000	5.184	4.054	4.392	41094000	0	0.0
3	3	3	2010-07-02	4.600	4.620	3.742	3.840	25699000	0	0.0
4	4	4	2010-07-06	4.000	4.000	3.166	3.222	34334500	0	0.0

url="https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data=requests.get(url).text

soup=BeautifulSoup(html_data,'html5lib')

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date =col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue},ignore_index=True)
    
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

tesla_revenue.dropna(inplace=True)
print(tesla_revenue)

tesla_revenue.tail()

	Date	Revenue
41	2010-09-30	31
42	2010-06-30	28
43	2010-03-31	21
45	2009-09-30	46
46	2009-06-30	27

make_graph(tesla_data, tesla_revenue, 'Tesla')

gamestop=yf.Ticker("GME")

gme_data=gamestop.history(period="max")

gme_data.reset_index(inplace=True)
gme_data.head()

url="https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue?cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork-23455606&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork-23455606&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork-23455606&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork-23455606&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ"
html_data=requests.get(url).text

soup2=BeautifulSoup(html_data,'html5lib')

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in soup2.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date =col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    gme_revenue = gme_revenue.append({"Date":date, "Revenue":revenue},ignore_index=True)
    
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

gme_revenue.tail(5)

	Date	Revenue
59	2006-01-31	1667
60	2005-10-31	534
61	2005-07-31	416
62	2005-04-30	475
63	2005-01-31	709

make_graph(gme_data, gme_revenue, 'GameStop')
