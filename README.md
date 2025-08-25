# C File Function Parsing Web App

## Description
This Python Streamlit app parses C source files (.c) and automatically inserts printf statements to log when functions are entered and exited. It provides a simple web interface where users can upload a C file, view the modified version in the browser, and download the updated file.

## The App Outputs
A modified C source file containing additional printf statements for:
- "Entering function" at the start of each function.
- "Exiting function" before each return statement.

## Key Data Points Inserted
Function Name: Extracted from the function signature in the C source file.  
Function Entry Log: Prints "Entering function <function_name>" when the function starts.  
Function Exit Log: Prints "Exiting function <function_name>" before each return statement.   

## Usage
Clone this repository:  
git clone https://github.com/Kimberly-Njamen/CFile_application.git  
cd CFile_application  

Install requirements:  
pip install streamlit  

Run the app locally:  
streamlit run C_file_degugging_application.py  

Open your browser at http://localhost:8501, upload a .c file, preview the modified version, and download the updated file.  

### Online (Optional)
You can use the live deployed version without installing anything:  
🔗 https://cfileapplication-bp3yg7jd3vh3vxmyglm8sb.streamlit.app/  

To deploy your own version, use Streamlit Community Cloud and set C_file_degugging_application.py as the entry point.

## Requirements
Python 3.x  
Streamlit  


