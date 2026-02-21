import markdown
from xhtml2pdf import pisa

def create_pdf(markdown_content, pdf_path):
    # Convert Markdown to HTML
    # Using an HTML entity for the overline in IO/M
    html_content = markdown.markdown(markdown_content, extensions=['tables'])

    # Basic CSS for better PDF formatting
    html_with_css = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: DejaVu Sans, sans-serif; line-height: 1.6; font-size: 10pt; }}
            h1, h2, h3 {{ font-family: DejaVu Sans, sans-serif; }}
            h1 {{ font-size: 18pt; text-align: center; margin-bottom: 20pt; }}
            h2 {{ font-size: 14pt; margin-top: 20pt; margin-bottom: 10pt; border-bottom: 1px solid #ccc; padding-bottom: 5px;}}
            h3 {{ font-size: 12pt; margin-top: 15pt; margin-bottom: 5pt;}}
            ul, ol {{ margin-bottom: 10pt; }}
            li {{ margin-bottom: 3pt; }}
            code {{ font-family: "Courier New", Courier, monospace; background-color: #f0f0f0; padding: 2px 4px; border-radius: 3px; }}
            hr {{ border: 0; height: 1px; background: #333; margin: 20pt 0; }}
            .instructions {{ font-style: italic; margin-bottom: 15pt; }}
            .question-meta {{ font-size: 9pt; color: #555; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Create PDF
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(
            html_with_css,  # the HTML to convert
            dest=pdf_file,  # file handle to recieve result
            encoding='UTF-8'
        )

    if not pisa_status.err:
        print(f"PDF successfully created at {pdf_path}")
    else:
        print(f"Error creating PDF: {pisa_status.err}")

# The Markdown content of the question paper
# Note: Replaced $\overline{M}$ with M&#773; for better HTML entity handling in PDF
markdown_text = """
# Consolidated Sample Question Paper
## **A14-MICROPROCESSORS ARCHITECTURE AND PROGRAMMING**
**(Based on 2022, 2023, 2024 Degree Examinations)**

<div class="instructions">This paper consolidates unique questions from the April 2022, April 2023, and April 2024 examinations. The year(s) in which each question appeared and the total number of times it appeared are indicated in brackets.</div>

---

## Section A
**Short Answer Questions**

1.  What is a Microprocessor? <span class="question-meta">(2024 - 1 time)</span>
2.  What do you mean by multiplexing of data bus? <span class="question-meta">(2024 - 1 time)</span>
3.  What is the size of a register in 8085? Name the valid register pairs in 8085. <span class="question-meta">(2024 - 1 time)</span>
4.  Differentiate between data bus and address bus. <span class="question-meta">(2024 - 1 time)</span>
5.  What do you mean by maskable interrupts? <span class="question-meta">(2024 - 1 time)</span>
6.  What are the software interrupts in 8085? <span class="question-meta">(2024 - 1 time)</span>
7.  What is stack pointer? <span class="question-meta">(2024 - 1 time)</span>
8.  What is the function of POP instruction? <span class="question-meta">(2024 - 1 time)</span>
9.  What is the function/use of ALE signal in 8085? <span class="question-meta">(2024, 2022 - 2 times)</span>
10. Which logical instruction can be used for clearing the accumulator? <span class="question-meta">(2024 - 1 time)</span>
11. Give two differences between 8086 and 8088. <span class="question-meta">(2024 - 1 time)</span>
12. Differentiate between CMP and SUB instruction. <span class="question-meta">(2024 - 1 time)</span>
13. What do you mean by mode 0 operation of 8255? <span class="question-meta">(2024 - 1 time)</span>
14. What is the function of overflow flag in 8086? <span class="question-meta">(2024 - 1 time)</span>
15. What do you mean by maximum mode operation of 8086? <span class="question-meta">(2024 - 1 time)</span>
16. Name the 16 bit registers available in 8085. <span class="question-meta">(2022 - 1 time)</span>
17. What is the function of IO/M&#773; signal in the 8085? <span class="question-meta">(2022 - 1 time)</span>
18. Mention the purpose of SID and SOD lines. <span class="question-meta">(2022 - 1 time)</span>
19. What do you mean by memory mapping? <span class="question-meta">(2022 - 1 time)</span>
20. Differentiate between Instruction cycle, Machine cycle and T-states. <span class="question-meta">(2022 - 1 time)</span>
21. Explain the instruction DAA. <span class="question-meta">(2022 - 1 time)</span>
22. How many address lines are there in a 4096 x 8 EPROM CHIP? <span class="question-meta">(2022 - 1 time)</span>
23. What do you mean by priority in an interrupt? <span class="question-meta">(2022 - 1 time)</span>
24. What is the importance of IN and OUT instructions? <span class="question-meta">(2022 - 1 time)</span>
25. Explain the difference between a JMP instruction and CALL instruction. <span class="question-meta">(2022 - 1 time)</span>
26. What is PSW in 8085? <span class="question-meta">(2022 - 1 time)</span>
27. What is the purpose of restart instructions in 8085? <span class="question-meta">(2022 - 1 time)</span>
28. What are the modes of operations of 8254? <span class="question-meta">(2022 - 1 time)</span>
29. What are the different types of instructions in 8086? <span class="question-meta">(2022 - 1 time)</span>
30. List few applications of microprocessor-based system. <span class="question-meta">(2023 - 1 time)</span>
31. What is an Assembler? <span class="question-meta">(2023 - 1 time)</span>
32. What is the purpose of HOLD pin in 8085? <span class="question-meta">(2023 - 1 time)</span>
33. What is the clock frequency of 8085? <span class="question-meta">(2023 - 1 time)</span>
34. How is address de-multiplexing done in 8085? <span class="question-meta">(2023 - 1 time)</span>
35. What are the program control instructions available in 8085? <span class="question-meta">(2023 - 1 time)</span>
36. What is the primary difference between memory read and instruction fetch operations in 8085? <span class="question-meta">(2023 - 1 time)</span>
37. Predict the accumulator content while executing the following instructions: MOV A, M; XRA A. <span class="question-meta">(2023 - 1 time)</span>
38. Explain the various machine cycles associated with the execution of the instruction: OUT 80H. <span class="question-meta">(2023 - 1 time)</span>
39. What is a delay program and what are its uses? <span class="question-meta">(2023 - 1 time)</span>
40. List the four instructions which control the interrupt structure of the 8085 microprocessor. <span class="question-meta">(2023 - 1 time)</span>
41. What are the applications of 8255A PPI? <span class="question-meta">(2023 - 1 time)</span>
42. What are the modes of operation of 8237 IC? <span class="question-meta">(2023 - 1 time)</span>
43. Define Pipelining. <span class="question-meta">(2023 - 1 time)</span>
44. What is NMI? <span class="question-meta">(2023 - 1 time)</span>

---

## Section B
**Medium Answer Questions**

1.  What are different microprocessor initiated operations of 8085? <span class="question-meta">(2024 - 1 time)</span>
2.  Describe the instruction format of 8085 based on the number of bytes used. <span class="question-meta">(2024 - 1 time)</span>
3.  Draw the timing diagram of the instruction MVI B, data. <span class="question-meta">(2024 - 1 time)</span>
4.  Write an 8085 assembly language program for block data transfer (i.e., transferring a set of data from one location to another location). <span class="question-meta">(2024 - 1 time)</span>
5.  What are the functions of RIM and SIM instruction? <span class="question-meta">(2024 - 1 time)</span>
6.  Explain how data transfer is performed using 8257 DMA controller. <span class="question-meta">(2024 - 1 time)</span>
7.  Explain the BSR mode of 8255. <span class="question-meta">(2024 - 1 time)</span>
8.  Explain the function of segment registers in 8086. <span class="question-meta">(2024 - 1 time)</span>
9.  Explain how the memory is classified in computer architecture. <span class="question-meta">(2022 - 1 time)</span>
10. What are flags? Explain how flags are accessed in 8085. <span class="question-meta">(2022 - 1 time)</span>
11. Discuss the various machine cycles involved in 8085. <span class="question-meta">(2022 - 1 time)</span>
12. Draw the timing diagram associated with the instruction: MOV M,A (e.g., at an address A000h). <span class="question-meta">(2022 - 1 time)</span>
13. Write an 8085 assembly program to check the number of 1's in a byte taken into the accumulator from a memory location (e.g., 4000H). <span class="question-meta">(2022 - 1 time)</span>
14. What is stack? Explain how stack is used in 8085. <span class="question-meta">(2022 - 1 time)</span>
15. Draw the internal block diagram showing the various units in 8237 chip. <span class="question-meta">(2022 - 1 time)</span>
16. What are the different busses in 8086? Explain in brief. <span class="question-meta">(2022 - 1 time)</span>
17. Draw and explain the pin out of 8085 microprocessor. <span class="question-meta">(2023 - 1 time)</span>
18. Explain the role of accumulator in 8085. <span class="question-meta">(2023 - 1 time)</span>
19. Discuss the logical instructions in 8085. <span class="question-meta">(2023 - 1 time)</span>
20. Write an 8085 ALP to add the numbers stored in memory locations with a starting address (e.g., 5500H). <span class="question-meta">(2023 - 1 time)</span>
21. Draw and explain the timing diagram for executing the instruction: STA address (e.g., STA 526AH, given opcode 41FFH). <span class="question-meta">(2023 - 1 time)</span>
22. Explain the branching instructions in 8085. <span class="question-meta">(2023 - 1 time)</span>
23. Explain the various hardware interrupts in 8085. How are these interrupts serviced during a program? <span class="question-meta">(2023 - 1 time)</span>

---

## Section C
**Long Answer/Essay Questions**

1.  Explain the classification of instructions in 8085. <span class="question-meta">(2024 - 1 time)</span>
2.  Describe in detail the interrupts of 8085 (including types, priority, and servicing). <span class="question-meta">(2024 - 1 time)</span>
3.  With block diagram, explain the internal architecture and working of the Programmable Interval Timer, 8254. <span class="question-meta">(2024, 2023 - 2 times)</span>
4.  With block diagram, explain the internal architecture of 8086. <span class="question-meta">(2024 - 1 time)</span>
5.  Explain the bus organisation in 8085 microprocessor. Describe the flag registers associated with 8085. <span class="question-meta">(2022 - 1 time)</span>
6.  Discuss the various mathematical and logical instructions used in 8085. <span class="question-meta">(2022 - 1 time)</span>
7.  Explain the modes of operation in 8255A PPI. <span class="question-meta">(2022 (Sec C), 2023 (Sec B) - 2 times)</span>
8.  Explain the addressing modes in 8086. <span class="question-meta">(2022 - 1 time)</span>
9.  Discuss the register organisation in 8085. <span class="question-meta">(2023 - 1 time)</span>
10. Explain the various addressing modes in 8085 with proper examples. <span class="question-meta">(2023 - 1 time)</span>
11. Explain the internal organisation of registers in 8086. <span class="question-meta">(2023 - 1 time)</span>

---
"""

if __name__ == '__main__':
    # Define the output PDF file path
    pdf_file_path = "consolidated_question_paper.pdf"
    create_pdf(markdown_text, pdf_file_path)