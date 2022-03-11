# downloadPdf
Process of downloading pdf files with Selenium searching for keywords in the link.

## previous steps
* pip3 install virtualenv
* python3 -m venv env
* source env/bin/activate
* python3 -m pip install --upgrade pip
* pip3 install -r requirements

## launching example
python3 downloadPdf.py --down /home/$USER/Desktop/ /home/$USER/Desktop/geckodriver https://cfiscal.contraloria.gov.co/Reportes/ConsultaBoletinesTrimestrales.aspx Boletin 

## news
This capsule is created in order to have a starting point for downloading the Contraloria's quarterly bulletin using selenium with firefox webdriver fully configured to skip download accept popup.

[Boletín de Responsables Fiscales formato PDF](https://cfiscal.contraloria.gov.co/Reportes/ConsultaBoletinesTrimestrales.aspx)

[capsules against amnecia]
