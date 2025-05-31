import streamlit.web.bootstrap
from pathlib import Path

filename = str(Path("ekspresyon.py").resolve())
streamlit.web.bootstrap.run(filename, '', [], None)
