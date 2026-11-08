# Electrical topology: reference data and unknowns

## Edmonton GenCAD records

The public archive listing identifies an Edmonton boardview. This project inspected an ASCII GenCAD 1.4 artifact locally but does not redistribute the CAD file.

The artifact contains the following reference-design net assignments:

| Refdes | Reference connection | Evidence class |
|---|---|---|
| R7R2 | V_1P8STBY to VREG_1P8STBY_ADJ | GenCAD-only |
| R4E5 | MMC_CLK to MMC_CLK_R | GenCAD-only |
| R4E7 | MMC_CMD to MMC_CMD_R | GenCAD-only |
| R4E23 | MMC_DATA<0> to MMC_DATA_R<0> (DAT0) | GenCAD-only |
| R4E1 | MMC_RST_N to MMC_RST_N_R | GenCAD-only |

The component records place R7R2 on the board bottom with a 0402 footprint. The physical photograph confirms the R7R2 silkscreen and apparent component population. It cannot determine which photo-visible terminal is pin 1, nor prove either terminal's net.

## Schematic limit

The Kingston Fab G schematic identifies U3D6 as an AP2127KADJ adjustable standby regulator and includes a 1.8 V standby adjustment circuit. It is a reference for X947889-001. Compatibility with X947889-002 has not been established. Neither the boardview nor the schematic measures rail voltage, component value, regulator sequencing, controller isolation, bus contention, or back-powering on the photographed board.

## Acquisition status

No read-only eMMC acquisition method has been electrically validated for this X947889-002 board. No reader is connected and no electrical measurement has been performed. A physical R7R2 placement match is useful evidence for local boardview correspondence, but it is not an eMMC interface authorization.

A future board-specific investigation must establish signal-side separation, voltage domains, and safe powering/isolation before an external reader is considered. This repository intentionally omits wiring or probing instructions unsupported by revision-matched evidence.

## Sources

- [Edmonton boardview archive listing](https://archive.org/details/xbox-one-x-cactus-boardview) — listing/source reference only; the boardview bytes are not redistributed here.
- [Kingston Fab G RetailOne S schematic](https://consolemods.org/wiki/images/3/32/Kingston_FabG_RetailOne_S.pdf) — X947889-001 reference; no -002 equivalence claim.
