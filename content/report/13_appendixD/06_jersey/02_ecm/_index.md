---
title: "D.12 Jersey: ECM Yield"
linkTitle: "D.12 ECM Yield"
url: jersey-ecm
weight: 1
sidebar:
  open: false
type: "docs"
---
### D.12.1: Full Period: 1998-2023 {#model_je_ecm_full}

#### **Model Summary**

<div id="tab_67">
<table>
<thead>
<tr>
<th>A. parametric coefficients</th><th>Estimate</th><th>Std. Error</th><th>t-value</th><th>p-value</th>
</tr>
</thead>
<tbody>
<tr><td>(Intercept)</td><td>18.5383</td><td>0.8722</td><td>21.2546</td><td>\(< 0.0001\)</td></tr>
<tr><td>parityprimiparous</td><td>-3.1781</td><td>0.0163</td><td>-195.4078</td><td>\(< 0.0001\)</td></tr>
<tr><td>year1999</td><td>-0.8262</td><td>0.9761</td><td>-0.8464</td><td>0.3973</td></tr>
<tr><td>year2000</td><td>0.0183</td><td>0.9690</td><td>0.0189</td><td>0.9849</td></tr>
<tr><td>year2001</td><td>0.7161</td><td>0.9324</td><td>0.7680</td><td>0.4425</td></tr>
<tr><td>year2002</td><td>1.1984</td><td>0.9342</td><td>1.2828</td><td>0.1996</td></tr>
<tr><td>year2003</td><td>1.6896</td><td>0.9407</td><td>1.7962</td><td>0.0725</td></tr>
<tr><td>year2004</td><td>2.3125</td><td>0.9084</td><td>2.5456</td><td>0.0109</td></tr>
<tr><td>year2005</td><td>2.6139</td><td>0.8927</td><td>2.9282</td><td>0.0034</td></tr>
<tr><td>year2006</td><td>2.7400</td><td>0.8919</td><td>3.0722</td><td>0.0021</td></tr>
<tr><td>year2007</td><td>2.5140</td><td>0.8873</td><td>2.8333</td><td>0.0046</td></tr>
<tr><td>year2008</td><td>2.9241</td><td>0.8861</td><td>3.2999</td><td>0.0010</td></tr>
<tr><td>year2009</td><td>3.0485</td><td>0.8928</td><td>3.4146</td><td>0.0006</td></tr>
<tr><td>year2010</td><td>3.2974</td><td>0.8999</td><td>3.6642</td><td>\(< 0.0005\)</td></tr>
<tr><td>year2011</td><td>3.5419</td><td>0.8911</td><td>3.9750</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2012</td><td>3.8750</td><td>0.8833</td><td>4.3869</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2013</td><td>3.8343</td><td>0.8801</td><td>4.3567</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2014</td><td>4.5334</td><td>0.8848</td><td>5.1234</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2015</td><td>4.6029</td><td>0.8831</td><td>5.2123</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2016</td><td>4.9300</td><td>0.8818</td><td>5.5910</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2017</td><td>5.2786</td><td>0.8865</td><td>5.9547</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2018</td><td>5.6528</td><td>0.8850</td><td>6.3875</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2019</td><td>6.0667</td><td>0.8797</td><td>6.8962</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2020</td><td>6.3867</td><td>0.8849</td><td>7.2176</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2021</td><td>6.4376</td><td>0.8848</td><td>7.2758</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2022</td><td>6.1875</td><td>0.8845</td><td>6.9955</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2023</td><td>6.4372</td><td>0.8763</td><td>7.3457</td><td>\(< 0.0001\)</td></tr>
</tbody>
</table>
<br>
<table>
<thead>
<tr>
<th>B. smooth terms</th><th>edf</th><th>Ref.df</th><th>F-value</th><th>p-value</th>
</tr>
</thead>
<tbody>
<tr><td>s(thi_mean_t0_3d):paritymultiparous</td><td>7.9519</td><td>7.9519</td><td>114.8914</td><td>\(< 0.0001\)</td></tr>
<tr><td>s(thi_mean_t0_3d):parityprimiparous</td><td>5.6644</td><td>5.6644</td><td>146.4984</td><td>\(< 0.0001\)</td></tr>
<tr><td>s(days_in_milk_t):paritymultiparous</td><td>13.5716</td><td>13.5716</td><td>34840.0802</td><td>\(< 0.0001\)</td></tr>
<tr><td>s(days_in_milk_t):parityprimiparous</td><td>13.0755</td><td>13.0755</td><td>3646.1487</td><td>\(< 0.0001\)</td></tr>
</tbody>
</table>
</div>
<figcaption style="text-align: left;">
    Table D.67: Jersey: ECM Yield - 1998-2023 - GAMM model summary without random effect terms.
</figcaption>
<br>

<div id="tab_68">
<table>
<thead>
<tr>
<th>Smooth Term Fixed Effect</th><th>Est.</th><th>SE</th><th>z</th><th>p</th>
</tr>
</thead>
<tbody>
<tr><td>s(thi_mean_t0_3d):multiFx1</td><td>0.622797</td><td>0.111537</td><td>5.58</td><td>\(< 1e-07\)</td></tr>
<tr><td>s(thi_mean_t0_3d):primiFx1</td><td>0.472103</td><td>0.115708</td><td>4.08</td><td>\(< 1e-04\)</td></tr>
<tr><td>s(days_in_milk_):multiFx1</td><td>3.87517</td><td>0.426994</td><td>9.08</td><td>\(< 1e-18\)</td></tr>
<tr><td>s(days_in_milk_):primiFx1</td><td>3.47422</td><td>0.603778</td><td>5.75</td><td>\(< 1e-08\)</td></tr>
</tbody>
</table>
<br>
<table>
<thead>
<tr>
<th>Variance Component</th><th>Estimated \( \sigma \)</th><th></th><th></th><th></th>
</tr>
</thead>
<tbody>
<tr><td>\( \sigma_\alpha\)</td><td>2.63725</td><td></td><td></td><td></td></tr>
<tr><td>\( \sigma_\iota\)</td><td>1.11866</td><td></td><td></td><td></td></tr>
<tr><td>\( \sigma_\phi\)</td><td>3.68271</td><td></td><td></td><td></td></tr>
<tr><td>s(thi_mean_t0_3d):multi</td><td>1.89398</td><td></td><td></td><td></td></tr>
<tr><td>s(days_in_milk_):primi</td><td>8.30084</td><td></td><td></td><td></td></tr>
<tr><td>s(days_in_milk_):multi</td><td>8.67344</td><td></td><td></td><td></td></tr>
<tr><td>s(thi_mean_t0_3d):primi</td><td>1.04356</td><td></td><td></td><td></td></tr>
<tr><td>Residual</td><td>3.85243</td><td></td><td></td><td></td></tr>
</tbody>
</table>
</div>
<figcaption style="text-align: left;">
    Table D.68: Jersey: ECM Yield - 1998-2023 - Mixed Model Summary - Smooth Terms and Random Effects.
</figcaption>
<br>

#### **Model Diagnostics**

{{< figure
  src="/media/figures/models/ecm/full/je_ecm_full/je_ecm_full_diagnostics.png"
  caption="Figure D.67: Jersey: ECM Yield - 1998-2023 - Diagnostic Plot"
  id="fig_je_ecm_full_diagnostics"
  class="figure-no-margin"
>}}

#### **THI Effect and Lactation Curve**

<div id="fig_main" style="display: grid; grid-template-columns: 45% 45%; grid-gap: 0.05%;">
{{< figure
  src="/media/figures/models/ecm/full/je_ecm_full/je_ecm_full_marginal_thi_milk_combined.png"
  caption=""
  id="fig_je_ecm_full_marginal_thi_milk_combined"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/full/je_ecm_full/je_ecm_full_marginal_dim_milk_combined.png"
  caption=""
  id="fig_je_ecm_full_marginal_dim_milk_combined"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/full/je_ecm_full/je_ecm_full_marginal_thi_milk_primi.png"
  caption=""
  id="fig_je_ecm_full_marginal_thi_milk_primi"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/full/je_ecm_full/je_ecm_full_marginal_dim_milk_primi.png"
  caption=""
  id="fig_je_ecm_full_marginal_dim_milk_primi"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/full/je_ecm_full/je_ecm_full_marginal_thi_milk_multi.png"
  caption=""
  id="fig_je_ecm_full_marginal_thi_milk_multi"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/full/je_ecm_full/je_ecm_full_marginal_dim_milk_multi.png"
  caption=""
  id="fig_je_ecm_full_marginal_dim_milk_multi"
  class="figure-no-margin"
>}}
</div>
<figcaption style="text-align: left;">
    Figure D.68: Jersey: ECM Yield - 1998 - 2023 - THI Effect and Lactation Curve
</figcaption>

### D.12.2: Split Period: Until 2010 - After 2010

#### **D.12.2.1: Split Period: 1998 - 2010** {#model_je_ecm_before}

##### **Model Summary**

<div id="tab_69">
<table>
<thead>
<tr>
<th>A. parametric coefficients</th><th>Estimate</th><th>Std. Error</th><th>t-value</th><th>p-value</th>
</tr>
</thead>
<tbody>
<tr><td>(Intercept)</td><td>18.2669</td><td>0.7578</td><td>24.1067</td><td>\(< 0.0001\)</td></tr>
<tr><td>parityprimiparous</td><td>-2.5939</td><td>0.0256</td><td>-101.3950</td><td>\(< 0.0001\)</td></tr>
<tr><td>year1999</td><td>-0.6468</td><td>0.8527</td><td>-0.7586</td><td>0.4481</td></tr>
<tr><td>year2000</td><td>0.2027</td><td>0.8311</td><td>0.2439</td><td>0.8073</td></tr>
<tr><td>year2001</td><td>1.1265</td><td>0.8029</td><td>1.4030</td><td>0.1606</td></tr>
<tr><td>year2002</td><td>1.8105</td><td>0.8042</td><td>2.2513</td><td>0.0244</td></tr>
<tr><td>year2003</td><td>2.3125</td><td>0.7949</td><td>2.9093</td><td>0.0036</td></tr>
<tr><td>year2004</td><td>3.0193</td><td>0.7861</td><td>3.8407</td><td>0.0001</td></tr>
<tr><td>year2005</td><td>3.4202</td><td>0.7798</td><td>4.3858</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2006</td><td>3.6439</td><td>0.7756</td><td>4.6983</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2007</td><td>3.5288</td><td>0.7748</td><td>4.5543</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2008</td><td>4.0872</td><td>0.7753</td><td>5.2718</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2009</td><td>4.4202</td><td>0.7742</td><td>5.7095</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2010</td><td>4.8513</td><td>0.7709</td><td>6.2932</td><td>\(< 0.0001\)</td></tr>
</tbody>
</table>
<br>
<table>
<thead>
<tr>
<th>B. smooth terms</th><th>edf</th><th>Ref.df</th><th>F-value</th><th>p-value</th>
</tr>
</thead>
<tbody>
<tr><td>s(thi_mean_t0_3d):paritymultiparous</td><td>6.7718</td><td>6.7718</td><td>42.2573</td><td>\(< 0.0001\)</td></tr>
<tr><td>s(thi_mean_t0_3d):parityprimiparous</td><td>4.9785</td><td>4.9785</td><td>51.3939</td><td>\(< 0.0001\)</td></tr>
<tr><td>s(days_in_milk_t):paritymultiparous</td><td>12.8146</td><td>12.8146</td><td>11531.2301</td><td>\(< 0.0001\)</td></tr>
<tr><td>s(days_in_milk_t):parityprimiparous</td><td>11.8206</td><td>11.8206</td><td>1844.1937</td><td>\(< 0.0001\)</td></tr>
</tbody>
</table>
</div>
<figcaption style="text-align: left;">
    Table D.69: Jersey: ECM Yield - 1998-2010 - GAMM model summary without random effect terms.
</figcaption>
<br>

<div id="tab_70">
<table>
<thead>
<tr>
<th>Smooth Term Fixed Effect</th><th>Est.</th><th>SE</th><th>z</th><th>p</th>
</tr>
</thead>
<tbody>
<tr><td>s(thi_mean_t0_3d):multiFx1</td><td>0.556587</td><td>0.166586</td><td>3.34</td><td>0.0008</td></tr>
<tr><td>s(thi_mean_t0_3d):primiFx1</td><td>0.399362</td><td>0.171063</td><td>2.33</td><td>0.0196</td></tr>
<tr><td>s(days_in_milk_):multiFx1</td><td>3.05618</td><td>0.696401</td><td>4.39</td><td>\(< 1e-04\)</td></tr>
<tr><td>s(days_in_milk_):primiFx1</td><td>2.77329</td><td>0.788521</td><td>3.52</td><td>0.0004</td></tr>
</tbody>
</table>
<br>
<table>
<thead>
<tr>
<th>Variance Component</th><th>Estimated \( \sigma \)</th><th></th><th></th><th></th>
</tr>
</thead>
<tbody>
<tr><td>\( \sigma_\alpha\)</td><td>2.53036</td><td></td><td></td><td></td></tr>
<tr><td>\( \sigma_\iota\)</td><td>1.11190</td><td></td><td></td><td></td></tr>
<tr><td>\( \sigma_\phi\)</td><td>3.27697</td><td></td><td></td><td></td></tr>
<tr><td>s(thi_mean_t0_3d):multi</td><td>1.72458</td><td></td><td></td><td></td></tr>
<tr><td>s(days_in_milk_):primi</td><td>6.95605</td><td></td><td></td><td></td></tr>
<tr><td>s(days_in_milk_):multi</td><td>8.30984</td><td></td><td></td><td></td></tr>
<tr><td>s(thi_mean_t0_3d):primi</td><td>1.22781</td><td></td><td></td><td></td></tr>
<tr><td>Residual</td><td>3.49403</td><td></td><td></td><td></td></tr>
</tbody>
</table>
</div>
<figcaption style="text-align: left;">
    Table D.70: Jersey: ECM Yield - 1998-2010 - Mixed Model Summary - Smooth Terms and Random Effects.
</figcaption>
<br>

##### **Model Diagnostics**

{{< figure
  src="/media/figures/models/ecm/before2010/je_ecm_before2010/je_ecm_before2010_diagnostics.png"
  caption="Figure D.69: Jersey: ECM Yield - 1998-2010 - Diagnostic Plot"
  id="fig_je_ecm_before2010_diagnostics"
  class="figure-no-margin"
>}}

##### **THI Effect and Lactation Curve**

<div id="fig_main_je_ecm_before2010" style="display: grid; grid-template-columns: 45% 45%; grid-gap: 0.05%;">
{{< figure
  src="/media/figures/models/ecm/before2010/je_ecm_before2010/je_ecm_before2010_marginal_thi_milk_combined.png"
  caption=""
  id="fig_je_ecm_before2010_thi_combined"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/before2010/je_ecm_before2010/je_ecm_before2010_marginal_dim_milk_combined.png"
  caption=""
  id="fig_je_ecm_before2010_dim_combined"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/before2010/je_ecm_before2010/je_ecm_before2010_marginal_thi_milk_primi.png"
  caption=""
  id="fig_je_ecm_before2010_thi_primi"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/before2010/je_ecm_before2010/je_ecm_before2010_marginal_dim_milk_primi.png"
  caption=""
  id="fig_je_ecm_before2010_dim_primi"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/before2010/je_ecm_before2010/je_ecm_before2010_marginal_thi_milk_multi.png"
  caption=""
  id="fig_je_ecm_before2010_thi_multi"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/before2010/je_ecm_before2010/je_ecm_before2010_marginal_dim_milk_multi.png"
  caption=""
  id="fig_je_ecm_before2010_dim_multi"
  class="figure-no-margin"
>}}
</div>
<figcaption style="text-align: left;">
    Figure D.70: Jersey: ECM Yield - 1998 - 2010 - THI Effect and Lactation Curve
</figcaption>

#### **D.12.2.2: Split Period: 2010 - 2023** {#model_je_ecm_after}

##### **Model Summary**

<div id="tab_71">
<table>
<thead>
<tr>
<th>A. parametric coefficients</th><th>Estimate</th><th>Std. Error</th><th>t-value</th><th>p-value</th>
</tr>
</thead>
<tbody>
<tr><td>(Intercept)</td><td>21.9720</td><td>0.1946</td><td>112.8937</td><td>\(< 0.0001\)</td></tr>
<tr><td>parityprimiparous</td><td>-3.2946</td><td>0.0213</td><td>-154.9018</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2012</td><td>0.2540</td><td>0.2259</td><td>1.1242</td><td>0.2609</td></tr>
<tr><td>year2013</td><td>0.2118</td><td>0.2609</td><td>0.8118</td><td>0.4169</td></tr>
<tr><td>year2014</td><td>0.8891</td><td>0.2536</td><td>3.5061</td><td>0.0005</td></tr>
<tr><td>year2015</td><td>0.9643</td><td>0.2528</td><td>3.8138</td><td>0.0001</td></tr>
<tr><td>year2016</td><td>1.2941</td><td>0.2389</td><td>5.4180</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2017</td><td>1.6423</td><td>0.2463</td><td>6.6682</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2018</td><td>2.0143</td><td>0.2347</td><td>8.5841</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2019</td><td>2.4266</td><td>0.2273</td><td>10.6763</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2020</td><td>2.7412</td><td>0.2476</td><td>11.0717</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2021</td><td>2.7795</td><td>0.2468</td><td>11.2643</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2022</td><td>2.5202</td><td>0.2486</td><td>10.1379</td><td>\(< 0.0001\)</td></tr>
<tr><td>year2023</td><td>2.7349</td><td>0.2213</td><td>12.3600</td><td>\(< 0.0001\)</td></tr>
</tbody>
</table>
<br>
<table>
<thead>
<tr>
<th>B. smooth terms</th><th>edf</th><th>Ref.df</th><th>F-value</th><th>p-value</th>
</tr>
</thead>
<tbody>
<tr><td>s(thi_mean_t0_3d):paritymultiparous</td><td>7.8183</td><td>7.8183</td><td>101.7990</td><td>\(< 0.0001\)</td></tr>
<tr><td>s(thi_mean_t0_3d):parityprimiparous</td><td>5.9748</td><td>5.9748</td><td>101.4406</td><td>\(< 0.0001\)</td></tr>
<tr><td>s(days_in_milk_t):paritymultiparous</td><td>13.4448</td><td>13.4448</td><td>25136.3559</td><td>\(< 0.0001\)</td></tr>
<tr><td>s(days_in_milk_t):parityprimiparous</td><td>12.6212</td><td>12.6212</td><td>2246.7077</td><td>\(< 0.0001\)</td></tr>
</tbody>
</table>
</div>
<figcaption style="text-align: left;">
    Table D.71: Jersey: ECM Yield - 2011-2023 - GAMM model summary without random effect terms.
</figcaption>
<br>

<div id="tab_72">
<table>
<thead>
<tr>
<th>Smooth Term Fixed Effect</th><th>Est.</th><th>SE</th><th>z</th><th>p</th>
</tr>
</thead>
<tbody>
<tr><td>s(thi_mean_t0_3d):multiFx1</td><td>-0.690297</td><td>0.130414</td><td>-5.29</td><td>\(< 1e-06\)</td></tr>
<tr><td>s(thi_mean_t0_3d):primiFx1</td><td>-0.514106</td><td>0.148913</td><td>-3.45</td><td>0.0006</td></tr>
<tr><td>s(days_in_milk_):multiFx1</td><td>3.86596</td><td>0.476176</td><td>8.12</td><td>\(< 1e-15\)</td></tr>
<tr><td>s(days_in_milk_):primiFx1</td><td>3.43391</td><td>0.653845</td><td>5.25</td><td>\(< 1e-06\)</td></tr>
</tbody>
</table>
<br>
<table>
<thead>
<tr>
<th>Variance Component</th><th>Estimated \( \sigma \)</th><th></th><th></th><th></th>
</tr>
</thead>
<tbody>
<tr><td>\( \sigma_\alpha\)</td><td>2.60104</td><td></td><td></td><td></td></tr>
<tr><td>\( \sigma_\iota\)</td><td>1.16946</td><td></td><td></td><td></td></tr>
<tr><td>\( \sigma_\phi\)</td><td>3.90069</td><td></td><td></td><td></td></tr>
<tr><td>s(thi_mean_t0_3d):multi</td><td>2.10256</td><td></td><td></td><td></td></tr>
<tr><td>s(days_in_milk_):primi</td><td>7.40217</td><td></td><td></td><td></td></tr>
<tr><td>s(days_in_milk_):multi</td><td>8.58295</td><td></td><td></td><td></td></tr>
<tr><td>s(thi_mean_t0_3d):primi</td><td>1.46353</td><td></td><td></td><td></td></tr>
<tr><td>Residual</td><td>3.91111</td><td></td><td></td><td></td></tr>
</tbody>
</table>
</div>
<figcaption style="text-align: left;">
    Table D.72: Jersey: ECM Yield - 2011-2023 - Mixed Model Summary - Smooth Terms and Random Effects.
</figcaption>
<br>

##### **Model Diagnostics**

{{< figure
  src="/media/figures/models/ecm/after2010/je_ecm_after2010/je_ecm_after2010_diagnostics.png"
  caption="Figure D.71: Jersey: ECM Yield - 2011 - 2023 - Diagnostic Plot"
  id="fig_je_ecm_after2010_diagnostics"
  class="figure-no-margin"
>}}

##### **THI Effect and Lactation Curve**

<div id="fig_main_je_ecm_after2010" style="display: grid; grid-template-columns: 45% 45%; grid-gap: 0.05%;">
{{< figure
  src="/media/figures/models/ecm/after2010/je_ecm_after2010/je_ecm_after2010_marginal_thi_milk_combined.png"
  caption=""
  id="fig_je_ecm_after2010_thi_combined"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/after2010/je_ecm_after2010/je_ecm_after2010_marginal_dim_milk_combined.png"
  caption=""
  id="fig_je_ecm_after2010_dim_combined"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/after2010/je_ecm_after2010/je_ecm_after2010_marginal_thi_milk_primi.png"
  caption=""
  id="fig_je_ecm_after2010_thi_primi"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/after2010/je_ecm_after2010/je_ecm_after2010_marginal_dim_milk_primi.png"
  caption=""
  id="fig_je_ecm_after2010_dim_primi"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/after2010/je_ecm_after2010/je_ecm_after2010_marginal_thi_milk_multi.png"
  caption=""
  id="fig_je_ecm_after2010_thi_multi"
  class="figure-no-margin"
>}}
{{< figure
  src="/media/figures/models/ecm/after2010/je_ecm_after2010/je_ecm_after2010_marginal_dim_milk_multi.png"
  caption=""
  id="fig_je_ecm_after2010_dim_multi"
  class="figure-no-margin"
>}}
</div>
<figcaption style="text-align: left;">
    Figure D.72: Jersey: ECM Yield - 2011 - 2023 - THI Effect and Lactation Curve
</figcaption>
