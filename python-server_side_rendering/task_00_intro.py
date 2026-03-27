#!/usr/bin/env python3
"""Simple templating program for generating personalized invitations."""


def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template and attendees.

    Args:
        template: A string containing placeholders like {name}, {event_title}.
        attendees: A list of dictionaries with attendee data.
    """
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Invalid input type for attendees. Expected a list of dictionaries.")
        return

    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for i, attendee in enumerate(attendees, start=1):
        output = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        filename = f"output_{i}.txt"
        with open(filename, "w") as f:
            f.write(output)
