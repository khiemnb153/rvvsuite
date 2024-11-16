from rvvsuite import asm
import os

INPUT_FILE = 'test_0.S'
OUTPUT_DIR = 'output'

# Read assembly file
f = open(INPUT_FILE, 'r', encoding="utf-8")
assembly = f.read()
f.close()

# Split into text section and data section
text_section, data_section = asm.sectionify(assembly)

# Parse
data = asm.parse_data(data_section)
text= asm.parse_text(text_section, data)

# Translate
dmem = asm.translate_data(data)
imem = asm.translate_text(text)

# Output
os.makedirs(OUTPUT_DIR, exist_ok=True)

f = open(f'{OUTPUT_DIR}/dmem.mem', 'w')
f.write(dmem)
f.close

f = open(f'{OUTPUT_DIR}/imem.mem', 'w')
f.write(imem)
f.close