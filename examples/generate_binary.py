from rvvsuite.rtg import parse_config_file
from rvvsuite import rtg
from rvvsuite import asm
import os

CONFIG_FILE = 'configs.json'
OUTPUT_DIR = 'output'

configs = parse_config_file(CONFIG_FILE)

num_of_test = configs['num_of_tests']
test_prefix = configs['test_prefix']

for i in range(num_of_test):
    data_section, init_text_seq, main_text_seq = rtg.generator_test(configs, use_addr=True)

    dmem = asm.translate_data(data_section)
    imem = asm.translate_text(init_text_seq + main_text_seq)

    os.makedirs(f'{OUTPUT_DIR}/{test_prefix}{i}',exist_ok=True)

    f = open(f'{OUTPUT_DIR}/{test_prefix}{i}/imem.mem', 'w')
    f.write(imem)
    f.close()

    f = open(f'{OUTPUT_DIR}/{test_prefix}{i}/dmem.mem', 'w')
    f.write(dmem)
    f.close()




