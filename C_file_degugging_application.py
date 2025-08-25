
# -----------------------------------------------------------
# Streamlit Web interface app for c file debugging/parsing
# Author: Kimberly
# Description:
# This web app reads a C source file (.c) and automatically inserts printf statements at the start ("Entering function") and before
# every return ("Exiting function") in each function.
# Users cannupload a .c file, view the modified version, and download it.
# --

import streamlit as st
import re


def instrument_c_code(code: str) -> str:
    lines = code.splitlines(keepends=True)
    modified_code = []
    inside_function = False
    current_function_name = ""

    function_pattern = re.compile(  r'^\s*(?:[a-zA-Z_][a-zA-Z0-9_*\s]*)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^;]*\)\s*\{' )

    for line in lines:
        match = function_pattern.match(line)
        if match:
            inside_function = True
            current_function_name = match.group(1)
            modified_code.append(line)
            modified_code.append(
                f'    printf("Entering function {current_function_name}\\n");\n'
            )
            continue

        if inside_function and 'return' in line:
            modified_code.append(
                f'    printf("Exiting function {current_function_name}\\n");\n'
            )

        modified_code.append(line)

        if inside_function and '}' in line.strip():
            inside_function = False
            current_function_name = ""

    return "".join(modified_code)




st.title("C Function Degugging Tool")
st.write("Upload a `.c` file to add printf debug statements to at the start and end of functions.")

uploaded_file = st.file_uploader("Choose a C file to add debug statements to", type=["c"])

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")

    modified_code = instrument_c_code(code)

    st.subheader("Modified Code:")
    st.code(modified_code, language="c")

    st.download_button(
        label="Download Modified File",
        data=modified_code,
        file_name=f"modified_{uploaded_file.name}",
        mime="text/x-c"
    )
