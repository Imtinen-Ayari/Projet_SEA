import csv

# Nom du fichier CSV généré par le crawler
csv_file = 'crawl_results.csv'
# Nom du fichier HTML de sortie
html_file = 'crawl_results.html'

# Lecture des données à partir du fichier CSV
data = []
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Génération du contenu HTML
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Résultats du Crawling</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 15px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Résultats du Crawling</h1>
    <table>
        <thead>
            <tr>
                <th>URL</th>
                <th>Title</th>
            </tr>
        </thead>
        <tbody>
"""

# Ajouter les lignes de données à la table HTML
for row in data:
    html_content += "<tr>"
    for cell in row:
        html_content += f"<td>{cell}</td>"
    html_content += "</tr>"

# Fermer les balises HTML
html_content += """
        </tbody>
    </table>
</body>
</html>
"""

# Écrire le contenu HTML dans le fichier
with open(html_file, mode='w', encoding='utf-8') as file:
    file.write(html_content)

print(f'Le fichier HTML a été généré : {html_file}')
