# Input config file for running trees2ws

trees2wsCfg = {

  # Name of RooDirectory storing input tree
  'inputTreeDir':'DiphotonTree',

  # Variables to be added to dataframe: use wildcard * for common strings
  'mainVars':["mass_gggg","weight","dZ","weight_*"], # Var for the nominal RooDataSets
  'dataVars':["mass_gggg","weight"], # Vars to be added for data
  'stxsVar':'',
  'systematicsVars':["mass_gggg","weight"], # Variables to add to sytematic RooDataHists
  'theoryWeightContainers':{},

  # List of systematics: use string YEAR for year-dependent systematics
  'systematics':[],

  # Analysis categories: python list of cats or use 'auto' to extract from input tree
  'cats':'auto'

}
