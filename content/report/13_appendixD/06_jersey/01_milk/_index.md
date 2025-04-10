---
title: "D.11 Jersey: Milk Yield"
linkTitle: "D.11 Milk Yield"
url: jersey-milk
weight: 1
sidebar:
  open: false
type: "docs"
---
### D.11.1: Full Period: 1998-2023 {#model_je_milk_full}

#### **Model Summary**

<div>
<table>
<thead>
<tr>
<th>A. parametric coefficients</th><th>Estimate</th><th>Std. Error</th><th>t-value</th><th>p-value</th>
</tr>
</thead>
<tbody>
<tr>
<td>(Intercept)</td><td>13.7621</td><td>0.7123</td><td>19.3200</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>parityprimiparous</td><td>-2.0196</td><td>0.0125</td><td>-162.2099</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year1999</td><td>-0.5788</td><td>0.7821</td><td>-0.7401</td><td>0.4592</td>
</tr>
<tr>
<td>year2000</td><td>0.1706</td><td>0.7908</td><td>0.2158</td><td>0.8292</td>
</tr>
<tr>
<td>year2001</td><td>0.6872</td><td>0.7611</td><td>0.9029</td><td>0.3666</td>
</tr>
<tr>
<td>year2002</td><td>1.1345</td><td>0.7621</td><td>1.4886</td><td>0.1366</td>
</tr>
<tr>
<td>year2003</td><td>1.6274</td><td>0.7688</td><td>2.1169</td><td>0.0343</td>
</tr>
<tr>
<td>year2004</td><td>2.1381</td><td>0.7407</td><td>2.8868</td><td>0.0039</td>
</tr>
<tr>
<td>year2005</td><td>2.3294</td><td>0.7283</td><td>3.1986</td><td>0.0014</td>
</tr>
<tr>
<td>year2006</td><td>2.6162</td><td>0.7276</td><td>3.5957</td><td>0.0003</td>
</tr>
<tr>
<td>year2007</td><td>2.4384</td><td>0.7239</td><td>3.3683</td><td>0.0008</td>
</tr>
<tr>
<td>year2008</td><td>2.6780</td><td>0.7231</td><td>3.7037</td><td>0.0002</td>
</tr>
<tr>
<td>year2009</td><td>2.9302</td><td>0.7281</td><td>4.0244</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2010</td><td>3.1502</td><td>0.7338</td><td>4.2930</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2011</td><td>3.3587</td><td>0.7275</td><td>4.6169</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2012</td><td>3.6206</td><td>0.7210</td><td>5.0218</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2013</td><td>3.6943</td><td>0.7185</td><td>5.1417</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2014</td><td>4.3000</td><td>0.7222</td><td>5.9540</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2015</td><td>4.4102</td><td>0.7209</td><td>6.1173</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2016</td><td>4.6309</td><td>0.7199</td><td>6.4324</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2017</td><td>5.0141</td><td>0.7237</td><td>6.9289</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2018</td><td>5.3353</td><td>0.7225</td><td>7.3848</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2019</td><td>5.6806</td><td>0.7183</td><td>7.9088</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2020</td><td>5.9019</td><td>0.7223</td><td>8.1711</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2021</td><td>5.9578</td><td>0.7225</td><td>8.2465</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2022</td><td>5.9243</td><td>0.7222</td><td>8.2033</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2023</td><td>6.0294</td><td>0.7156</td><td>8.4255</td><td>\(< 0.0001\)</td>
</tr>
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
<tr>
<td>s(thi_mean_t0_3d):paritymultiparous</td><td>8.0636</td><td>8.0636</td><td>1133.7258</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>s(thi_mean_t0_3d):parityprimiparous</td><td>8.5711</td><td>8.5711</td><td>44.5719</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>s(days_in_milk_t):paritymultiparous</td><td>14.5547</td><td>14.5547</td><td>57761.6129</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>s(days_in_milk_t):parityprimiparous</td><td>13.8436</td><td>13.8436</td><td>9080.5596</td><td>\(< 0.0001\)</td>
</tr>
</tbody>
</table>
</div>
<figcaption style="text-align: left;">
Table D.61: Jersey: Milk Yield - 1998-2023 - GAMM model summary without random effect terms.
</figcaption>
<br>

<div>
<table>
<thead>
<tr>
<th>Smooth Term Fixed Effect</th><th>Est.</th><th>SE</th><th>z</th><th>p</th>
</tr>
</thead>
<tbody>
<tr>
<td>s(thi_mean_t0_3d):multiFx1</td><td>0.3076</td><td>0.0866</td><td>3.55</td><td>\(< 0.0004\)</td>
</tr>
<tr>
<td>s(thi_mean_t0_3d):primiFx1</td><td>0.1474</td><td>0.1459</td><td>1.01</td><td>0.3124</td>
</tr>
<tr>
<td>s(days_in_milk_):multiFx1</td><td>4.9106</td><td>0.3978</td><td>12.34</td><td>\(< 1e-34\)</td>
</tr>
<tr>
<td>s(days_in_milk_):primiFx1</td><td>4.1249</td><td>0.5323</td><td>7.75</td><td>\(< 1e-14\)</td>
</tr>
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
<tr>
<td>\( \sigma_\alpha\)</td><td>2.3991</td><td></td><td></td><td></td>
</tr>
<tr>
<td>\( \sigma_\iota\)</td><td>0.9500</td><td></td><td></td><td></td>
</tr>
<tr>
<td>\( \sigma_\phi\)</td><td>2.9764</td><td></td><td></td><td></td>
</tr>
<tr>
<td>s(thi_mean_t0_3d):multi</td><td>1.5575</td><td></td><td></td><td></td>
</tr>
<tr>
<td>s(days_in_milk_):primi</td><td>6.9995</td><td></td><td></td><td></td>
</tr>
<tr>
<td>s(days_in_milk_):multi</td><td>8.4095</td><td></td><td></td><td></td>
</tr>
<tr>
<td>s(thi_mean_t0_3d):primi</td><td>3.9762</td><td></td><td></td><td></td>
</tr>
<tr>
<td>Residual</td><td>2.9355</td><td></td><td></td><td></td>
</tr>
</tbody>
</table>
</div>
<figcaption style="text-align: left;">
Table D.62: Jersey: Milk Yield - 1998-2023 - Mixed Model Summary - Smooth Terms and Random Effects.
</figcaption>
<br>

#### **Model Diagnostics**

{{< figure
src="/media/figures/models/milk/full/je_milk_full/je_milk_full_diagnostics.png"
caption="Figure D.61: Jersey: Milk Yield - 1998-2023 - Diagnostic Plot"
id="fig_61"
class="figure-no-margin"
>}}

#### **THI Effect and Lactation Curve**

<div id="fig_main" style="display: grid; grid-template-rows: auto auto auto;">
  <div style="display: grid; grid-template-columns: 1fr 1fr;">
    <div>
      {{< figure
        src="/media/figures/models/milk/full/je_milk_full/je_milk_full_marginal_thi_milk_combined.png"
        caption=""
        id="fig_62_1"
        class="figure-no-margin"
      >}}
    </div>
    <div>
      {{< figure
        src="/media/figures/models/milk/full/je_milk_full/je_milk_full_marginal_dim_milk_combined.png"
        caption=""
        id="fig_62_2"
        class="figure-no-margin"
      >}}
    </div>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr;">
    <div>
      {{< figure
        src="/media/figures/models/milk/full/je_milk_full/je_milk_full_marginal_thi_milk_primi.png"
        caption=""
        id="fig_62_3"
        class="figure-no-margin"
      >}}
    </div>
    <div>
      {{< figure
        src="/media/figures/models/milk/full/je_milk_full/je_milk_full_marginal_dim_milk_primi.png"
        caption=""
        id="fig_62_4"
        class="figure-no-margin"
      >}}
    </div>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr;">
    <div>
      {{< figure
        src="/media/figures/models/milk/full/je_milk_full/je_milk_full_marginal_thi_milk_multi.png"
        caption=""
        id="fig_62_5"
        class="figure-no-margin"
      >}}
    </div>
    <div>
      {{< figure
        src="/media/figures/models/milk/full/je_milk_full/je_milk_full_marginal_dim_milk_multi.png"
        caption=""
        id="fig_62_6"
        class="figure-no-margin"
      >}}
    </div>
  </div>
</div>
<figcaption style="text-align: left;">
Figure D.62: Jersey: Milk Yield - 1998 - 2023 - THI Effect and Lactation Curve
</figcaption>

### D.11.2: Split Period: Until 2010 - After 2010

#### **D.11.2.1: Split Period: 1998 - 2010** {#model_je_milk_before}

##### **Model Summary**

<div>
<table>
<thead>
<tr>
<th>A. parametric coefficients</th><th>Estimate</th><th>Std. Error</th><th>t-value</th><th>p-value</th>
</tr>
</thead>
<tbody>
<tr>
<td>(Intercept)</td><td>13.8464</td><td>0.6158</td><td>22.4846</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>parityprimiparous</td><td>-1.5962</td><td>0.0195</td><td>-81.7385</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year1999</td><td>-0.4670</td><td>0.6855</td><td>-0.6812</td><td>0.4958</td>
</tr>
<tr>
<td>year2000</td><td>0.2987</td><td>0.6751</td><td>0.4424</td><td>0.6582</td>
</tr>
<tr>
<td>year2001</td><td>0.9551</td><td>0.6524</td><td>1.4639</td><td>0.1432</td>
</tr>
<tr>
<td>year2002</td><td>1.5417</td><td>0.6531</td><td>2.3604</td><td>0.0183</td>
</tr>
<tr>
<td>year2003</td><td>2.0455</td><td>0.6455</td><td>3.1688</td><td>0.0015</td>
</tr>
<tr>
<td>year2004</td><td>2.6115</td><td>0.6385</td><td>4.0902</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2005</td><td>2.8675</td><td>0.6331</td><td>4.5293</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2006</td><td>3.2272</td><td>0.6297</td><td>5.1248</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2007</td><td>3.1239</td><td>0.6291</td><td>4.9658</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2008</td><td>3.4796</td><td>0.6295</td><td>5.5276</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2009</td><td>3.8885</td><td>0.6287</td><td>6.1845</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2010</td><td>4.2474</td><td>0.6261</td><td>6.7842</td><td>\(< 0.0001\)</td>
</tr>
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
<tr>
<td>s(thi_mean_t0_3d):paritymultiparous</td><td>7.4687</td><td>7.4687</td><td>367.5611</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>s(thi_mean_t0_3d):parityprimiparous</td><td>5.9291</td><td>5.9291</td><td>31.4722</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>s(days_in_milk_t):paritymultiparous</td><td>13.9600</td><td>13.9600</td><td>17839.8816</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>s(days_in_milk_t):parityprimiparous</td><td>12.8822</td><td>12.8822</td><td>3856.3426</td><td>\(< 0.0001\)</td>
</tr>
</tbody>
</table>
</div>
<figcaption style="text-align: left;">
Table D.63: Jersey: Milk Yield - 1998-2010 - GAMM model summary without random effect terms.
</figcaption>
<br>

<div>
<table>
<thead>
<tr>
<th>Smooth Term Fixed Effect</th><th>Est.</th><th>SE</th><th>z</th><th>p</th>
</tr>
</thead>
<tbody>
<tr>
<td>s(thi_mean_t0_3d):multiFx1</td><td>0.3833</td><td>0.1433</td><td>2.68</td><td>0.0075</td>
</tr>
<tr>
<td>s(thi_mean_t0_3d):primiFx1</td><td>0.0868</td><td>0.1631</td><td>0.53</td><td>0.5943</td>
</tr>
<tr>
<td>s(days_in_milk_):multiFx1</td><td>4.2188</td><td>0.6749</td><td>6.25</td><td>\(< 1e-09\)</td>
</tr>
<tr>
<td>s(days_in_milk_):primiFx1</td><td>3.1564</td><td>0.7455</td><td>4.23</td><td>\(< 1e-04\)</td>
</tr>
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
<tr>
<td>\( \sigma_\alpha\)</td><td>0.9524</td><td></td><td></td><td></td>
</tr>
<tr>
<td>\( \sigma_\iota\)</td><td>2.2355</td><td></td><td></td><td></td>
</tr>
<tr>
<td>\( \sigma_\phi\)</td><td>2.6202</td><td></td><td></td><td></td>
</tr>
<tr>
<td>s(thi_mean_t0_3d):multi</td><td>1.8172</td><td></td><td></td><td></td>
</tr>
<tr>
<td>s(days_in_milk_):primi</td><td>7.1500</td><td></td><td></td><td></td>
</tr>
<tr>
<td>s(days_in_milk_):multi</td><td>9.1468</td><td></td><td></td><td></td>
</tr>
<tr>
<td>s(thi_mean_t0_3d):primi</td><td>1.3871</td><td></td><td></td><td></td>
</tr>
<tr>
<td>Residual</td><td>2.6539</td><td></td><td></td><td></td>
</tr>
</tbody>
</table>
</div>
<figcaption style="text-align: left;">
Table D.64: Jersey: Milk Yield - 1998-2010 - Mixed Model Summary - Smooth Terms and Random Effects.
</figcaption>
<br>

##### **Model Diagnostics**

{{< figure
src="/media/figures/models/milk/before2010/je_milk_before2010/je_milk_before2010_diagnostics.png"
caption="Figure D.63: Jersey: Milk Yield - 1998-2010 - Diagnostic Plot"
id="fig_63"
class="figure-no-margin"
>}}

##### **THI Effect and Lactation Curve**

<div id="fig_main" style="display: grid; grid-template-rows: auto auto auto;">
  <div style="display: grid; grid-template-columns: 1fr 1fr;">
    <div>
      {{< figure
        src="/media/figures/models/milk/before2010/je_milk_before2010/je_milk_before2010_marginal_thi_milk_combined.png"
        caption=""
        id="fig_64_1"
        class="figure-no-margin"
      >}}
    </div>
    <div>
      {{< figure
        src="/media/figures/models/milk/before2010/je_milk_before2010/je_milk_before2010_marginal_dim_milk_combined.png"
        caption=""
        id="fig_64_2"
        class="figure-no-margin"
      >}}
    </div>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr;">
    <div>
      {{< figure
        src="/media/figures/models/milk/before2010/je_milk_before2010/je_milk_before2010_marginal_thi_milk_primi.png"
        caption=""
        id="fig_64_3"
        class="figure-no-margin"
      >}}
    </div>
    <div>
      {{< figure
        src="/media/figures/models/milk/before2010/je_milk_before2010/je_milk_before2010_marginal_dim_milk_primi.png"
        caption=""
        id="fig_64_4"
        class="figure-no-margin"
      >}}
    </div>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr;">
    <div>
      {{< figure
        src="/media/figures/models/milk/before2010/je_milk_before2010/je_milk_before2010_marginal_thi_milk_multi.png"
        caption=""
        id="fig_64_5"
        class="figure-no-margin"
      >}}
    </div>
    <div>
      {{< figure
        src="/media/figures/models/milk/before2010/je_milk_before2010/je_milk_before2010_marginal_dim_milk_multi.png"
        caption=""
        id="fig_64_6"
        class="figure-no-margin"
      >}}
    </div>
  </div>
</div>
<figcaption style="text-align: left;">
Figure D.64: Jersey: Milk Yield - 1998 - 2010 - THI Effect and Lactation Curve
</figcaption>

#### **D.11.2.2: Split Period: 2010 - 2023** {#model_je_milk_after}

##### **Model Summary**

<div>
<table>
<thead>
<tr>
<th>A. parametric coefficients</th><th>Estimate</th><th>Std. Error</th><th>t-value</th><th>p-value</th>
</tr>
</thead>
<tbody>
<tr>
<td>(Intercept)</td><td>16.9374</td><td>0.1584</td><td>106.9310</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>parityprimiparous</td><td>-2.0885</td><td>0.0163</td><td>-128.1973</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2012</td><td>0.2060</td><td>0.1796</td><td>1.1471</td><td>0.2513</td>
</tr>
<tr>
<td>year2013</td><td>0.2842</td><td>0.2108</td><td>1.3481</td><td>0.1776</td>
</tr>
<tr>
<td>year2014</td><td>0.8749</td><td>0.2054</td><td>4.2601</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2015</td><td>0.9939</td><td>0.2045</td><td>4.8606</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2016</td><td>1.2244</td><td>0.1932</td><td>6.3379</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2017</td><td>1.6126</td><td>0.1992</td><td>8.0952</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2018</td><td>1.9356</td><td>0.1895</td><td>10.2118</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2019</td><td>2.2870</td><td>0.1840</td><td>12.4266</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2020</td><td>2.5084</td><td>0.2001</td><td>12.5361</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2021</td><td>2.5636</td><td>0.1994</td><td>12.8587</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2022</td><td>2.5237</td><td>0.2008</td><td>12.5669</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>year2023</td><td>2.6125</td><td>0.1791</td><td>14.5866</td><td>\(< 0.0001\)</td>
</tr>
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
<tr>
<td>s(thi_mean_t0_3d):paritymultiparous</td><td>8.1013</td><td>8.1013</td><td>856.5674</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>s(thi_mean_t0_3d):parityprimiparous</td><td>5.9065</td><td>5.9065</td><td>53.5215</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>s(days_in_milk_t):paritymultiparous</td><td>14.5129</td><td>14.5129</td><td>42118.2414</td><td>\(< 0.0001\)</td>
</tr>
<tr>
<td>s(days_in_milk_t):parityprimiparous</td><td>13.6452</td><td>13.6452</td><td>5835.7977</td><td>\(< 0.0001\)</td>
</tr>
</tbody>
</table>
</div>
<figcaption style="text-align: left;">
Table D.65: Jersey: Milk Yield - 2011-2023 - GAMM model summary without random effect terms.
</figcaption>
<br>

<div>
<table>
<thead>
<tr>
<th>Smooth Term Fixed Effect</th><th>Est.</th><th>SE</th><th>z</th><th>p</th>
</tr>
</thead>
<tbody>
<tr>
<td>s(thi_mean_t0_3d):multiFx1</td><td>-0.3112</td><td>0.1041</td><td>-2.99</td><td>0.0028</td>
</tr>
<tr>
<td>s(thi_mean_t0_3d):primiFx1</td><td>-0.1658</td><td>0.1121</td><td>-1.48</td><td>0.1391</td>
</tr>
<tr>
<td>s(days_in_milk_):multiFx1</td><td>4.7696</td><td>0.4524</td><td>10.54</td><td>\(< 1e-25\)</td>
</tr>
<tr>
<td>s(days_in_milk_):primiFx1</td><td>3.9223</td><td>0.6090</td><td>6.44</td><td>\(< 1e-09\)</td>
</tr>
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
<tr>
<td>\( \sigma_\alpha\)</td><td>2.3907</td><td></td><td></td><td></td>
</tr>
<tr>
<td>\( \sigma_\iota\)</td><td>0.9756</td><td></td><td></td><td></td>
</tr>
<tr>
<td>\( \sigma_\phi\)</td><td>3.1309</td><td></td><td></td><td></td>
</tr>
<tr>
<td>s(thi_mean_t0_3d):multi</td><td>1.9309</td><td></td><td></td><td></td>
</tr>
<tr>
<td>s(days_in_milk_):primi</td><td>7.4722</td><td></td><td></td><td></td>
</tr>
<tr>
<td>s(days_in_milk_):multi</td><td>9.2408</td><td></td><td></td><td></td>
</tr>
<tr>
<td>s(thi_mean_t0_3d):primi</td><td>1.0857</td><td></td><td></td><td></td>
</tr>
<tr>
<td>Residual</td><td>2.9808</td><td></td><td></td><td></td>
</tr>
</tbody>
</table>
</div>
<figcaption style="text-align: left;">
Table D.66: Jersey: Milk Yield - 2011-2023 - Mixed Model Summary - Smooth Terms and Random Effects.
</figcaption>
<br>

##### **Model Diagnostics**

{{< figure
src="/media/figures/models/milk/after2010/je_milk_after2010/je_milk_after2010_diagnostics.png"
caption="Figure D.65: Jersey: Milk Yield - 2011-2023 - Diagnostic Plot"
id="fig_65"
class="figure-no-margin"
>}}

##### **THI Effect and Lactation Curve**

<div id="fig_main" style="display: grid; grid-template-rows: auto auto auto;">
  <div style="display: grid; grid-template-columns: 1fr 1fr;">
    <div>
      {{< figure
        src="/media/figures/models/milk/after2010/je_milk_after2010/je_milk_after2010_marginal_thi_milk_combined.png"
        caption=""
        id="fig_66_1"
        class="figure-no-margin"
      >}}
    </div>
    <div>
      {{< figure
        src="/media/figures/models/milk/after2010/je_milk_after2010/je_milk_after2010_marginal_dim_milk_combined.png"
        caption=""
        id="fig_66_2"
        class="figure-no-margin"
      >}}
    </div>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr;">
    <div>
      {{< figure
        src="/media/figures/models/milk/after2010/je_milk_after2010/je_milk_after2010_marginal_thi_milk_primi.png"
        caption=""
        id="fig_66_3"
        class="figure-no-margin"
      >}}
    </div>
    <div>
      {{< figure
        src="/media/figures/models/milk/after2010/je_milk_after2010/je_milk_after2010_marginal_dim_milk_primi.png"
        caption=""
        id="fig_66_4"
        class="figure-no-margin"
      >}}
    </div>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr;">
    <div>
      {{< figure
        src="/media/figures/models/milk/after2010/je_milk_after2010/je_milk_after2010_marginal_thi_milk_multi.png"
        caption=""
        id="fig_66_5"
        class="figure-no-margin"
      >}}
    </div>
    <div>
      {{< figure
        src="/media/figures/models/milk/after2010/je_milk_after2010/je_milk_after2010_marginal_dim_milk_multi.png"
        caption=""
        id="fig_66_6"
        class="figure-no-margin"
      >}}
    </div>
  </div>
</div>
<figcaption style="text-align: left;">
Figure D.66: Jersey: Milk Yield - 2010 - 2023 - THI Effect and Lactation Curve
</figcaption>
