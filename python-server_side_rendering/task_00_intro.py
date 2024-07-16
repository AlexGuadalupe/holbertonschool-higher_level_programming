from task_00_intro import generate_invitations
import os


def generate_invitations(template, attendees):
    # Verificar tipos de entrada
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries")
        return

    # Verificar si la plantilla está vacía
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Verificar si la lista de asistentes está vacía
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Procesar cada asistente
    for i, attendee in enumerate(attendees, start=1):
        # Reemplazar los marcadores de posición en la plantilla con los valores correspondientes
        personalized_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            personalized_template = personalized_template.replace(
                f"{{{key}}}", value)

        # Generar nombre para archivo de salida
        output_filename = f"output_{i}.txt"

        # Escribir la plantilla procesada en el archivo de salida
        with open(output_filename, 'w') as output_file:
            output_file.write(personalized_template)
        print(f"Generated: {output_filename}")


# Paso 4: Probar la Función
# Leer la plantilla de un archivo
with open('template.txt', 'r') as file:
    template_content = file.read()

# Lista de asistentes
attendees = [
    {"name": "Alice", "event_title": "Python Conference",
        "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop",
        "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit",
        "event_date": None, "event_location": "Boston"}
]

# Llamar a la función con la plantilla y la lista de asistentes
generate_invitations(template_content, attendees)
