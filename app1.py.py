import streamlit as st
import re

# ------------------------------
# Function to insert printfs
# ------------------------------
def add_print_statements(code: str) -> str:
    """
    Naive parser: Adds a printf at the start of each function.
    Adjust regex for more robustness if needed.
    """
    pattern = r"(\w[\w\s\*]+)\s+(\w+)\s*\(([^)]*)\)\s*\{"
    
    def replacer(match):
        return f"{match.group(0)}\n    printf(\"[DEBUG] Entering {match.group(2)}()\\n\");"

    return re.sub(pattern, replacer, code)

# ------------------------------
# Streamlit Interface
# ------------------------------
st.title("C Function Instrumentation Tool")
st.write("Upload a `.c` file, add debug print statements, and download the modified file.")

# Upload file
uploaded_file = st.file_uploader("Choose a C file", type=["c"])

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")

    # Process file
    modified_code = add_print_statements(code)

    # Display modified code
    st.subheader("Modified Code:")
    st.code(modified_code, language="c")

    # Download button
    st.download_button(
        label="Download Modified File",
        data=modified_code,
        file_name=f"modified_{uploaded_file.name}",
        mime="text/x-c"
    )
