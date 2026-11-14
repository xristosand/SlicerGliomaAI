# Third-Party Notices

GliomaAI incorporates third-party components and pretrained model weights. These components remain the property of their respective copyright holders and are subject to their own licensing terms.

## FreeSurfer SynthStrip — Pretrained Model Weights

**Component:** SynthStrip pretrained model weights, version 1 (`synthstrip.1.pt`)

**Purpose:** Brain extraction (skull stripping) during MRI preprocessing.

**Copyright holder:** The General Hospital Corporation (Massachusetts General Hospital).

**License:** MIT License, selected from the MIT / Creative Commons Attribution 4.0 International (CC BY 4.0) dual-licensing options offered by the SynthStrip developers for pretrained model weights.

**Original source:**
https://surfer.nmr.mgh.harvard.edu/docs/synthstrip/

**Source repository:**
https://github.com/freesurfer/freesurfer/tree/dev/mri_synthstrip

**Bundled file:**
`GliomaClassifier/Resources/Models/synthstrip.1.pt`

**SHA-256:**
`37417f802196186441aae3e7f385d94f8a98c64a88acaeaa2723af995c653e33`

The model weights are redistributed without modification. The applicable license text is provided in `licenses/SynthStrip-MIT.txt`.

### Reference

Hoopes, A., Mora, J. S., Dalca, A. V., Fischl, B., and Hoffmann, M. (2022). SynthStrip: Skull-Stripping for Any Brain Image. *NeuroImage*, 260, 119474.

https://doi.org/10.1016/j.neuroimage.2022.119474

## Licensing Scope

The MIT license selected above applies to the bundled SynthStrip pretrained model weights. It does not replace or supersede the licensing terms applicable to other FreeSurfer software components or independently installed third-party Python packages.

The GliomaAI source code is distributed under the license specified in the repository's root `LICENSE.txt`.