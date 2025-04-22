# Ersilia Compound Embeddings

Bioactivity-aware chemical embeddings for small molecules. Using transfer learning, we have created a fast network that produces embeddings of 1024 features condensing physicochemical as well as bioactivity information The training of the network has been done using the FS-Mol and ChEMBL datasets, and Grover, Mordred and ECFP descriptors

This model was incorporated on 2023-04-13.

## Information
### Identifiers
- **Ersilia Identifier:** `eos2gw4`
- **Slug:** `ersilia-compound-embedding`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Descriptor`, `Embedding`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1024`
- **Output Consistency:** `Fixed`
- **Interpretation:** Embedding of 1024 features representing a compound

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| dim_0000 | float |  | Feature 0 for the Ersilia Compound Embedding |
| dim_0001 | float |  | Feature 1 for the Ersilia Compound Embedding |
| dim_0002 | float |  | Feature 2 for the Ersilia Compound Embedding |
| dim_0003 | float |  | Feature 3 for the Ersilia Compound Embedding |
| dim_0004 | float |  | Feature 4 for the Ersilia Compound Embedding |
| dim_0005 | float |  | Feature 5 for the Ersilia Compound Embedding |
| dim_0006 | float |  | Feature 6 for the Ersilia Compound Embedding |
| dim_0007 | float |  | Feature 7 for the Ersilia Compound Embedding |
| dim_0008 | float |  | Feature 8 for the Ersilia Compound Embedding |
| dim_0009 | float |  | Feature 9 for the Ersilia Compound Embedding |

_10 of 1024 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos2gw4](https://hub.docker.com/r/ersiliaos/eos2gw4)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2gw4.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2gw4.zip)

### Resource Consumption


### References
- **Source Code**: [https://github.com/ersilia-os/compound-embedding](https://github.com/ersilia-os/compound-embedding)
- **Publication**: [https://www.nature.com/articles/s41467-023-41512-2](https://www.nature.com/articles/s41467-023-41512-2)
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
