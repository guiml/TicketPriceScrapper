from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from io import open

driver = webdriver.Chrome(executable_path='./geckodriver.exe')
driver.get("http://www.submarinoviagens.com.br/travel/resultado-passagens.aspx?searchtype=Air&Origem=POA&Destino=JFK&Origem=JFK&Destino=POA&Proximity=&ProximityId=0&Data=11-11-2019&RoundTrip=1&Data=15-11-2019&SomenteDireto=false&ExecutiveFlight=false&NumADT=1&NumCHD=0&NumINF=0&Hora=&Hora=&Multi=false&pmkt=60&utm_source=melhores_destinos&utm_medium=post&utm_campaign=listagem_passagens-aereas")
file = open("Output.html", "w", encoding="utf-8")
file.write(driver.page_source)

