#!/usr/bin/env python3
import Mesh  # export as STL
import Import  # export as STEP
import os
import shutil

doc = App.openDocument('spring-double.FCStd')
print(f'processing {doc.Name}')


def export(name, size, obj):  # type: ignore[no-untyped-def]
    filename = os.path.join('STL', f'{name}-{size}mm.stl')
    if os.path.exists(filename):
        print(f'skip existing {filename}')
        return
    print(f'export {filename} ...')
    obj.Visibility = True
    doc.VarSet.Height = size
    doc.recompute()
    Mesh.export([obj], filename)
    # Import.export([obj], filename + '.step')


for variant, v_name in [(0, 'original'), (1, 'single-screw')]:
    before = doc.VarSet.Options_Variant
    doc.VarSet.Options_Variant = variant
    print(f'switching model variant: {doc.VarSet.Options_Variant}')
    if before != doc.VarSet.Options_Variant:
        # for whatever reason FC cant change multiple vars at once
        doc.recompute()
    for sz in [2.0, 2.5, 3.0, 3.5, 4.0]:
        export(f'spring-{v_name}', sz, doc.Body.Tip)
        if sz < 4:
            export(f'spacer-{v_name}', 4-sz, doc.getObject('Pocket002'))


print('done.')
shutil.rmtree('__pycache__', ignore_errors=True)
exit(0)
