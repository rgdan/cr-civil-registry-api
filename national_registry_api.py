from flask import Flask, render_template, request, jsonify
from playwright.sync_api import Playwright, sync_playwright
from bs4 import BeautifulSoup

app = Flask(__name__)

def parse_id_html_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = {
        "id_number": soup.find("span", {"id": "lblcedula"}).text if soup.find("span", {"id": "lblcedula"}) else "N/A",
        "full_name": soup.find("span", {"id": "lblnombrecompleto"}).text if soup.find("span", {"id": "lblnombrecompleto"}) else "N/A",
        "birthday": soup.find("span", {"id": "lblfechaNacimiento"}).text if soup.find("span", {"id": "lblfechaNacimiento"}) else "N/A",
        "nationality": soup.find("span", {"id": "lblnacionalidad"}).text if soup.find("span", {"id": "lblnacionalidad"}) else "N/A",
        "alias": soup.find("span", {"id": "lblconocidocomo"}).text if soup.find("span", {"id": "lblconocidocomo"}) else "N/A",
        "homeless": soup.find("span", {"id": "lblLeyendaMarginal"}).text if soup.find("span", {"id": "lblLeyendaMarginal"}) else "N/A",
        "death_date": soup.find("span", {"id": "lbldefuncion2"}).text if soup.find("span", {"id": "lbldefuncion2"}) else "N/A",
        "father": soup.find("span", {"id": "lblnombrepadre"}).text if soup.find("span", {"id": "lblnombrepadre"}) else "N/A",
        "father_id_number": soup.find("span", {"id": "lblid_padre"}).text if soup.find("span", {"id": "lblid_padre"}) else "N/A",
        "mother": soup.find("span", {"id": "lblnombremadre"}).text if soup.find("span", {"id": "lblnombremadre"}) else "N/A",
        "mother_id_number": soup.find("span", {"id": "lblid_madre"}).text if soup.find("span", {"id": "lblid_madre"}) else "N/A"
    }
    return data

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/id_lookup', methods=['GET'])
def id_lookup():
    id_number = request.args.get('id')
    if not id_number:
        return jsonify({"error": "ID number is required"}), 400

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://servicioselectorales.tse.go.cr/chc/consulta_cedula.aspx")
        page.get_by_placeholder("Digite el número de cédula ahora").click()
        page.get_by_placeholder("Digite el número de cédula ahora").fill(id_number)
        page.get_by_role("button", name="Consultar").click()
        page.wait_for_timeout(1000)

        html_content = page.content()
        data = parse_id_html_content(html_content)

        context.close()
        browser.close()

    return jsonify(data)

@app.route('/name_lookup', methods=['GET'])
def name_lookup():
    first_name = request.args.get('first_name')
    last_name1 = request.args.get('last_name1')
    last_name2 = request.args.get('last_name2')
    pass

if __name__ == '__main__':
    app.run(debug=True)
