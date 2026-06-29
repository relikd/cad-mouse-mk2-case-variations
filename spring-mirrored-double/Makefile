
UNAME := $(shell uname)

ifeq ($(UNAME), Darwin)
	FC := $(shell mdfind "kMDItemCFBundleIdentifier=='org.freecad.FreeCAD'")/Contents/MacOS/FreeCAD
else
	# TODO: find executable on Win and Linux
	FC := freecad
endif

.PHONY: export
export:
	$(FC) -c export.py
