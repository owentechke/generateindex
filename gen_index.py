import os

header_info = f"<html>\n<head>\n<title>Index</title>\n"
header_info += "<link rel='icon' href='icon.png' type='image/png'>\n" 
header_info += "<link rel='stylesheet' href='style1.css' type='text/css'>\n" 
header_info += "</head>\n<body background='backg.jpg'>\n" 
index_text = header_info + "<ul>\n"
for filename in os.listdir():
    if filename.endswith(".html"):
        filename_parts = filename.split('.')
        filename_without_extension = filename_parts[0]
        print(filename_without_extension)
        index_text += f"\t<li><a href='{filename}'>{filename_without_extension}</a></li>\n"

index_text += "</ul>\n</body>"        
html_file = open("index.html", 'w')
print(index_text, file = html_file)
html_file.close()