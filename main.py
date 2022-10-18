import requests

url = "https://qualysapi.qg3.apps.qualys.com/qps/rest/3.0/create/was/webapp"

headers ={
    'X-Requested-With':'EXTRACT',
    'Authorization':'YOUR USER:PASS IN BASE64'
}
xml_template = """<ServiceRequest>
<data>
<WebApp>
<name><![CDATA[My Web Application]]></name>
    <url><![CDATA[http://mywebapp.com]]></url>
</WebApp>
</data>
</ServiceRequest>"""
f = open('urls.txt', 'r')
conteudo = f.readlines()
for linha in conteudo:
    xml = xml_template.replace("My Web Application", linha)
    xml_t= xml.replace("http://mywebapp.com",linha)

    chuck_size_calc=20*1024
    with requests.request("POST",url,stream=True,headers=headers,data=xml_t) as r:
        with open("kb_full.xml","w") as f:
            for chuck in r.iter_content(chunk_size=chuck_size_calc):
                f.write(chuck.decode('utf-8'))