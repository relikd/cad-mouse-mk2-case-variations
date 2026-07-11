#!/usr/bin/env python3
import Mesh  # export as STL
import Import  # export as STEP
import os
import shutil
from tkinter import filedialog


def askOpen():  # type: () -> tuple[str, ...]
    # ignore result. Required, or else filedialog will open twice
    App.ActiveDocument
    return filedialog.askopenfilenames(
        title='Choose FreeCAD files',
        filetypes=[('FreeCAD files', '*.FCStd'), ('All Files', '*.*')]
    ) or ()


def export(name, variant, flipped):  # type: (str, int, bool) -> None
    filename = os.path.join('STL', f'{name}.stl')
    if os.path.exists(filename):
        print(f'skip existing {filename}')
        return
    print(f'export {filename} ...')
    doc = App.ActiveDocument
    # this works because all files have the same variable names
    doc.VarSet.Options_Variant = variant
    doc.VarSet.Options_MountIsFlipped = flipped
    doc.recompute()
    Mesh.export(doc.RootObjects, filename)
    # Import.export(doc.RootObjects, filename + '.step')


def process(fname):  # type: (str) -> None
    basename = os.path.splitext(os.path.basename(fname))[0]
    print(f'processing {basename}')

    doc = App.openDocument(fname)
    for v_id, v_name in [(0, 'OG'), (1, 'SCS')]:  # original, single-screw
        for f_flag, f_name in [(True, 'CF'), (False, 'CN')]:  # flipped
            export(f'{v_name}_{f_name}_{basename}', v_id, f_flag)
    App.closeDocument(doc.Name)


for path in askOpen():
    process(path)

print('done.')
shutil.rmtree('__pycache__', ignore_errors=True)
exit(0)
