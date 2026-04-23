import os
import json
import csv
import configparser
import xml.etree.ElementTree as ET
import pip install pyyaml

class FileManager:
    def __init__(self):
        # Carpeta donde se guardarán los resultados
        self.output_folder = "output"
        # Crear carpeta si no existe
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    # ==============================================
    # 1. Leer archivo TXT
    # ==============================================
    def read_txt_file(self, filename):
        """Lee el archivo 2-1 mit.txt y retorna lista de diccionarios"""
        students_list = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                # Leer todas las lineas
                lines = file.readlines()
                
                # Omitimos la primera linea si es el encabezado
                for line in lines[1:]:
                    # Limpiamos espacios y separamos por espacios
                    parts = line.strip().split()
                    
                    if len(parts) >= 3:
                        # Estructura: ApellidoP ApellidoM Nombre
                        student = {
                            "apellidos": f"{parts[0]} {parts[1]}",
                            "nombres": parts[2],
                            # ✅ LLENANDO INFORMACIÓN FALTANTE
                            "grado": "2",       
                            "grupo": "j",       
                            "turno": "vespertino" 
                        }
                        students_list.append(student)
                        
            return students_list
        except FileNotFoundError:
            print(f"Error: El archivo {filename} no fue encontrado.")
            return []

    # ==============================================
    # 2. Ordenar por Apellidos
    # ==============================================
    def sort_by_lastname(self, data):
        """Ordena la lista alfabeticamente por apellidos"""
        # sorted ordena, key=lambda busca ordenar basado en la clave 'apellidos'
        return sorted(data, key=lambda x: x['apellidos'])

    # ==============================================
    # 3. Guardar JSON
    # ==============================================
    def save_json(self, data, filename="students.json"):
        path = os.path.join(self.output_folder, filename)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Archivo {filename} creado exitosamente.")

    # ==============================================
    # 4. Guardar CSV
    # ==============================================
    def save_csv(self, data, filename="students.csv"):
        path = os.path.join(self.output_folder, filename)
        with open(path, 'w', newline='', encoding='utf-8') as f:
            # Obtener nombres de columnas
            fieldnames = data[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            # Escribir encabezado
            writer.writeheader()
            # Escribir datos
            writer.writerows(data)
        print(f"Archivo {filename} creado exitosamente.")

    # ==============================================
    # 5. Guardar INI
    # ==============================================
    def save_ini(self, data, filename="students.ini"):
        path = os.path.join(self.output_folder, filename)
        config = configparser.ConfigParser()
        
        for i, student in enumerate(data):
            # Crear sección para cada alumno
            section_name = f"ALUMNO_{i+1}"
            config[section_name] = student
        
        with open(path, 'w') as configfile:
            config.write(configfile)
        print(f"Archivo {filename} creado exitosamente.")

    # ==============================================
    # 6. Guardar YAML
    # ==============================================
    def save_yaml(self, data, filename="students.yaml"):
        path = os.path.join(self.output_folder, filename)
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False)
        print(f"Archivo {filename} creado exitosamente.")

    # ==============================================
    # 7. Guardar XML
    # ==============================================
    def save_xml(self, data, filename="students.xml"):
        path = os.path.join(self.output_folder, filename)
        # Crear nodo raíz
        root = ET.Element("students")
        
        for student in data:
            # Crear nodo estudiante
            student_elem = ET.SubElement(root, "student")
            # Agregar hijos
            for key, value in student.items():
                child = ET.SubElement(student_elem, key)
                child.text = str(value)
        
        # Crear árbol y guardar
        tree = ET.ElementTree(root)
        tree.write(path, encoding='utf-8', xml_declaration=True)
        print(f"Archivo {filename} creado exitosamente.")

# ==============================================
# EJECUCIÓN DEL PROGRAMA
# ==============================================
if __name__ == "__main__":
    print("=== INICIANDO PROCESO DE MANEJO DE ARCHIVOS ===")
    
    # Crear objeto
    manager = FileManager()
    
    # PASO 1: Leer datos
    print("\nLeyendo archivo 2-1 mit.txt...")
    students_data = manager.read_txt_file("2-1 mit.txt")
    
    if students_data:
        # PASO 2: Ordenar
        print("Ordenando por apellidos...")
        sorted_data = manager.sort_by_lastname(students_data)
        
        # PASO 3: Generar todos los archivos
        print("\nGenerando archivos de salida...\n")
        
        manager.save_json(sorted_data)
        manager.save_csv(sorted_data)
        manager.save_ini(sorted_data)
        manager.save_yaml(sorted_data)
        manager.save_xml(sorted_data)
        
        print("\n✅ PROCESO FINALIZADO. Revisa la carpeta 'output'")
    else:
        print("No hay datos para procesar, revisa el archivo.")