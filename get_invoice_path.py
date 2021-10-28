from pathlib import Path
import pandas as pd  # pip install pandas

df = pd.read_excel("invoices.xlsx")
invoice_number = int(input("Enter an invoice number: "))
df_filered = df.query("Invoice_Number == @invoice_number")

# Build path
invoice_filepath = (
    Path.cwd()
    / "ServiceInvoice"
    / str(df_filered["Account_Number"].iloc[0])
    / str(df_filered["Service_Master"].iloc[0])
    / str(df_filered["Invoice_Number"].iloc[0])
)
print(invoice_filepath.with_suffix(".pdf"))
