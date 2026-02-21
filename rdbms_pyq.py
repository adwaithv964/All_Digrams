from xhtml2pdf import pisa

def create_pdf(output_path):

    html = """
    <html>
    <head>
    <style>

        body {
    font-family: Times New Roman;
    font-size: 12px;   /* overall text */
    margin: 40px;
}

table {
    border-collapse: collapse;
    width: 100%;
    table-layout: fixed;
}

th {
    font-size: 14px;   /* BIGGER HEADER */
    font-weight: bold;
    padding: 12px;
}

td {
    font-size: 12px;   /* normal content */
    padding: 12px;     /* more row height */
}

th, td {
    border: 1px solid black;
    text-align: center;
    vertical-align: middle;
}


    </style>
    </head>

    <body>

    <table>

        <tr>
            <th>Field Name</th>
            <th>Data Type</th>
            <th>Description</th>
        </tr>

        <tr><td>_id</td><td>ObjectId</td><td>Unique identifier</td></tr>
        <tr><td>userId</td><td>ObjectId</td><td>Reference to User</td></tr>
        <tr><td>subject</td><td>String</td><td>Subject studied</td></tr>
        <tr><td>topic</td><td>String</td><td>Specific topic covered</td></tr>
        <tr><td>duration</td><td>Number</td><td>Actual duration in hours</td></tr>
        <tr><td>plannedDuration</td><td>Number</td><td>Planned duration in minutes</td></tr>
        <tr><td>startTime</td><td>String</td><td>Session start time (ISO)</td></tr>
        <tr><td>notes</td><td>String</td><td>Session notes/reflections</td></tr>
        <tr><td>createdAt</td><td>Date</td><td>Record creation timestamp</td></tr>

    </table>

    </body>
    </html>
    """

    with open(output_path, "wb") as f:
        pisa.CreatePDF(html, dest=f)


create_pdf("final_clean_table.pdf")
print("Done")
