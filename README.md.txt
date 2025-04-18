Proyecto de Automatización con Selenium - DemoQA

Este proyecto automatiza pruebas en el sitio(https://demoqa.com) utilizando Selenium WebDriver en modo headless, abarcando formularios, carga/descarga de archivos y alertas.

---

## Funcionalidades probadas

- Registro de usuario (formulario)
- Carga de archivos (`Upload`)
- Descarga de archivos (`Download`)
- Interacción con alertas (`Confirm` y `Prompt`)
- Ejecución en modo headless
- Manejo de descargas automáticas sin intervención

---

## Requisitos del sistema

- Python 3.8 o superior
- Google Chrome instalado
- Sistema operativo: **Windows** (esta versión está configurada para Windows)

---

##Instalación y configuración

1. Clonar el repositorio

git clone https://github.com/Juanico1/Pruebas_Automaticas_Selenium.git
cd Pruebas_Automaticas_Selenium

2. Instalar Dependencias

pip install selenium

3. Ejecución de Pruebas

Correr el script principal "pruebas.py"

4. Estructura del proyecto 

Automatizacion_Pruebas/
+-- pruebas.py              # Script principal con las pruebas
+-- test_image.jpg          # Archivo usado para prueba de carga
+-- reporte.html            # Reporte generado con resultados
+-- README.md

---

##Detalles técnicos

1. Modo Headless

Se configura en el navegador con:

options.add_argument("--headless")

Esto permite ejecutar las pruebas sin abrir una ventana de navegador.

2. Descargas automáticas

El navegador Chrome fue configurado con las siguientes preferencias para gestionar descargas de forma automática:

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

---

Proyecto realizado por Juan Nicolas Sanabria Gomez para la asignatura de Pruebas de Software – 2025