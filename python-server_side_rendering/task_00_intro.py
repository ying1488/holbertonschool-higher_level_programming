import sys, os, logging

def generate_invitations(template_content, attendees):
    if not isinstance(template_content, str) or not isinstance(attendees, list):
        sys.exit()

    # remove whitespacesfrom input
    template_content = template_content.strip()

    if len(template_content) == 0:
        logging.warning("template_content is empty")
        sys.exit()
    
    if len(attendees) == 0:
        logging.warning("attendees is empty")
        sys.exit()
    
    count = 1 
    for row in attendees:
        template_copy = template_content

        for key in ["name", "event_title", "event_date", "event_location"]:
            value = ""
            to_replace = "{" + key + "}"

            # Not just the value! if the key is missing, we should also add 'N/A'
            if key not in row: 
                value = "N/A"
            else:
                value = row[key]
            
            if value == "" or value is None:
                value = "N/A"
            template_copy = template_copy.replace(to_replace, value)
        count = count + 1 
        f = open("output_" + str(count) + ".txt", "a")
        f.write(template_copy)
        f.close()
 
