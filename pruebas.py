from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Objeto que puede almacenar texto
from io import StringIO 
import os
import platform
import time
#Libreria que accede al sistema y a la salida stdout que va a la consola
import sys 

#Inicializa un contenedor para capturar el texto que saldria por print
console_output = StringIO() 
#Redirige lo que se imprime con print hacia el objeto console_output
sys.stdout = console_output

# Definir carpeta de descargas según SO con la ayuda de platform.system()
if platform.system() == "Windows":
     download_dir = r"C:\downloads"
else:
    download_dir = os.path.expanduser("~/downloads")

#Asegura la existencia de la carpeta
os.makedirs(download_dir, exist_ok=True)

#Configurar Chrome en modo headless, acepatando cookies de terceros para
# el funcionamiento correcto y configuración de descargas automaticas
options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-features=BlockThirdPartyCookies")
options.add_argument("--disable-features=SameSiteByDefaultCookies")

prefs = {
        #Define la carpeta de descarga
        "download.default_directory": download_dir, 
        #Desactiva diálogos de descarga (ventanas secundarias)
        "download.prompt_for_download": False, 
        #Impide la aparición de pop ups
        "profile.default_content_settings.popups": 0, 
        #Permite descargas de multiples archivos
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1 
    }

#Se agregan las preferencias a las opciones
options.add_experimental_option("prefs", prefs)
#Se inicializa el driver con las opciones previamente definidad
driver = webdriver.Chrome(options=options)
#Se configura para que Chrome ocupe toda la pantalla
driver.maximize_window()
#Se crea una variable wait que esperar 10 segundos para re utilizar durante varios pasos
#de la ejecución
wait = WebDriverWait(driver, 10)

try:
    #Inicia la prueba de registro usuario en la URL especificada
    print("Iniciando prueba: Registro de Usuario...")
    driver.get("https://demoqa.com/automation-practice-form")
    #Captura los elementos (campos de texto) por el ID
    driver.find_element(By.ID, "firstName").send_keys("Juan")
    driver.find_element(By.ID, "lastName").send_keys("Sanabria")
    driver.find_element(By.ID, "userEmail").send_keys("juansanabria@gmail.com")
    #Selecciona el genero por el XPATH, en este caso con el input ID
    genero = driver.find_element(By.XPATH, "//input[@id='gender-radio-1']")
    #Espera mientras lo encuentra antes de dar click con el .SPACE
    time.sleep(2)
    genero.send_keys(Keys.SPACE)
    #Captura los elementos (campos de texto) por el ID
    driver.find_element(By.ID, "userNumber").send_keys("3224052439")
    #Hace click en el botón submit usando javascript evitando errores por superposición
    driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "submit"))
    #Espera hasta que un elemento con el texto establecido aparezca y lo almacena en "msg"
    msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Thanks for submitting the form']"))).text
    #Condicional que valida si el texto se encuentra en "msg" para dar una respuesta acorde
    if "Thanks for submitting the form" in msg:
        print("Registro de usuario exitoso")
    else:
        print("Registro de usuario fallido. Mensaje no encontrado")

    #Inicia la prueba de carga de archivos abriendo la URL especificada
    print("\nIniciando prueba: Carga de Archivos...")
    driver.get("https://demoqa.com/upload-download")
    time.sleep(2)
    #Crea la variable que almacena la ruta absoluta del archivo especificado
    file = os.path.abspath("test_image.jpg") 
    #Ubica el elemento con el ID dado que es el boton que subira el archivo
    subir_archivo = driver.find_element(By.ID, "uploadFile")
    #Espera 2 segundos y envia la ruta del archivo para subirlo
    time.sleep(2)
    subir_archivo.send_keys(file)
    #Espera hasta que en el elemento con el ID dado genere un texto y lo almacena en la variable
    nombre_carga = wait.until(EC.visibility_of_element_located((By.ID, "uploadedFilePath"))).text
    #Condicional que valida que el archivo se halla subido correctamente con el nombre del archivo
    if "test_image.jpg" in nombre_carga:
        print("Archivo subido correctamente")
    else:
        print("Error al subir el archivo")

    #Inicia la prueba de descarga de archivos abriendo la URL especificada
    print("\nIniciando prueba: Descarga de Archivos...")
    driver.get("https://demoqa.com/upload-download")
    #Ubica el elemento por el ID especificado y lo almacena en la variable
    descarga_boton = driver.find_element(By.ID, "downloadButton")
    #Espera 2 segundos y da click en el boton
    time.sleep(2)
    descarga_boton.click()
    #Con el join une la ruta de descargas con el nombre del archivo y lo almacena en la variable
    downloaded_path = os.path.join(download_dir, "sampleFile.jpeg")
    #Crea una constante con el valor de 15
    timeout = 15
    #Variable que guarda el momento exacto en que comienza una operación
    start_time = time.time()
    ##Ciclo que espera 15 segundos por la descarga y valida cada segundo
    while True:
        resta = time.time() - start_time
        if resta >= timeout:
            print(f"No se encontró 'sampleFile.jpeg' en {download_dir} dentro de {timeout} segundos")
            break
        if os.path.exists(downloaded_path):
            print(f"Archivo descargado en: {downloaded_path}")
            break
        time.sleep(1)

    #Inicia la prueba de alertas abriendo la URL especificada
    print("\nIniciando prueba: Alertas...")
    driver.get("https://demoqa.com/alerts")
    #Ubica el botón por el ID dado, lo almacena en la variable y espera 2 segundos
    confirmar_boton = driver.find_element(By.ID, "confirmButton")
    time.sleep(2)
    #Condicional que si encuentra el boton da click y confirma que lo encontro
    if(confirmar_boton):
        print("Se encontro el boton confirmar")
        confirmar_boton.click()

        wait.until(EC.alert_is_present())

        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        #Espera hasta que en el elemento con el ID dado genere un texto y lo almacena en la variable
        result_confirm = wait.until(EC.visibility_of_element_located((By.ID, "confirmResult"))).text
        #Si el texto OK se encuentra en la variable confirma que fue aceptada
        if "Ok" in result_confirm:
            print("Alert confirm aceptada")
        else:
            print("Resultado de alert confirm no esperado")
    else:
        print("No se encontro el boton")
    
    #Espera 5 segundos para ubicar el otro botón con el ID dado
    time.sleep(5)
    promp_boton = driver.find_element(By.ID, "promtButton")
    time.sleep(2)
    #Condicional que si encuentra el boton da click y confirma que lo encontro
    if(promp_boton):
        print("Se encontro el boton prompt")
        promp_boton.click()

        wait.until(EC.alert_is_present())

        prompt = driver.switch_to.alert
        time.sleep(2)
        #Por el tipo de alerta enviamos el texto y damos aceptar
        prompt.send_keys("Nicolas")
        prompt.accept()
        #Espera hasta que en el elemento con el ID dado genere un texto y lo almacena en la variable
        result_prompt = wait.until(EC.visibility_of_element_located((By.ID, "promptResult"))).text
        #Si el texto Nicolas se encuentra en la variable confirma que fue aceptada
        if "Nicolas" in result_prompt:
            print("Prompt alert procesada con texto correcto")
        else:
            print("El texto ingresado en el prompt no se refleja correctamente")
    else:
        print("No se encontro el boton")
    #Imprime que todas las pruebas finalizaron   
    print("\nTodas las pruebas finalizaron.")
finally:
    time.sleep(5) 
    #Al finalizar devielve la salida por consola por si hay futuros print
    sys.stdout = sys.__stdout__
    #Contenido del reporte HTML
    #Se usa f-string para incluir variables como fecha y el contenido capturado
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Reporte de Pruebas Selenium - DemoQA</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }}
            h1 {{ color: #333; }}
            pre {{ background: #fff; padding: 15px; border: 1px solid #ccc; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>Reporte de Pruebas Automatizadas</h1>
        <p><strong>Fecha:</strong> {time.strftime("%Y-%m-%d %H:%M:%S")}</p>
        <pre>{console_output.getvalue()}</pre>
    </body>
    </html>
    """
    #{console_output.getvalue()} inserta todo lo impreso con print() dentro de una etiqueta
    #<pre> para que mantenga los saltos de linea y espcaciados

    # Guardar en un archivo HTML
    #Abre un archivo llamada reporte.html en modo escritura con codificación UTF-8
    with open("reporte.html", "w", encoding="utf-8") as f:
        #Escribe el contenido HTML generado en ese archivo
        f.write(html_content)
    #Confirma que el reporte se creo con el nombre
    print("Reporte generado en: reporte.html")
    input("Presione enter para cerrar el navegador")
    driver.quit()
