### Base commands for running each tool in this study on an example file

## DeepVirFinder
# Default settings.
```Python dvf.py -i file.fasta -o dvf/ -c 8```

## MetaPhinder
# Default settings.
```python2 MetaPhinder.py -i file.fasta -o file_out -d database/ALL_140821_hr -b metaphinder/bin/```

## MARVEL
# Rename fasta headers to contig1..contig2..contig3.. so MARVEL can handle it
awk '/^>/{print ">contig" ++i; next}{print}' < file.fasta > file_short_headers.fasta
# Split multifasta into individual fasta files
awk '/^>/ {OUT=substr($0,2) ".fa"}; OUT {print >OUT}' file_short_headers.fasta
# Loop MARVEL with default setting over each fasta
for i in contig*; do python3 marvel_bins.py -i ${i} -t 8;done

## PPR_Meta
# Default settings.
./PPR_Meta file.fasta file.pprmeta.txt

## Seeker
# Default settings.
predict-metagenome file.fasta > file.seeker.txt

## VIBRANT
# Default settings.
VIBRANT_run.py -i file.fasta -t 8 -virome -folder vibrant/ -d VIBRANT/databases
-m VIBRANT/files
# Virome decontaination mode on. (Run for phage sample only).
VIBRANT_run.py -i file.fasta -t 8 -virome -folder vibrant_virome/ -d VIBRANT/databases -m VIBRANT/files

## ViralVerify (MetaViralSPAdes)
# Default settings and PFAM 33.0 database.
viralverify.py -f file.fasta -o viralverify/ --hmm PfamA.hmm -t 8

## VirFinder
# Default settings using a script that allows use of multiple cores. Available at https://github.com/jessieren/VirFinder
predResult <- parVF.pred.R("file.fasta ")

## VirSorter
# Default settings.
wrapper_phage_contigs_sorter_iPlant.pl -f file.fasta --db 1 –wdir virsorter-file/ --ncpu 8 --data-dir virsorter-data/
# Virome decontaination mode on. (Run for phage sample only).
wrapper_phage_contigs_sorter_iPlant.pl -f file.fasta --virome --db 1 --wdir virsorter-file/ --ncpu 8 --data-dir virsorter-data/

## VirSorter2
# Default settings with provirus detection off.
virsorter run -w file.out -i file.fasta --provirus-off -j 8
