# Ersilia Compound Embeddings

Bioactivity-aware molecular representation built by Ersilia, condensing a compound into 1024 features. A prototypical network of the kind introduced with FS-Mol was trained on Grover and Mordred descriptors to learn an embedding shaped by assay outcomes rather than structure alone, used to embed a reference library of around two million ChEMBL molecules, and then distilled into a small network that maps ECFP fingerprints straight onto those embeddings. That last step makes the descriptor cheap enough for routine screening. Individual dimensions are not interpretable.

This model was incorporated on 2023-04-13.Last packaged on 2026-08-31.

## Information
### Identifiers
- **Ersilia Identifier:** `eos2gw4`
- **Slug:** `ersilia-compound-embedding`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Descriptor`, `Embedding`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1024`
- **Output Consistency:** `Fixed`
- **Interpretation:** 1024 bioactivity-aware features condensing a molecule for use as input to downstream models.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_0000 | float |  | Feature 0 for the Ersilia Compound Embedding |
| feat_0001 | float |  | Feature 1 for the Ersilia Compound Embedding |
| feat_0002 | float |  | Feature 2 for the Ersilia Compound Embedding |
| feat_0003 | float |  | Feature 3 for the Ersilia Compound Embedding |
| feat_0004 | float |  | Feature 4 for the Ersilia Compound Embedding |
| feat_0005 | float |  | Feature 5 for the Ersilia Compound Embedding |
| feat_0006 | float |  | Feature 6 for the Ersilia Compound Embedding |
| feat_0007 | float |  | Feature 7 for the Ersilia Compound Embedding |
| feat_0008 | float |  | Feature 8 for the Ersilia Compound Embedding |
| feat_0009 | float |  | Feature 9 for the Ersilia Compound Embedding |

_10 of 1024 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos2gw4](https://hub.docker.com/r/ersiliaos/eos2gw4)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2gw4.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2gw4.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `620`
- **Image Size (Mb):** `671.55`

**Computational Performance (seconds):**
- 10 inputs: `33.06`
- 100 inputs: `25.28`
- 10000 inputs: `61.02`

### References
- **Source Code**: [https://github.com/ersilia-os/compound-embedding](https://github.com/ersilia-os/compound-embedding)
- **Publication**: [https://doi.org/10.1038/s41467-023-41512-2](https://doi.org/10.1038/s41467-023-41512-2)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2023`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos2gw4
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos2gw4
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
