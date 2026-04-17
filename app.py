# from flask import Flask, render_template, request, send_file
# from fpdf import FPDF
# import io

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/generate', methods=['POST'])
# def generate():
#     emp_id = request.form['emp_id']
#     emp_name = request.form['emp_name']
#     basic = float(request.form['basic'])
#     allowances = float(request.form['allowances'])
#     deductions = float(request.form['deductions'])

#     net = basic + allowances - deductions

#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     pdf.cell(200, 10, txt="PAYSLIP", ln=True)
#     pdf.cell(200, 10, txt=f"ID: {emp_id}", ln=True)
#     pdf.cell(200, 10, txt=f"Name: {emp_name}", ln=True)
#     pdf.cell(200, 10, txt=f"Net Salary: {net}", ln=True)

#     pdf_bytes = pdf.output(dest='S').encode('latin-1')

#     return send_file(
#         io.BytesIO(pdf_bytes),
#         download_name="payslip.pdf",
#         as_attachment=True
#     )

# if __name__ == "__main__":
#     app.run()





from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():

    emp_id = request.form['emp_id']
    emp_name = request.form['emp_name']
    basic = float(request.form['basic'])
    allowances = float(request.form['allowances'])
    deductions = float(request.form['deductions'])

    net = basic + allowances - deductions

    pdf = FPDF()
    pdf.add_page()

    # TITLE
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(190, 10, "PAYSLIP", border=1, ln=True, align='C')
    pdf.ln(5)

    # TABLE STYLE
    pdf.set_font("Arial", size=12)

    pdf.cell(95, 10, "Payslip No.", border=1)
    pdf.cell(95, 10, emp_id, border=1, ln=True)

    pdf.cell(95, 10, "Employee Name", border=1)
    pdf.cell(95, 10, emp_name, border=1, ln=True)

    pdf.cell(95, 10, "Basic Salary", border=1)
    pdf.cell(95, 10, str(basic), border=1, ln=True)

    pdf.cell(95, 10, "Allowances", border=1)
    pdf.cell(95, 10, str(allowances), border=1, ln=True)

    pdf.cell(95, 10, "Deductions", border=1)
    pdf.cell(95, 10, str(deductions), border=1, ln=True)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(95, 10, "NET SALARY", border=1)
    pdf.cell(95, 10, str(net), border=1, ln=True)

    pdf_bytes = pdf.output(dest='S').encode('latin-1')

    return send_file(
        io.BytesIO(pdf_bytes),
        download_name='emp_name'.pdf,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)
