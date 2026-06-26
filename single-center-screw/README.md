Author: relikd

Based on: `original` + `print-improvements`

---

Re-designed to assemble all parts with a single center screw (M5) while maximizing bottom volume for weights.


### Changes

- All heights are calculated from sensors board + MCU dimensions.
  This assures a minimal possible height and allows customizations for custom PCB designs.
- The `Bottom` is fixed with self-tapping screws (no heat-set inserts needed, just regular 3mm).
- The `Top` can be fixed with either heat-set inserts (M3) or self-tapping screws (3mm) – choose the STL accordingly.
- The model files `Top`, `Button`, and `Diffuser` have variant options (screw type and PCB variants (see below).
  All models have `VarSet` variables.


### PCB variants

- Original (PCB design by [sb-ocr](https://github.com/sb-ocr/cad-mouse-mk2), the original release)
- Nikki (PCB design by [sheffieldnikki](https://github.com/sb-ocr/cad-mouse-mk2/issues/24), community variant, mounting the MCU directly onto the sensors board)


### Re-used parts

- from `print-improvements`:
	- `knob`
- from `original`:
	- `magnet-holder`


### Print settings

- The model is tweaked for a minimum layer height of 0.2mm.
  Try not to go above or else you will have overhangs in screw holes etc. (or: adjust the printer variables in the model files)
- Only `Top` needs supports.
  All other parts have bridges for overhangs and should print without supports.


### Bill of materials

- 6x Magnets 6mm x 3mm (same as original)
- 1x M5 x 40, Hexagon Socket Head Cap Screw
- 1x M5 nut
- 3x M3 x 12 (`Knob`)
- 3x M3 Heat-Set Inserts 4mm (`Knob`)
- 4x 3mm Self-Tapping Screw, 5-12mm long, Sink Head or Flat Head (head type doesnt really matter but shouldn't stick out too much) (connects `Bottom` and `Separator`)
- 4x 3mm Self-Tapping Screw, 4-7mm long, Flat Head (connects PCB to `Top`)

__Alternatively__, replace the 4 `Top` screws with:
- 4x M3 x 4 (OR: M3 x 6), Hexagon Socket Head Cap Screw
- 4x M3 Heat-Set Inserts 4mm


### Assembly

The mouse consists of three main parts: bottom, top, and knob.

1. Fill the `Bottom` with weights (e.g., steel balls), fill it up with wax and then close it off with the `Separator`.
2. Place the `Diffuser` in the `Top` shell (the diffuser cut-out should point in the same direction as the USB port).
   Place the PCB onto the diffuser (pinout in the same direction).
   Then, screw both together and insert the MCU.
3. Combine the `Stem`, `Spring`, and `Nut-Cage`.
   Place the M5 nut into the cage.
   Combine this stack with the `Magnet-Holder` and fix both into the `Knob`.
4. Finally, stack all three components loosely together and insert the M5 screw carefully.
   Don't push too hard, or the nut will fall out (and you'll have to disassamble the knob again).

The single M5 screw holds all parts together.
Most parts have a tight fit.
Especially the spring and stem should fit as perfect as possible (reduces rotational wobble).
