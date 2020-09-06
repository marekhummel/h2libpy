import os
import sys
import time

import examples.example_amatrix_bem3d as exa
import examples.example_h2matrix_bem3d as exht
import examples.example_hmatrix_bem3d as exh


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


funcs = {'amatrix': exa.main, 'hmatrix': exh.main, 'h2matrix': exht.main}
reps = 5

with open('benchmark.txt', 'w') as f:
    for func in funcs.items():
        for split in [8, 16, 32]:
            for qreg in [2, 4]:
                if split == 32 and qreg == 4: break
                start = time.time()
                with HiddenPrints():
                    for _ in range(reps):
                        norm = func[1](qreg, split)
                t = (time.time() - start) / reps
                f.write(f'{func[0].ljust(8)}: {split:-2d},{qreg} = {t:9.5f}s ({norm})\n')
                print(f'{func[0]}: {split},{qreg}')
        f.write('\n')
