# Phage_tools
Specifically designed tools for predicting and identifying phage in metagenomes and metaviromes.

| Software | Description | Released | Reference | Available at: |
| -------- | -------- | --------------- | --------- | ------------- |
| Cenote-Taker2 | Pipeline for annotating contigs with direct terminal repeats and known genes for submission to GenBank.| 2020 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7000223/ | https://github.com/mtisza1/Cenote-Taker2 |
| DeepVirFinder | Predicts viral sequences via a k-mer based deep learning method using convolutional neural networks (CNN). Based on VirFinder. | 2018 | https://link.springer.com/article/10.1007/s40484-019-0187-4 | https://github.com/jessieren/DeepVirFinder |
| FastViromeExplorer | Detects viral sequences and predicts their abundance by pseudoalignment of reads to a database. | 2018 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5768174/ | https://code.vt.edu/saima5/FastViromeExplorer |
| HoloVir | Pipeline designed for taxonomic classification and gene function assignment using genomic and marker databases.| 2016 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4899465/ | https://github.com/plaffy/HoloVir |
| MARVEL | Machine learning tool for predicting phage sequences in metagenomic bins. | 2018 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6090037/ | https://github.com/LaboratorioBioinformatica/MARVEL |
| MetaPhinder | 2016 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5042410/ | https://cge.cbs.dtu.dk/services/MetaPhinder/, https://github.com/vanessajurtz/MetaPhinder |
| metaViralSPAdes | Identifies viral sequences by leveraging metagenomic assembly graphs and analyzing the variations in depth of coverage between viral and bacterial genomes. Made of three modules, it also calculates the completeness of predicted viral sequences. | 2020 | https://www.ncbi.nlm.nih.gov/pubmed/32413137 | https://github.com/ablab/spades/tree/metaviral_publication |
| PhaMers | Identifies phage sequences by a machine learning model based on k-mer frequencies. | 2017 | https://www.biorxiv.org/content/10.1101/169672v1 | https://github.com/jondeaton/PhaMers |
| PHASTER | Web server for identification and annotation of prophages in bacterial genomes and metagenomes | 2016 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4987931/ | https://phaster.ca/ |
| Phigaro | Phage prediction by Hidden Markov Model annotation and smoothing window algorithm mand GC content to predict prophage regions. | 2019 | https://academic.oup.com/bioinformatics/article/doi/10.1093/bioinformatics/btaa250/5822875 | https://pypi.org/project/phigaro/ |
| PPR-Meta | Deep learning CNN approach to identify both phages and plasmids | 2019 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6586199/ | https://github.com/zhenchengfang/PPR-Meta |
| Seeker | Deep learning framework that uses Long Short -Term Memory models (LSTM) which does not depend on sequence motifs. | 2020 | https://www.biorxiv.org/content/10.1101/2020.04.04.025783v2 | https://github.com/gussow/seeker |
| VIBRANT | Deep learning neural network based on protein signatures which also highlights auxiliary metabolic genes and pathways. | 2020 | https://www.biorxiv.org/content/10.1101/855387v1 | https://github.com/AnantharamanLab/VIBRANT |
| VIP | Pipeline for virus identification by nucleotide and remote amino acid comparisons; multiple k-mer de novo assembly; and phylogeny. | 2016 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4824449/ | https://github.com/keylabivdc/VIP |
| ViraMiner | Extension of DeepVirFinder that is trained to identify any virus that may colonise human samples. | 2019 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6738585/ | https://github.com/NeuroCSUT/ViraMiner |
| VirFinder | K-mer based machine learning method for identification of viral contigs. | 2017 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5501583/ | https://github.com/jessieren/VirFinder |
| VirMAP | Creates “super-scaffolds” from de novo assembly and a mapping assembly and taxonomically classifies them with a bits-per-base score. | 2018 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6086868/ | https://github.com/cmmr/VirMAP |
| virMine | Iterative pipeline that relies on the abundance of non-viral sequences in databases to strictly filter out unwanted contigs. Pipeline accepts both reads or assembled contigs. | 2019 | https://www.ncbi.nlm.nih.gov/pubmed/30993039 | https://github.com/thatzopoulos/virMine |
| VirMiner | Web-based pipeline that handles genome assembly, functional annotation using a variety of databases and identification of phage contigs via a random forest algorithm | 2019 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6425642/ | https://github.com/TingtZHENG/VirMiner |
| VirNet | Deep learning neural network using an attentional neural model trained on nucleotide viral fragments. | 2018 | https://ieeexplore.ieee.org/document/8639400 | https://github.com/alyosama/virnet |
| VIROME | Web-based pipeline that classifies viral sequences based on homology to databases and functional annotates them. | 2012 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3558967/ | http://virome.dbi.udel.edu/ |
| ViromeScan | Screens metagenomic reads against complete viral genome database before being filtered and then screen against the same database again. Provides viral hit counts and relative abundance. | 2016 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4774116/ | https://sourceforge.net/projects/viromescan/ |
| VirSorter | Uses referenced-based and reference-free approaches in unison relying on probabilistic similarity models and referenced based protein homology searches to increase novel virus detection. | 2015 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4451026/ | https://github.com/simroux/VirSorter |
| VirusSeeker | Made up of two BLAST-based pipelines – Virome and Discovery. Virome aligns reads to a curated database to identify viral sequences and compute their abundance in the sample. Discovery focuses on contig-based analysis to aid novel virus discovery. | 2017 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5326578/ | https://wupathlabs.wustl.edu/virusseeker/ |

Tools that appear to be no longer available
| Metavir2 | 2014 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4002922/ |
| PHACCS | 2005 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC555943/ |
| Phage Eco-Locator | 2011 | ~https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3194218/ |
| VMGAP | 2011 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3156399/ |
