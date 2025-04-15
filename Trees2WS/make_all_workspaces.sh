#!/bin/bash

# Runs like this: ./make_all_workspaces.sh <path_in_signal_tests> <postEE/preEE>

for m in {15..60..5}
do
    echo "Running trees2ws.py for ${m} GeV mass point for $2!"
    python3 trees2ws.py --inputConfig ws_config_nominal.py --inputTreeFile "/afs/crc.nd.edu/user/s/scastel2/Private/higgs-dna-4-gamma-tanays-copy/scripts/signal_tests/$1/root/Signal_${m}_GeV_$2/output_MA${m}$2_M125_13TeV_amcatnloFXFX_pythia8.root" --productionMode "Signal_${m}_GeV_$2"
done
