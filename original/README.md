License: CC-BY-NC-SA 4.0

The FreeCAD and STL files in this folder were created by relikd.

The files in the STEP folder were extracted - without modification - from the original design.

Original design by [Salim Benbouziyane](https://github.com/sb-ocr/cad-mouse-mk2).


### Improvements

- fix counterbore overhangs with bridging (`Bottom Shell`, `Bottom Lid`).
- replace overhang fillets (z-axis) with 45° chamfers (`Knob`, `Bottom Shell`, `Bottom Lid`, `Button`).


#### Additional parts

- `spring` (any `OG_CN_` will do)
- Optional: use `magnet-holder-v2` (with a `OG_CF_` spring)


### Notes

`base-shell-top` is the only part which needs supports.
For aesthetic reasons, the part should be printed in the final orientation such that it has a smooth top curvature.
You *could* print it upside-down (without support) but that will create a hard edge on the top (visible part).
