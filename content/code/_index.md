---
title: Code
share: false
type: landing
sections:
  - block: markdown
    id: preprocessing
    content:
      title: Preprocessing
      text: |
        <style> .hbb-section {padding-top:1rem !important;padding-bottom:2rem !important;} .mb-6 {margin-bottom: 0 !important;} </style>
        <div style="text-align: center;"><a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="https://github.com/aschneuw/heatstress-resources/tree/main/notebooks/preprocessing" target="_blank"> Notebooks </a>&nbsp;<a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="/heatstress/materials#sec_data" target="_blank"> Report </a></div>
        Notebooks with data preprocessing steps. This includes processing, filtering and matching steps for the hydroclimatic, geospatial and agronomic data. 
  - block: markdown
    id: mixedmodels-jl
    content:
      title: MixedModels.jl with GAMM Support
      text:  |
        <div style="text-align: center;"><a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="https://github.com/aschneuw/MixedModels.jl" target="_blank"> Code </a> &nbsp;<a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="/heatstress/materials/#sec_julia_modifications" target="_blank"> Report </a></div>
        This repository contains a tweaked MixedModels.jl accommodating random effect matrices to support GAMMs defined as mixed models. The key add-on is multiplication support for random effect matrices with arbitrary real numbers.
  - block: markdown
    id: gammJ
    content:
      title: gammJ
      text: |
        <div style="text-align: center;"><a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="https://github.com/aschneuw/heatstress-resources/tree/main/gammJ" target="_blank"> Notebook </a> &nbsp;<a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="/heatstress/materials/#sec_gammJ" target="_blank"> Report </a></div>
        Contains the files required to run a full gammJ procedure. The notebook <code>gammJ_v9_example.ipynb</code> fits a GAMM by leveraging model generation component by gamm4, and then executing them with <code>trainGAM.jl</code> (which leverages the modified MixedModels.jl) and <code>postprocessGAM.jl</code> to compute the psudo data covariance matrix.
  - block: markdown
    id: gamm4
    content:
      title: gamm4 Performance Test
      text: |
        <div style="text-align: center;"><a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="https://github.com/aschneuw/heatstress-resources/tree/main/gamm4/gamm4_jersey_performance.ipynb" target="_blank"> Code </a> &nbsp;<a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="/heatstress/materials/#sec_gamm4" target="_blank"> Report </a></div>
        Highlights the gamm4 performance bottleneck by fitting multiple models with an increasing amount of random intercept factor levels.
  - block: markdown
    id: gamm4b
    content:
      title: gamm4b
      text: |
        <div style="text-align: center;"><a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="https://github.com/aschneuw/heatstress-resources/tree/main/gamm4b/gamm4b_example.ipynb" target="_blank"> Code </a> &nbsp;<a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="/heatstress/materials/#sec_gamm4b" target="_blank"> Report </a></div>
        Points to the performance enhanced gamm4 code in notebook format. This code has only been tested for our use case and does not necessarily work for other model confgurations such as different linking functions.
  - block: markdown
    id: model-notebooks
    content:
      title: Model Notebooks
      text: |
        <div style="text-align: center;"><a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="https://github.com/aschneuw/heatstress-resources/tree/main/notebooks" target="_blank"> Code </a> &nbsp;<a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="/heatstress/results/#sec_model_overview" target="_blank"> Report </a></div>
        Points to all gammJ execution notebooks for the individual models per milk performance variable (Milk Yield as well as ECM) and breed.
  - block: markdown
    id: fe-notebooks
    content:
      title: Pooled OLS Notebooks
      text: |
        <div style="text-align: center;"><a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="https://github.com/aschneuw/heatstress-resources/tree/main/notebooks/models/fixed_effect_econometrics" target="_blank"> Notebooks </a> </div>
        Points to experimental notebooks where a piecewise linear approach from econometrics with pooled regressions is used. These results are biased because of the unbalanced nature of our data.
  - block: markdown
    id: report
    content:
      title: Report
      text: |
        <div style="text-align: center;"><a class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600" href="https://github.com/aschneuw/heatstress-resources/tree/main/thesis" target="_blank"> Latex </a> </div>
        Points to the LaTex source of the report.
---

<style>
    .hbb-section {
        padding-top: 0 !important;
        padding-bottom: 2rem !important;
    }
</style>