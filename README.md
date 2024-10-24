# Ersilia Compound Embeddings

Bioactivity-aware chemical embeddings for small molecules. Using transfer learning, we have created a fast network that produces embeddings of 1024 features condensing physicochemical as well as bioactivity information The training of the network has been done using the FS-Mol and ChEMBL datasets, and Grover, Mordred and ECFP descriptors

## Identifiers

* EOS model ID: `eos2gw4`
* Slug: `eosce`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Embedding of 1024 features representing a compound

## References

* [Publication](https://www.nature.com/articles/s41467-023-41512-2)
* [Source Code](https://github.com/ersilia-os/compound-embedding)
* Ersilia contributor: [GemmaTuron](https://github.com/GemmaTuron)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos2gw4)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2gw4.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos2gw4) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://www.nature.com/articles/s41467-023-41512-2) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!