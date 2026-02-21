import markdown
from xhtml2pdf import pisa
import os

def create_exam_pdf(raw_text_content, pdf_path):
    """
    Converts structured exam content into a colorful, styled PDF using xhtml2pdf.

    Args:
        raw_text_content (str): The raw text of the exam paper, formatted with Markdown.
        pdf_path (str): The full path where the generated PDF file will be saved.
    """
    # The raw_text_content is already structured as Markdown, so no
    # additional pre-processing for custom symbols (like 📘, 🔹, ✅) is needed.
    # Markdown will handle headings, lists, and code blocks directly.
    # We include 'fenced_code' for code blocks, 'tables' for any potential tables,
    # and 'nl2br' to convert single newlines into <br> tags, preserving line breaks
    # within paragraphs and list items as seen in the input.
    html_content = markdown.markdown(raw_text_content, extensions=['tables', 'fenced_code', 'nl2br'])

    # Embed CSS to stylize the HTML for PDF, ensuring a neat and standard colorful appearance
    html_with_css = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Exam Paper</title>
        <style>
            @page {{
                size: A4; /* Using A4 paper size for the PDF */
                margin: 1in; /* Standard 1-inch margins on all sides */
            }}
            body {{
                font-family: 'DejaVu Sans', sans-serif; /* A Unicode-friendly font for broad character support */
                font-size: 10pt;
                color: #34495e; /* A dark slate grey for general body text for readability */
                line-height: 1.6; /* Generous line spacing for readability */
            }}
            /* Main Paper Title (hardcoded in HTML as it's not part of the Markdown `raw_text_content`) */
            h1 {{
                font-size: 18pt; /* Large font size for the main exam title */
                text-align: center;
                color: #2E86C1; /* A professional blue for emphasis */
                margin-bottom: 5pt;
                line-height: 1.2;
            }}
            /* Course Code/Title (hardcoded in HTML) */
            h2.course-title {{
                font-size: 14pt;
                text-align: center;
                color: #117864; /* A deep forest green for contrast */
                margin-top: 5pt;
                margin-bottom: 5pt; /* Reduced margin */
            }}
            .header-info {{
                font-size: 10pt;
                text-align: center;
                color: #555;
                margin-top: 2pt;
                margin-bottom: 2pt;
            }}
            /* Horizontal Rule for separation */
            hr {{
                border: 0;
                height: 1px;
                background: #bdc3c7; /* Light grey line for subtle division */
                margin: 25pt 0; /* Space above and below the line */
            }}
            /* Section Headings (e.g., "Section A – Short Answer Type Questions") */
            h2 {{
                font-size: 14pt;
                color: #117864; /* Consistent deep green for section titles */
                margin-top: 25pt; /* More space above new sections for clear breaks */
                margin-bottom: 10pt;
                border-bottom: 1px solid #ccc; /* Subtle bottom border */
                padding-bottom: 4px;
            }}
            /* Styling for the "(Each question carries..." lines (rendered as paragraphs by Markdown) */
            .ceiling-info {{
                font-size: 9pt;
                color: #7f8c8d; /* Soft grey for less prominent text */
                text-align: right;
                margin-top: -5pt; /* Pull text up to be closer to its section heading */
                margin-bottom: 15pt;
            }}
            /* Sub-headings within sections (e.g., "5. What are domain constraints?") */
            h3 {{ /* Note: With the new Markdown for questions 5-12, H3 will be less used for question numbers */
                font-size: 12pt;
                color: #B03A2E; /* A warm reddish-brown for distinct sub-headings */
                margin-top: 15pt;
                margin-bottom: 5pt;
            }}
            /* Bold text (Markdown `**text**` becomes `<strong>text</strong>`) */
            strong {{
                color: #1A5276; /* Dark blue for emphasized text */
            }}
            /* Italic text (Markdown `*text*` becomes `<em>text</em>`) */
            em {{
                font-style: italic;
            }}
            /* Standard paragraph spacing */
            p {{
                margin-bottom: 8pt;
            }}
            /* Styling for unordered and ordered lists */
            ul, ol {{
                margin-left: 20pt; /* Indentation for lists */
                margin-bottom: 10pt;
            }}
            li {{
                margin-bottom: 4pt; /* Spacing between individual list items */
            }}
            /* Styling for code blocks (Markdown fenced code blocks) */
            pre {{
                font-family: "Courier New", monospace; /* Monospace font for code */
                background-color: #f8f8f8; /* Very light grey background for code blocks */
                border: 1px solid #ccc; /* Subtle border */
                padding: 10px; /* Generous padding around code */
                border-radius: 3px; /* Slightly rounded corners */
                margin: 10px 0; /* Space above and below code blocks */
                overflow-x: auto; /* Enable horizontal scrolling for long code lines */
            }}
            /* Styling for inline code (Markdown `` `code` ``) */
            code {{
                font-family: "Courier New", monospace;
                background-color: #eee; /* Lighter background for inline code */
                padding: 2px 4px;
                border-radius: 3px;
                font-size: 9pt;
                color: #C0392B; /* A distinct reddish color for inline code */
            }}
            /* Styling for mark allocations (e.g., (5 marks)) */
            .marks {{
                font-size: 9pt;
                color: #7f8c8d;
                float: right; /* Float to the right for alignment */
                margin-left: 10px; /* Space from the main text */
                font-weight: normal; /* Ensure it's not bold */
            }}
            /* Clearfix for marks span */
            .question-with-marks::after {{
                content: "";
                display: table;
                clear: both;
            }}
        </style>
    </head>
    <body>
        <!-- Main title and course code are hardcoded as they are not part of the Markdown raw_text_content variable below -->
        <h1>FOURTH SEMESTER (CBCSS–UG) DEGREE EXAMINATION APRIL 2024</h1>
        <h2 class="course-title">BCA4B05 / BCS4B05 — DATABASE MANAGEMENT SYSTEM AND RDBMS</h2>
        <p class="header-info">Time: Two and HalfHours</p>
        <p class="header-info">Maximum: 80 Marks</p>
        <hr> <!-- Separator below the main header -->
        {html_content}
    </body>
    </html>
    """

    # Generate the PDF file
    try:
        with open(pdf_path, "wb") as pdf_file:
            # pisa.CreatePDF converts the HTML string to a PDF file
            pisa_status = pisa.CreatePDF(
                html_with_css,  # The HTML content with embedded CSS
                dest=pdf_file,  # The file handle to write the PDF output to
                encoding='UTF-8' # Ensure proper character encoding for all text
            )
        if not pisa_status.err:
            print(f"✅ PDF created successfully: {os.path.abspath(pdf_path)}")
        else:
            print(f"❌ Error during PDF creation: {pisa_status.err}")
            # Uncomment the line below for more detailed error logging from xhtml2pdf
            # print(f"Pisa log: {pisa_status.log}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# --- Full exam content from the user's prompt ---
# This content has been carefully structured with Markdown to ensure proper rendering.
raw_text_content = """
## Section A – Short Answer Type Questions
(Each question carries 2 marks. Ceiling: 20 marks)

1. **List the advantages and applications of DBMS.**
    **Advantages:**
    - Data redundancy control
    - Data consistency
    - Improved data sharing and security
    - Data integrity
    - Backup and recovery options

    **Applications:**
    - Banking systems
    - Online shopping platforms
    - Airlines and railway reservation systems
    - University databases
    - Hospital management systems

2. **Define instances and schemas of database.**
    **Instance:** The set of data stored in the database at a particular moment.
    **Schema:** The structure or design of the database, describing tables, fields, relationships, and constraints.

3. **What are the different Relationship Sets? Explain.**
    - **One-to-One:** One entity is related to only one entity of another set.
    - **One-to-Many:** One entity is related to many entities of another set.
    - **Many-to-One:** Many entities are related to one entity of another set.
    - **Many-to-Many:** Many entities are related to many entities of another set.

4. **Define i) Super key ; ii) Candidate key.**
    - **Super Key:** A set of one or more attributes that uniquely identifies a record in a table.
    - **Candidate Key:** A minimal super key; no proper subset can uniquely identify a tuple.

---

5. **What are domain constraints?**
    - **Domain constraints** specify the permissible values for an attribute.
    - For example, an age column may be constrained to accept only **positive integers**.

---

6. **Explain about multi-valued dependencies.**
    - A **multi-valued dependency** occurs when one attribute in a table determines multiple values of another attribute independently of other attributes.
    - It exists in cases requiring **Fourth Normal Form (4NF)**.

---

7. **Define views.**
    - A **view** is a virtual table based on the result of an SQL query.
    - It does **not store data physically** but presents data from one or more tables.

---

8. **Explain deadlock and advisory lock.**
    - **Deadlock**: A situation where two or more transactions are waiting for each other to release locks, causing a cycle of dependencies.
    - **Advisory Lock**: A user-defined lock that is cooperative; it does not enforce locking but relies on **application logic**.

---

9. **What is meant by REVOKE? How is it applied?**
    - **REVOKE** is an SQL command used to take back privileges granted to a user.

    **Example:**
    ```sql
    REVOKE SELECT ON Students FROM user1;
    ```

---

10. **What is the need for triggers?**
    - **Triggers** automate tasks such as **validation**, **logging**, or **enforcing rules** before or after operations like **INSERT**, **UPDATE**, or **DELETE**.

---

11. **How to lock Table-level?**
    - Table-level locking can be done using commands like:

    ```sql
    LOCK TABLE table_name IN [SHARE | EXCLUSIVE] MODE;
    ```

---

12. **How to use IN operator in SQL? Explain.**
    - The **IN operator** is used to match a value against a list.

    **Example:**
    ```sql
    SELECT * FROM Students WHERE Department IN ('CS', 'IT');
    ```

---

## Section B – Short Essay Type Questions
(Each question carries 5 marks. Ceiling: 30 marks)

13. **What do you mean by Database Independence? Explain Three Schema Architecture.**
    Database Independence allows changes in one schema level without affecting others.

    **Three Schema Architecture:**
    - **External Level:** User views
    - **Conceptual Level:** Logical structure
    - **Internal Level:** Physical storage

---

14. **List the different set operations. Explain each with examples.**
    - **UNION**: Combines results of two queries.
    - **INTERSECT**: Returns common rows.
    - **EXCEPT / MINUS**: Returns rows from the first query not found in the second.

    **Example:**
    ```sql
    SELECT name FROM A
    UNION
    SELECT name FROM B;
    ```

---

15. **Explain about different types of integrity constraints.**
    - **Domain Constraint** – Valid values for a column
    - **Entity Integrity** – Primary key can't be NULL
    - **Referential Integrity** – Foreign key must refer to existing primary key
    - **Unique Constraint** – Prevents duplicate values
    - **Not Null Constraint** – Ensures value is not NULL

---

16. **Define Second and Fifth Normal Form.**
    - **2NF (Second Normal Form)**: Removes partial dependencies; table should be in 1NF and all non-key attributes fully dependent on primary key.
    - **5NF (Fifth Normal Form)**: Removes join dependencies; ensures that the relation can’t be further decomposed without losing data.

---

17. **What is Decomposition? What is the purpose of Decomposition in database?**
    **Decomposition** is the process of breaking a relation into smaller relations to eliminate redundancy and anomalies.

    **Purpose:**
    * Improve design
    * Remove redundancy
    * Prevent update, insert, and delete anomalies

---

18. **Which are the modes of lock? Explain. Explain two-phase locking.**
    **Lock Modes:**
    * **Shared (S) Lock**
    * **Exclusive (X) Lock**

    **Two-Phase Locking:**
    * **Growing Phase**: Locks acquired, no release.
    * **Shrinking Phase**: Locks released, no new locks allowed.

    Ensures **serializability**.

---

19. **Write about triggers and its operations in detail.**
    **Triggers** are stored procedures executed automatically in response to events on a table.

    **Operations:**
    * **BEFORE INSERT/UPDATE/DELETE**
    * **AFTER INSERT/UPDATE/DELETE**

    Used for validation, enforcing business rules, audit logs, etc.

    **Example:**
    ```sql
    CREATE TRIGGER before_insert
    BEFORE INSERT ON Students
    FOR EACH ROW
    BEGIN
      -- Logic
    END;
    ```

---

## Section C – Essay Type Questions
(Answer any one question. 10 marks)

---

20. <div class="question-with-marks">**Explain different relational database anomalies in a database.** <span class="marks">(5 marks)</span></div>

    * **Insertion Anomaly**: Difficulty adding data due to absence of other data.
    * **Update Anomaly**: Inconsistent data after updates.
    * **Deletion Anomaly**: Deletion of data leads to unintended loss of additional data.

    **b. List different data models and explain each.** <span class="marks">(5 marks)</span>

    * **Hierarchical Model**: Tree-like structure.
    * **Network Model**: Graph-like structure with multiple parent-child.
    * **Relational Model**: Data in tables with rows and columns.
    * **Object-Oriented Model**: Stores objects as in programming languages.
    * **Entity-Relationship Model**: Graphical representation of entities and relationships.

---

21. <div class="question-with-marks">**What Does Database Concurrency Mean? When a lost update problem occurs, how can the problems be avoided?** <span class="marks">(6 marks)</span></div>
    **Database Concurrency**: Allows multiple users to access the database simultaneously.

    **Lost Update Problem**: Occurs when two transactions read and update the same data, and one update is lost.

    **Solutions:**
    * Two-Phase Locking
    * Timestamp ordering
    * Optimistic Concurrency Control

    **b. What are the disadvantages of file-processing system?** <span class="marks">(4 marks)</span>

    * Data redundancy
    * Lack of data security
    * Difficult in concurrent access
    * Inconsistency and integrity issues
    * No centralized control
"""

if __name__ == '__main__':
    # Define the output PDF file path
    pdf_file_path = "exam_paper_formatted.pdf" # Consistent with user's example
    create_exam_pdf(raw_text_content, pdf_file_path)
