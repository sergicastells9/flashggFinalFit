# Config file: options for signal fitting

_year = '2022postEE'

signalScriptCfg = {

  # Setup
  'inputWSDir':'/afs/crc.nd.edu/user/s/scastel2/Private/higgs-dna-4-gamma-tanays-copy/scripts/signal_tests/outputs_signal_noCorr_PyArrowTest_11Apr2025/root/Signal_15_GeV_postEE/ws_Signal_15_GeV_postEE/',
  'procs':'auto', # if auto: inferred automatically from filenames
  'cats':'NOTAG', # if auto: inferred automatically from (0) workspace
  'ext':'tutorial_%s'%_year,
  'analysis':'tutorial', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'year':'%s'%_year, # Use 'combined' if merging all years: not recommended
  'massPoints':'125',

  #Photon shape systematics
  'scales':'', # separate nuisance per year
  'scalesCorr':'', # correlated across years
  'scalesGlobal':'', # affect all processes equally, correlated across years
  'smears':'', # separate nuisance per year

  # Job submission options
  'batch':'local', # ['condor','SGE','IC','local']
  'queue':'espresso',

}
