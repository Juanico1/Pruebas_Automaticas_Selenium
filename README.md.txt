Proyecto de Automatizaci�n con Selenium - DemoQA

Este proyecto automatiza pruebas en el sitio(https://demoqa.com) utilizando Selenium WebDriver en modo headless, abarcando formularios, carga/descarga de archivos y alertas.

---

## Funcionalidades probadas

- Registro de usuario (formulario)
- Carga de archivos (`Upload`)
- Descarga de archivos (`Download`)
- Interacci�n con alertas (`Confirm` y `Prompt`)
- Ejecuci�n en modo headless
- Manejo de descargas autom�ticas sin intervenci�n

---

## Requisitos del sistema

- Python 3.8 o superior
- Google Chrome instalado
- Sistema operativo: **Windows** (esta versi�n est� configurada para Windows)

---

##Instalaci�n y configuraci�n

1. Clonar el repositorio

git clone https://github.com/Juanico1/Pruebas_Automaticas_Selenium.git
cd Pruebas_Automaticas_Selenium

2. Instalar Dependencias

pip install selenium

3. Ejecuci�n de Pruebas

Correr el script principal "pruebas.py"

4. Estructura del proyecto 

Automatizacion_Pruebas/
+-- pruebas.py              # Script principal con las pruebas
+-- test_image.jpg          # Archivo usado para prueba de carga
+-- reporte.html            # Reporte generado con resultados
+-- README.md

---

##Detalles t�cnicos

1. Modo Headless

Se configura en el navegador con:

options.add_argument("--headless")

Esto permite ejecutar las pruebas sin abrir una ventana de navegador.

2. Descargas autom�ticas

El navegador Chrome fue configurado con las siguientes preferencias para gestionar descargas de forma autom�tica:

prefs = {
        #Define la carpeta de descarga
        "download.default_directory": download_dir, 
        #Desactiva di�logos de descarga (ventanas secundarias)
        "download.prompt_for_download": False, 
        #Impide la aparici�n de pop ups
        "profile.default_content_settings.popups": 0, 
        #Permite descargas de multiples archivos
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1 
    }

---

Proyecto realizado por Juan Nicolas Sanabria Gomez para la asignatura de Pruebas de Software � 2025