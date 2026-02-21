import markdown
from xhtml2pdf import pisa
import os # Import the os module to handle file paths

def create_pdf(raw_text_content, pdf_path):
    """
    Converts raw text content (with specific markers for headings) to a PDF file using xhtml2pdf.

    Args:
        raw_text_content (str): The raw text to be converted, which will be pre-processed into Markdown.
        pdf_path (str): The full path where the PDF file will be saved.
    """
    # Pre-process the raw text to convert custom markers into Markdown headings
    processed_markdown_lines = []
    lines = raw_text_content.split('\n')

    for line in lines:
        if line.startswith('📘 MOST IMPORTANT TOPICS'):
            # Convert the main title line to an H1 Markdown heading
            processed_markdown_lines.append(f"# {line}")
        elif line.startswith('🔹 Module'):
            # Convert module lines to H2 Markdown headings and remove the '🔹 ' symbol
            processed_markdown_lines.append(f"## {line.replace('🔹 ', '')}")
        elif line.startswith('✅ BONUS QUICK-SCORE TOPICS'):
            # Convert bonus topics line to an H2 Markdown heading and remove the '✅ ' symbol
            processed_markdown_lines.append(f"## {line.replace('✅ ', '')}")
        else:
            # Keep all other lines as is, Markdown will handle lists and bolding
            processed_markdown_lines.append(line)

    processed_markdown_content = "\n".join(processed_markdown_lines)

    # Convert processed Markdown to HTML. 'tables' and 'fenced_code' extensions are included
    # for broader Markdown support, even if not explicitly used by this specific text.
    html_content = markdown.markdown(processed_markdown_content, extensions=['tables', 'fenced_code'])

    # Basic CSS for better PDF formatting.
    # DejaVu Sans is chosen for its good Unicode support, which helps with symbols like 📘 and ✅.
    html_with_css = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Important Topics for Exam</title>
        <style>
            @page {{
                size: letter;
                margin: 1in; /* Standard 1-inch margins on all sides */
            }}
            body {{
                font-family: 'DejaVu Sans', sans-serif;
                line-height: 1.6; /* Comfortable line spacing */
                font-size: 10pt; /* Base font size for the document */
                color: #000000; /* Dark black color for all body text */
            }}
            h1 {{
                font-size: 18pt; /* Larger font size for the main title */
                text-align: center; /* Center align the main title */
                margin-bottom: 20pt; /* Space below the main title */
                color: #000000; /* Dark black color for H1 */
            }}
            h2 {{
                font-size: 14pt; /* Font size for module headings */
                margin-top: 25pt; /* More space above H2 to separate sections */
                margin-bottom: 10pt; /* Space below H2 */
                border-bottom: 1px solid #ddd; /* Light grey border for section separation */
                padding-bottom: 5px; /* Padding below the border */
                color: #000000; /* Dark black color for H2 */
            }}
            h3 {{ /* Styling for potential H3, though not explicitly used in this content */
                font-size: 12pt;
                margin-top: 15pt;
                margin-bottom: 5pt;
                color: #000000; /* Dark black color for H3 */
            }}
            p {{
                margin-bottom: 8pt; /* Standard paragraph spacing */
            }}
            ul, ol {{
                margin-left: 20pt; /* Indentation for lists */
                margin-bottom: 10pt; /* Space below lists */
            }}
            li {{
                margin-bottom: 3pt; /* Spacing between list items */
                padding-left: 5pt; /* Small left padding for list items */
            }}
            code {{
                font-family: "Courier New", Courier, monospace; /* Monospace font for code */
                background-color: #f0f0f0; /* Light background for code snippets */
                padding: 2px 4px; /* Padding around code text */
                border-radius: 3px; /* Slightly rounded corners for code blocks */
                font-size: 9pt; /* Smaller font size for code */
            }}
            hr {{
                border: 0; /* Remove default border */
                height: 1px; /* Make it a thin line */
                background: #ccc; /* Light grey color for horizontal rule */
                margin: 25pt 0; /* Space above and below horizontal rule */
            }}
            /* Specific styling for bold and italic text */
            strong {{
                font-weight: bold;
            }}
            em {{
                font-style: italic;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Create PDF
    try:
        with open(pdf_path, "wb") as pdf_file:
            # pisa.CreatePDF converts the HTML string to a PDF file
            pisa_status = pisa.CreatePDF(
                html_with_css,  # The HTML content to convert
                dest=pdf_file,  # The file handle to write the PDF output to
                encoding='UTF-8' # Ensure proper character encoding
            )
        if not pisa_status.err:
            print(f"PDF successfully created at {os.path.abspath(pdf_path)}")
        else:
            print(f"Error creating PDF: {pisa_status.err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# The raw text content to be converted to PDF.
# The script will automatically convert lines starting with '📘' and '🔹' into Markdown headings.
raw_text_content = """📘 MOST IMPORTANT TOPICS TO STUDY FIRST (HIGHLY LIKELY IN EXAM)
🔹 Module 1: Introduction to DBMS
Definition & Purpose of DBMS
Database vs. File System (advantages of DBMS over file system)
Data Models:
Hierarchical
Network
Relational (VERY IMPORTANT)
Object-Oriented
DBMS Architecture:
1-tier, 2-tier, 3-tier
Data Independence:
Logical vs. Physical
DBA Roles & Responsibilities
Entity, Attribute, Domain, Tuple, Relation
🔹 Module 2: Relational Model & RDBMS Concepts
Codd’s 12 Rules
Keys in RDBMS:
Primary, Candidate, Super, Foreign, Composite
Relational Algebra (VERY LIKELY):
Select, Project, Union, Set Difference, Cartesian Product, Rename
Relational Calculus (Tuple and Domain)
Integrity Constraints:
Entity, Referential, Domain
Schema vs. Instance
🔹 Module 3: SQL (Structured Query Language)
Data Definition Language (DDL):
CREATE, DROP, ALTER
Data Manipulation Language (DML):
SELECT, INSERT, UPDATE, DELETE
Data Control Language (DCL):
GRANT, REVOKE
Basic SQL Queries:
SELECT with WHERE, GROUP BY, ORDER BY, HAVING
Joins (VERY IMPORTANT):
Inner, Left, Right, Full Outer
Nested Queries & Subqueries
Aggregate Functions:
COUNT, SUM, AVG, MIN, MAX
Views and Indexes
🔹 Module 4: Database Design & ER Model
Entity-Relationship (ER) Model:
Entity, Relationship, Attributes
ER Diagrams (Symbols: Rectangle, Diamond, Oval, etc.)
Cardinality: 1:1, 1:N, M:N
Generalization, Specialization, Aggregation
Mapping ER Model to Relational Schema
🔹 Module 5: Normalization & Functional Dependencies
Functional Dependency (FD)
Anomalies in Unnormalized Data (Insertion, Deletion, Update)
Normalization:
1NF, 2NF, 3NF, BCNF (VERY IMPORTANT – with examples)
Multi-valued Dependency & 4NF (optional, if time permits)
🔹 Module 6: Transaction Management & Concurrency Control
ACID Properties
Transaction States: Active, Partially Committed, Failed, Aborted, Committed
Schedules:
Serial, Non-Serial
Conflict Serializability (VERY LIKELY)
Concurrency Control Techniques:
Lock-based Protocols (2PL – Two Phase Locking)
Timestamp-based Protocols
Deadlock Handling (Detection, Prevention)
Recovery Techniques:
Log-Based, Checkpointing
✅ BONUS QUICK-SCORE TOPICS (Short Questions)
DBMS vs. RDBMS
Difference between DELETE, TRUNCATE, and DROP
Candidate Key vs. Primary Key
Data Dictionary
DDL vs DML vs DCL vs TCL
View vs Table
SQL vs NoSQL
Data Redundancy & Data Integrity
Cardinality & Degree
NULL vs 0 vs ‘’ (empty string)
Trigger, Cursor, Stored Procedure (Definitions)"""

if __name__ == '__main__':
    # Define the output PDF file path
    pdf_file_path = "important_topics.pdf"
    create_pdf(raw_text_content, pdf_file_path)
