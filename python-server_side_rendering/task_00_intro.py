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

        # Generar nombre del archivo de salida
        output_filename = f"output_{i}.txt"

        # Escribir la plantilla procesada en el archivo de salida
        with open(output_filename, 'w') as output_file:
            output_file.write(personalized_template)
        print(f"Generated: {output_filename}")
