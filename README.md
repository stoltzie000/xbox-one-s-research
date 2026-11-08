# Xbox One S hardware and boot research

Read-only, evidence-based notes on one Xbox One S motherboard identified in supplied photographs as X947889-002. The work focuses on eMMC identification and the limits of boardview/schematic evidence when considering a future native custom-OS boot.

## Findings

- The PCB marking X947889-002 is visible in a project-owner photograph.
- The component-side photo shows U3D1 marked SK hynix H26M41204HPR. The eMMC is located beside the Xbox-branded controller.
- An underside photo shows the R7R2 designator and an apparently populated passive; C7R2 and R7R3 are adjacent. This verifies physical placement, not electrical connectivity.
- The Edmonton GenCAD reference has matching local placement for R7R2/C7R2/R7R3 and associates R7R2 with V_1P8STBY and VREG_1P8STBY_ADJ. Its header does not identify the exact PCB revision, so these net names remain reference-only for X947889-002.
- The Kingston Fab G schematic is for X947889-001. Electrical equivalence with X947889-002 is not established.

## Limits

No firmware/eMMC dump has been acquired. No eMMC reader has been connected, no electrical measurements have been performed, and no native Xbox One S exploit or independently booted Linux system has been demonstrated in this research. Reading eMMC would not itself bypass secure boot.

The public photographs omit the sticker/barcode image and a chassis photo with a computer display in the background. Those originals are preserved only in the private archive.

## Contents

- [Hardware identification and photo evidence](docs/hardware-evidence.md)
- [Electrical topology and verification limits](docs/electrical-status.md)
- [Boot chain and native Linux feasibility](docs/boot-feasibility.md)
- [Generic GenCAD inspection script](tools/inspect_gencad.py)

## Sources

- [Xbox One Research Wiki: eMMC / Flash](https://github.com/xboxoneresearch/wiki/blob/master/docs/hardware/emmc-flash.md)
- [Xbox One Research Wiki: Bootloaders](https://github.com/xboxoneresearch/wiki/blob/master/docs/boot/bootloaders.md)
- [Kingston Fab G RetailOne S schematic](https://consolemods.org/wiki/images/3/32/Kingston_FabG_RetailOne_S.pdf)
- [Internet Archive Edmonton boardview listing](https://archive.org/details/xbox-one-x-cactus-boardview)

## License

Original project-owner photographs and original written notes in this repository are released under CC BY 4.0; see [LICENSE.md](LICENSE.md). The analysis script is MIT-licensed separately; see [tools/LICENSE](tools/LICENSE). Referenced third-party materials are not included and retain their own terms.
