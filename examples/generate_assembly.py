from rvvsuite import rtg
from rvvsuite import asm
import os

CONFIG_FILE = 'configs.json'
OUTPUT_DIR = 'output'

configs = rtg.parse_config_file(CONFIG_FILE)

num_of_test = configs['num_of_tests']
test_prefix = configs['test_prefix']

for i in range(num_of_test):
    data_section, init_text_seq, main_text_seq = rtg.generator_test(configs)
    assembly = rtg.display(data_section, init_text_seq, main_text_seq)

    os.makedirs(OUTPUT_DIR,exist_ok=True)

    f = open(f'{OUTPUT_DIR}/{test_prefix}{i}.S', 'w')
    f.write(assembly)
    f.close()




