# Base commands for running each tool in this study on an example file

## DeepVirFinder v1.0
**Default settings.**
```
Python dvf.py -i file.fasta -o dvf_out/ -c 16
```

## Kraken2 v2.1.2
**Run with kraken2-microbial database available at https://lomanlab.github.io/mockcommunity/mc_databases.html**
```
kraken2 --db kraken2-microbial/ file.fasta --output kraken2_out/ --threads 16
```

## MetaPhinder 
**Default settings.**
```
python2 MetaPhinder.py -i file.fasta -o metaphinder_out -d database/ALL_140821_hr -b metaphinder/bin/
```

## PPR_Meta v1.1
**Default settings.**
```
./PPR_Meta file.fasta file.pprmeta.txt
```

## Seeker v1.0.3
**Default settings.**
```
predict-metagenome file.fasta > file.seeker.
```

## VIBRANT v1.2.1
**Default settings.**
```
VIBRANT_run.py -i file.fasta -t 16 -folder vibrant/ -d VIBRANT/databases -m VIBRANT/files
```
**Virome decontaination mode on. (Run for phage sample only).**
```
VIBRANT_run.py -i file.fasta -t 16 -virome -folder vibrant_virome/ -d VIBRANT/databases -m VIBRANT/files
```

## ViralVerify (MetaViralSPAdes) v1.1
**Default settings and PFAM 33.0 database.**
```
viralverify.py -f file.fasta -o viralverify/ --hmm viralVerify_nbc -t 16
viralverify.py -f file.fasta -o viralverify/ --hmm PfamA.hmm -t 16
```

## VirFinder v1.1
**Default settings using a script that allows use of multiple cores. Available at https://github.com/jessieren/VirFinder**
```
predResult <- parVF.pred.R("file.fasta ")
```

## VirSorter v1.06
**Run with diamond and viromedb**
```
wrapper_phage_contigs_sorter_iPlant.pl -f file.fasta --db 2 –wdir virsorter-file/ --ncpu 16 --data-dir virsorter-data/
```
**Virome decontaination mode on. (Run for phage sample only).**
```
wrapper_phage_contigs_sorter_iPlant.pl -f file.fasta --virome --db 2 --wdir virsorter-file/ --ncpu 16 --data-dir virsorter-data/
```

## VirSorter2 v2.2.3
**Default settings with provirus detection off.**
```
virsorter run -w file.out -i file.fasta --provirus-off -j 16
```
