This repository contains metadata and download scripts for ocean/atmosphere reanalyses and observations.

  The following markdown file contains several ['summary' tables](#summary-tables) for comparison of basic information between datasets. These tables contain links to [more detailed information](#detailed-metadata) for each dataset. Download scripts for specific datasets are located in the [scripts](./scripts) folder.


# Summary tables

## Atmospheric

| Product and version         | Spatial Resolution   | Temporal Resolution       | Period Available   |
|:----------------------------|:---------------------|:--------------------------|:-------------------|
| [20CR v2](#20cr-v2)         | 2º x 2º              | Sub-daily, daily, monthly | 1850-2014          |
| [20CR v3](#20cr-v3)         | 1º x 1º              | Sub-daily, daily, monthly | 1836-2015          |
| [ERA-20C](#era-20c)         | 1º x 1º              | Sub-daily, daily, monthly | 1900-2010          |
| [ERA-Interim](#era-interim) | 0.75º x 0.75º        | Sub-daily, daily, monthly | 1979-2019          |
| [ERA5](#era5)               | 1º x 1º              | Sub-daily                 | 1979-present       |
| [JRA-55](#jra-55)           | 1.25º x 1.25º        | Sub-daily, monthly        | 1958-present       |
| [MERRA](#merra)             | 0.5º x 0.667º        | sub-daily, monthly        | 1979-2016          |
| [NNR 1](#nnr-1)             | 2.5º x 2.5º          | 4-times daily, monthly    | 1948-present       |
| [NNR 2](#nnr-2)             | 2.5º x 2.5º          | Sub-daily, daily, monthly | 1979-present       |
| [OAFlux](#oaflux)           | 1º x 1º              | Daily, monthly            | 1958-2012          |
| [TropFlux](#tropflux)       | ???                  | Daily, monthly            | 1979-2013          |



## Wind

| Product and version                                     | Spatial Resolution   | Temporal Resolution    | Period Available   |
|:--------------------------------------------------------|:---------------------|:-----------------------|:-------------------|
| [CCMP Wind Vector Analysis](#ccmp-wind-vector-analysis) | 0.25º x 0.25º        | sub-daily              | 1987-present       |
| [IFREMER ](#ifremer)                                    | 0.25º x 0.25º        | Sub-daily              | 1992-present       |
| [Quikscat](#quikscat)                                   | 1º x 1º              | Daily, weekly, monthly | 1999-2009          |
| [WASWind](#waswind)                                     | 4º x 4º              | Monthly                | 1950-2011          |



## Precipitation

| Product and version           | Spatial Resolution         | Temporal Resolution       | Period Available   |
|:------------------------------|:---------------------------|:--------------------------|:-------------------|
| [Aphrodite](#aphrodite)       | 0.25º x 0.25º, 0.5º x 0.5º | daily                     | 1950-2007          |
| [CMAP](#cmap)                 | 2.5º x 2.5º                | mothly                    | 1979-present       |
| [CMORPH](#cmorph)             | 0.25º x 0.25º              | Sub-daily, daily          | 2002-2017          |
| [CloudSat](#cloudsat)         | 2º x 2º                    | Monthly                   | 2006-2010          |
| [GPCP v2.3](#gpcp-v23)        | 2.5º x 2.5º                | Monthly                   | 1979-present       |
| [GPM IMERG](#gpm-imerg)       | 0.1º x 0.1º                | sub-daily, daily, monthly | 2000-present       |
| [PERSIANN-CDR](#persiann-cdr) | 0.25º x 0.25º              | Sub-daily, daily          | 1983-2020          |
| [TRMM/GPM](#trmm/gpm)         | 0.25º x 0.25º              | Sub-daily, daily, monthly | 1998-2019          |



## Surface Ocean

| Product and version   | Spatial Resolution   | Temporal Resolution   | Period Available   |
|:----------------------|:---------------------|:----------------------|:-------------------|
| [OSCAR](#oscar)       | 0.33º x 0.33º        | 5 day                 | 1992-present       |



## SSS

| Product and version   | Spatial Resolution   | Temporal Resolution       | Period Available   |
|:----------------------|:---------------------|:--------------------------|:-------------------|
| [Aquarius](#aquarius) | 1º x 1º              | Sub-daily, daily, monthly | 2011-2015          |
| [SMAP](#smap)         | 0.25º x 0.25º        | sub-daily                 | 2010-present       |
| [SMOS](#smos)         | 25km x 25km?         | sub-daily, daily, monthly | 2010-present       |



## SSH

| Product and version                                       | Spatial Resolution   | Temporal Resolution   | Period Available   |
|:----------------------------------------------------------|:---------------------|:----------------------|:-------------------|
| [AVISO](#aviso)                                           | 1º x 1º              | Monthly               | 1992-2010          |
| [Global Ocean gridded SSH](#global-ocean-gridded-ssh)     | 0.25º x 0.25º        | sub-daily             | 1992-present       |
| [Reconstructed Sea Level v1](#reconstructed-sea-level-v1) | 0.5º x 0.5º          | 7-day                 | 1950-2009          |



## SST

| Product and version          | Spatial Resolution   | Temporal Resolution   | Period Available   |
|:-----------------------------|:---------------------|:----------------------|:-------------------|
| [ERSSTv4](#ersstv4)          | 2º x 2º              | Monthly               | 1854-present       |
| [ERSSTv5](#ersstv5)          | 2º x 2º              | Monthly               | 1854-present       |
| [GISTEMP](#gistemp)          | 2º x 2º              | Monthly               | 1880-2018          |
| [HadISST v1.1](#hadisst-v11) | 1º x 1º              | Monthly               | 1870-present       |
| [MODIS/Aqua](#modis/aqua)    | 4km                  | daily                 | 2002-2016          |
| [OISST v2](#oisst-v2)        | 0.25º x 0.25º        | daily, monthly        | 1981-present       |
| [OSTIA SST](#ostia-sst)      | 0.05º x 0.05º        | daily                 | 1992-present       |



## Subsurface Ocean

| Product and version                           | Spatial Resolution   | Temporal Resolution   | Period Available     |
|:----------------------------------------------|:---------------------|:----------------------|:---------------------|
| [ARGO](#argo)                                 | 1º x 1º              | weekly, monthly       | 2000-present         |
| [ECCO2](#ecco2)                               | 0.25º x 0.25º        | Monthly               | 1992-2013            |
| [EN4.1.1](#en411)                             | 1º x 1º              | Monthly               | 1900-present         |
| [GFDL-ECDA v3.1](#gfdl-ecda-v31)              | 0.33º x 1º           | Monthly               | 1961-2012            |
| [GLORYS2v1](#glorys2v1)                       | 0.25º x 0.25º        | sub-daily             | 1993-2017            |
| [GODAS](#godas)                               | 1º x 1º              | Monthly               | 1980-present         |
| [IAP ocean temp & OHC](#iap-ocean-temp-&-ohc) | 1º x 1º              | Monthly               | 1940-2016            |
| [IOTA/QuOTA](#iota/quota)                     | 0.5º x 0.5º          | ???                   | 1870-present         |
| [ITF Makassar](#itf-makassar)                 | nan                  | monthly               | 2004-2011, 2013-2017 |
| [ITF from IX1](#itf-from-ix1)                 | nan                  | monthly               | 1983-present         |
| [Ishii Product](#ishii-product)               | 1º x 1º              | Monthly               | 1945-2012            |
| [Levitus](#levitus)                           | variable             | variable              | 1955-2010            |
| [ORAS4](#oras4)                               | 1º x 1º              | Monthly               | 1958-2017            |
| [ORAS5](#oras5)                               | 1º x 1º              | Monthly               | 1979-2018            |
| [SODA 2.2.4](#soda-224)                       | 0.25º x 0.4º         | Monthly               | 1871-2008            |



## Climate Indices

| Product and version                 |   Spatial Resolution |   Temporal Resolution |   Period Available |
|:------------------------------------|---------------------:|----------------------:|-------------------:|
| [DMI](#dmi)                         |                  nan |                   nan |                nan |
| [IPO](#ipo)                         |                  nan |                   nan |                nan |
| [NAO](#nao)                         |                  nan |                   nan |                nan |
| [Nino3.4](#nino34)                  |                  nan |                   nan |                nan |
| [ONI](#oni)                         |                  nan |                   nan |                nan |
| [PDO](#pdo)                         |                  nan |                   nan |                nan |
| [SAM](#sam)                         |                  nan |                   nan |                nan |
| [SOI](#soi)                         |                  nan |                   nan |                nan |
| [monsoon indices](#monsoon-indices) |                  nan |                   nan |                nan |



# Detailed metadata

### NNR 1
|                             |                                                                      |
|:----------------------------|:---------------------------------------------------------------------|
| **Category**                | Atmospheric                                                          |
| **Product and version**     | NNR 1                                                                |
| **Institution**             | NCEP/NCAR                                                            |
| **Product Type**            | Reanalysis                                                           |
| **Spatial Resolution**      | 2.5º x 2.5º                                                          |
| **Period Available**        | 1948-present                                                         |
| **Temporal Resolution**     | 4-times daily, monthly                                               |
| **Variables**               | <ul> <li>Air Temperature</li> <li>Geopotential Height</li> </ul>     |
| **Reference**               | Kistler et al. (2001)                                                |
| **On CLIDEX?**              | nan                                                                  |
| **Data Storage Location**   | nan                                                                  |
| **Downloaded Variables**    | nan                                                                  |
| **URL 1**                   | https://www.esrl.noaa.gov/psd/data/gridded/data.ncep.reanalysis.html |
| **URL 2**                   | nan                                                                  |
| **User / point of contact** | nan                                                                  |
| **Download script**         | [scripts/nnr-1](scripts/nnr-1)                                       |
### NNR 2
|                             |                                                                                              |
|:----------------------------|:---------------------------------------------------------------------------------------------|
| **Category**                | Atmospheric                                                                                  |
| **Product and version**     | NNR 2                                                                                        |
| **Institution**             | NCEP/NCAR                                                                                    |
| **Product Type**            | Reanlysis                                                                                    |
| **Spatial Resolution**      | 2.5º x 2.5º                                                                                  |
| **Period Available**        | 1979-present                                                                                 |
| **Temporal Resolution**     | Sub-daily, daily, monthly                                                                    |
| **Variables**               | <ul> <li>Air Temperature</li> <li>Geopotential Height</li> <li>Precipitable water</li> </ul> |
| **Reference**               | Kanamitsu et al. (2002)                                                                      |
| **On CLIDEX?**              | nan                                                                                          |
| **Data Storage Location**   | nan                                                                                          |
| **Downloaded Variables**    | nan                                                                                          |
| **URL 1**                   | https://www.cpc.ncep.noaa.gov/products/wesley/reanalysis2/                                   |
| **URL 2**                   | nan                                                                                          |
| **User / point of contact** | nan                                                                                          |
| **Download script**         | [scripts/nnr-2](scripts/nnr-2)                                                               |
### MERRA
|                             |                                                                                                        |
|:----------------------------|:-------------------------------------------------------------------------------------------------------|
| **Category**                | Atmospheric                                                                                            |
| **Product and version**     | MERRA                                                                                                  |
| **Institution**             | NASA                                                                                                   |
| **Product Type**            | Reanalysis                                                                                             |
| **Spatial Resolution**      | 0.5º x 0.667º                                                                                          |
| **Period Available**        | 1979-2016                                                                                              |
| **Temporal Resolution**     | sub-daily, monthly                                                                                     |
| **Variables**               | <ul> <li>AirT</li> <li>geopotential height</li> <li>precipitable water</li> <li>water vapor</li> </ul> |
| **Reference**               | Rienecker et al. (2011)                                                                                |
| **On CLIDEX?**              | nan                                                                                                    |
| **Data Storage Location**   | nan                                                                                                    |
| **Downloaded Variables**    | nan                                                                                                    |
| **URL 1**                   | https://gmao.gsfc.nasa.gov/reanalysis/MERRA/                                                           |
| **URL 2**                   | nan                                                                                                    |
| **User / point of contact** | nan                                                                                                    |
| **Download script**         | [scripts/merra](scripts/merra)                                                                         |
### ERA-Interim
|                             |                                                                                                                                                                                                                                            |
|:----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Category**                | Atmospheric                                                                                                                                                                                                                                |
| **Product and version**     | ERA-Interim                                                                                                                                                                                                                                |
| **Institution**             | ECMWF                                                                                                                                                                                                                                      |
| **Product Type**            | Reanalysis                                                                                                                                                                                                                                 |
| **Spatial Resolution**      | 0.75º x 0.75º                                                                                                                                                                                                                              |
| **Period Available**        | 1979-2019                                                                                                                                                                                                                                  |
| **Temporal Resolution**     | Sub-daily, daily, monthly                                                                                                                                                                                                                  |
| **Variables**               | <ul> <li>AirT</li> <li>geopotential height</li> <li>precipitable water</li> <li>precip</li> <li>wind</li> <li>E-P</li> <li>humidity</li> <li>surface pressure</li> <li>water vapor flux</li> <li>cloud liquid/frozen water flux</li> </ul> |
| **Reference**               | Dee et al. (2008; 2011; 2014)                                                                                                                                                                                                              |
| **On CLIDEX?**              | Y                                                                                                                                                                                                                                          |
| **Data Storage Location**   | /climodes/data7/datasets/ERA-int/WAM_moisture_tracking_data                                                                                                                                                                                |
| **Downloaded Variables**    | nan                                                                                                                                                                                                                                        |
| **URL 1**                   | https://www.ecmwf.int/en/research/climate-reanalysis/era-interim                                                                                                                                                                           |
| **URL 2**                   | nan                                                                                                                                                                                                                                        |
| **User / point of contact** | nan                                                                                                                                                                                                                                        |
| **Download script**         | [scripts/era-interim](scripts/era-interim)                                                                                                                                                                                                 |
### ERA-20C
|                             |                                                                                                                                                                                                                                                              |
|:----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Category**                | Atmospheric                                                                                                                                                                                                                                                  |
| **Product and version**     | ERA-20C                                                                                                                                                                                                                                                      |
| **Institution**             | ECMWF                                                                                                                                                                                                                                                        |
| **Product Type**            | Reanalysis                                                                                                                                                                                                                                                   |
| **Spatial Resolution**      | 1º x 1º                                                                                                                                                                                                                                                      |
| **Period Available**        | 1900-2010                                                                                                                                                                                                                                                    |
| **Temporal Resolution**     | Sub-daily, daily, monthly                                                                                                                                                                                                                                    |
| **Variables**               | <ul> <li>multiple variables (e.g. Air temperature</li> <li>geopotential height</li> <li>heat flux</li> <li>humidity</li> <li>surface pressure</li> <li>surface roughness</li> <li>surface winds</li> <li>convergence</li> <li>sea level pressure)</li> </ul> |
| **Reference**               | Poli et al. (2013)                                                                                                                                                                                                                                           |
| **On CLIDEX?**              | nan                                                                                                                                                                                                                                                          |
| **Data Storage Location**   | nan                                                                                                                                                                                                                                                          |
| **Downloaded Variables**    | nan                                                                                                                                                                                                                                                          |
| **URL 1**                   | https://rda.ucar.edu/datasets/ds626.0/                                                                                                                                                                                                                       |
| **URL 2**                   | nan                                                                                                                                                                                                                                                          |
| **User / point of contact** | nan                                                                                                                                                                                                                                                          |
| **Download script**         | [scripts/era-20c](scripts/era-20c)                                                                                                                                                                                                                           |
### ERA5
|                             |                                                                                                                                                                                                          |
|:----------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Category**                | Atmospheric                                                                                                                                                                                              |
| **Product and version**     | ERA5                                                                                                                                                                                                     |
| **Institution**             | ECMWF                                                                                                                                                                                                    |
| **Product Type**            | Reanalysis                                                                                                                                                                                               |
| **Spatial Resolution**      | 1º x 1º                                                                                                                                                                                                  |
| **Period Available**        | 1979-present                                                                                                                                                                                             |
| **Temporal Resolution**     | Sub-daily                                                                                                                                                                                                |
| **Variables**               | <ul> <li>Pressure level data: wind and specific humidity. Single-level data: evap.</li> <li>precip.</li> <li>surface pressure</li> <li>precipitable water</li> <li>liquid/frozen water fluxes</li> </ul> |
| **Reference**               | nan                                                                                                                                                                                                      |
| **On CLIDEX?**              | Y                                                                                                                                                                                                        |
| **Data Storage Location**   | /clidex/data/reanalysis/era5/                                                                                                                                                                            |
| **Downloaded Variables**    | nan                                                                                                                                                                                                      |
| **URL 1**                   | nan                                                                                                                                                                                                      |
| **URL 2**                   | nan                                                                                                                                                                                                      |
| **User / point of contact** | Mariya                                                                                                                                                                                                   |
| **Download script**         | [scripts/era5](scripts/era5)                                                                                                                                                                             |
### 20CR v2
|                             |                                                                                                                  |
|:----------------------------|:-----------------------------------------------------------------------------------------------------------------|
| **Category**                | Atmospheric                                                                                                      |
| **Product and version**     | 20CR v2                                                                                                          |
| **Institution**             | NOAA                                                                                                             |
| **Product Type**            | Reanalysis                                                                                                       |
| **Spatial Resolution**      | 2º x 2º                                                                                                          |
| **Period Available**        | 1850-2014                                                                                                        |
| **Temporal Resolution**     | Sub-daily, daily, monthly                                                                                        |
| **Variables**               | <ul> <li>AirT</li> <li>geopotential height</li> <li>zonal/meridional wind</li> <li>precipitable water</li> </ul> |
| **Reference**               | Compo et al. (2011)                                                                                              |
| **On CLIDEX?**              | nan                                                                                                              |
| **Data Storage Location**   | nan                                                                                                              |
| **Downloaded Variables**    | nan                                                                                                              |
| **URL 1**                   | https://www.esrl.noaa.gov/psd/data/gridded/data.20thC_ReanV2.html                                                |
| **URL 2**                   | nan                                                                                                              |
| **User / point of contact** | nan                                                                                                              |
| **Download script**         | [scripts/20cr-v2](scripts/20cr-v2)                                                                               |
### 20CR v3
|                             |                                                                                                                  |
|:----------------------------|:-----------------------------------------------------------------------------------------------------------------|
| **Category**                | Atmospheric                                                                                                      |
| **Product and version**     | 20CR v3                                                                                                          |
| **Institution**             | NOAA                                                                                                             |
| **Product Type**            | Reanalysis                                                                                                       |
| **Spatial Resolution**      | 1º x 1º                                                                                                          |
| **Period Available**        | 1836-2015                                                                                                        |
| **Temporal Resolution**     | Sub-daily, daily, monthly                                                                                        |
| **Variables**               | <ul> <li>AirT</li> <li>geopotential height</li> <li>zonal/meridional wind</li> <li>precipitable water</li> </ul> |
| **Reference**               | Giese et al. (2016); Slivinski et al. (2019)                                                                     |
| **On CLIDEX?**              | nan                                                                                                              |
| **Data Storage Location**   | nan                                                                                                              |
| **Downloaded Variables**    | nan                                                                                                              |
| **URL 1**                   | https://www.esrl.noaa.gov/psd/data/gridded/data.20thC_ReanV3.html                                                |
| **URL 2**                   | nan                                                                                                              |
| **User / point of contact** | nan                                                                                                              |
| **Download script**         | [scripts/20cr-v3](scripts/20cr-v3)                                                                               |
### JRA-55
|                             |                                                                                              |
|:----------------------------|:---------------------------------------------------------------------------------------------|
| **Category**                | Atmospheric                                                                                  |
| **Product and version**     | JRA-55                                                                                       |
| **Institution**             | JMA                                                                                          |
| **Product Type**            | Reanalysis                                                                                   |
| **Spatial Resolution**      | 1.25º x 1.25º                                                                                |
| **Period Available**        | 1958-present                                                                                 |
| **Temporal Resolution**     | Sub-daily, monthly                                                                           |
| **Variables**               | <ul> <li>Air Temperature</li> <li>Geopotential Height</li> <li>Precipitable water</li> </ul> |
| **Reference**               | Tsujino (2015)                                                                               |
| **On CLIDEX?**              | Y                                                                                            |
| **Data Storage Location**   | /clidex/data/forcing/                                                                        |
| **Downloaded Variables**    | nan                                                                                          |
| **URL 1**                   | https://jra.kishou.go.jp/JRA-55/index_en.html                                                |
| **URL 2**                   | nan                                                                                          |
| **User / point of contact** | nan                                                                                          |
| **Download script**         | [scripts/jra-55](scripts/jra-55)                                                             |
### OAFlux
|                             |                                                                                                                                                     |
|:----------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Category**                | Atmospheric                                                                                                                                         |
| **Product and version**     | OAFlux                                                                                                                                              |
| **Institution**             | WHOI                                                                                                                                                |
| **Product Type**            | Blended renalysis and satellite to calc. fluxes                                                                                                     |
| **Spatial Resolution**      | 1º x 1º                                                                                                                                             |
| **Period Available**        | 1958-2012                                                                                                                                           |
| **Temporal Resolution**     | Daily, monthly                                                                                                                                      |
| **Variables**               | <ul> <li>Latent & sensible heat flux</li> <li>radiation</li> <li>wind</li> <li>SST</li> <li>ocean surface flux</li> <li>wind stress curl</li> </ul> |
| **Reference**               | Yu, Jin, and Weller (2008)                                                                                                                          |
| **On CLIDEX?**              | nan                                                                                                                                                 |
| **Data Storage Location**   | nan                                                                                                                                                 |
| **Downloaded Variables**    | nan                                                                                                                                                 |
| **URL 1**                   | http://oaflux.whoi.edu/description.html                                                                                                             |
| **URL 2**                   | nan                                                                                                                                                 |
| **User / point of contact** | nan                                                                                                                                                 |
| **Download script**         | [scripts/oaflux](scripts/oaflux)                                                                                                                    |
### TropFlux
|                             |                                                                                                                                                                                                                                                       |
|:----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Category**                | Atmospheric                                                                                                                                                                                                                                           |
| **Product and version**     | TropFlux                                                                                                                                                                                                                                              |
| **Institution**             | ???                                                                                                                                                                                                                                                   |
| **Product Type**            | Reanalysis                                                                                                                                                                                                                                            |
| **Spatial Resolution**      | ???                                                                                                                                                                                                                                                   |
| **Period Available**        | 1979-2013                                                                                                                                                                                                                                             |
| **Temporal Resolution**     | Daily, monthly                                                                                                                                                                                                                                        |
| **Variables**               | <ul> <li>Specific humidity</li> <li>air temperature</li> <li>SST</li> <li>wind speed</li> <li>net shortwave and longwave radiation</li> <li>latent and sensible heat flux</li> <li>surface heat flux</li> <li>zonal/meridional wind stress</li> </ul> |
| **Reference**               | Kumar et al. (2013)                                                                                                                                                                                                                                   |
| **On CLIDEX?**              | nan                                                                                                                                                                                                                                                   |
| **Data Storage Location**   | nan                                                                                                                                                                                                                                                   |
| **Downloaded Variables**    | nan                                                                                                                                                                                                                                                   |
| **URL 1**                   | https://incois.gov.in/tropflux/overview.jsp                                                                                                                                                                                                           |
| **URL 2**                   | nan                                                                                                                                                                                                                                                   |
| **User / point of contact** | nan                                                                                                                                                                                                                                                   |
| **Download script**         | [scripts/tropflux](scripts/tropflux)                                                                                                                                                                                                                  |
### Quikscat
|                             |                                                                          |
|:----------------------------|:-------------------------------------------------------------------------|
| **Category**                | Wind                                                                     |
| **Product and version**     | Quikscat                                                                 |
| **Institution**             | NASA JPL                                                                 |
| **Product Type**            | Satellite                                                                |
| **Spatial Resolution**      | 1º x 1º                                                                  |
| **Period Available**        | 1999-2009                                                                |
| **Temporal Resolution**     | Daily, weekly, monthly                                                   |
| **Variables**               | wind                                                                     |
| **Reference**               | nan                                                                      |
| **On CLIDEX?**              | nan                                                                      |
| **Data Storage Location**   | nan                                                                      |
| **Downloaded Variables**    | nan                                                                      |
| **URL 1**                   | https://podaac.jpl.nasa.gov/highlights/GriddedClimateVariables_2012_0913 |
| **URL 2**                   | nan                                                                      |
| **User / point of contact** | nan                                                                      |
| **Download script**         | [scripts/quikscat](scripts/quikscat)                                     |
### IFREMER 
|                             |                                                                             |
|:----------------------------|:----------------------------------------------------------------------------|
| **Category**                | Wind                                                                        |
| **Product and version**     | IFREMER                                                                     |
| **Institution**             | APDRC                                                                       |
| **Product Type**            | Blended satellite and buoy; synthesized                                     |
| **Spatial Resolution**      | 0.25º x 0.25º                                                               |
| **Period Available**        | 1992-present                                                                |
| **Temporal Resolution**     | Sub-daily                                                                   |
| **Variables**               | wind                                                                        |
| **Reference**               | nan                                                                         |
| **On CLIDEX?**              | nan                                                                         |
| **Data Storage Location**   | nan                                                                         |
| **Downloaded Variables**    | nan                                                                         |
| **URL 1**                   | http://apdrc.soest.hawaii.edu/datadoc/ifremer_LOPS_blended_wind_6hourly.php |
| **URL 2**                   | nan                                                                         |
| **User / point of contact** | nan                                                                         |
| **Download script**         | [scripts/ifremer](scripts/ifremer)                                          |
### CCMP Wind Vector Analysis
|                             |                                                                        |
|:----------------------------|:-----------------------------------------------------------------------|
| **Category**                | Wind                                                                   |
| **Product and version**     | CCMP Wind Vector Analysis                                              |
| **Institution**             | NASA                                                                   |
| **Product Type**            | Satellite, moored buoy, model; synthesized                             |
| **Spatial Resolution**      | 0.25º x 0.25º                                                          |
| **Period Available**        | 1987-present                                                           |
| **Temporal Resolution**     | sub-daily                                                              |
| **Variables**               | wind                                                                   |
| **Reference**               | Atlas et al. (2011); Hoffman et al. (2003)                             |
| **On CLIDEX?**              | nan                                                                    |
| **Data Storage Location**   | nan                                                                    |
| **Downloaded Variables**    | nan                                                                    |
| **URL 1**                   | http://www.remss.com/measurements/ccmp/                                |
| **URL 2**                   | nan                                                                    |
| **User / point of contact** | nan                                                                    |
| **Download script**         | [scripts/ccmp-wind-vector-analysis](scripts/ccmp-wind-vector-analysis) |
### WASWind
|                             |                                                           |
|:----------------------------|:----------------------------------------------------------|
| **Category**                | Wind                                                      |
| **Product and version**     | WASWind                                                   |
| **Institution**             | U Hawaii IPRC                                             |
| **Product Type**            | Gridded from obs                                          |
| **Spatial Resolution**      | 4º x 4º                                                   |
| **Period Available**        | 1950-2011                                                 |
| **Temporal Resolution**     | Monthly                                                   |
| **Variables**               | <ul> <li>Wind</li> <li>wind stress</li> </ul>             |
| **Reference**               | Tokinaga and Xie (2011)                                   |
| **On CLIDEX?**              | nan                                                       |
| **Data Storage Location**   | nan                                                       |
| **Downloaded Variables**    | nan                                                       |
| **URL 1**                   | https://rda.ucar.edu/datasets/ds232.3/                    |
| **URL 2**                   | https://www.riam.kyushu-u.ac.jp/oed/tokinaga/waswind.html |
| **User / point of contact** | nan                                                       |
| **Download script**         | [scripts/waswind](scripts/waswind)                        |
### GPCP v2.3
|                             |                                                           |
|:----------------------------|:----------------------------------------------------------|
| **Category**                | Precipitation                                             |
| **Product and version**     | GPCP v2.3                                                 |
| **Institution**             | GEWEX, WCRP                                               |
| **Product Type**            | Gridded from obs                                          |
| **Spatial Resolution**      | 2.5º x 2.5º                                               |
| **Period Available**        | 1979-present                                              |
| **Temporal Resolution**     | Monthly                                                   |
| **Variables**               | precip                                                    |
| **Reference**               | Adler et al. (2003; 2017; 2018)                           |
| **On CLIDEX?**              | nan                                                       |
| **Data Storage Location**   | nan                                                       |
| **Downloaded Variables**    | nan                                                       |
| **URL 1**                   | https://www.esrl.noaa.gov/psd/data/gridded/data.gpcp.html |
| **URL 2**                   | nan                                                       |
| **User / point of contact** | nan                                                       |
| **Download script**         | [scripts/gpcp-v23](scripts/gpcp-v23)                      |
### TRMM/GPM
|                             |                                                 |
|:----------------------------|:------------------------------------------------|
| **Category**                | Precipitation                                   |
| **Product and version**     | TRMM/GPM                                        |
| **Institution**             | NASA                                            |
| **Product Type**            | Satellite                                       |
| **Spatial Resolution**      | 0.25º x 0.25º                                   |
| **Period Available**        | 1998-2019                                       |
| **Temporal Resolution**     | Sub-daily, daily, monthly                       |
| **Variables**               | precip                                          |
| **Reference**               | Kummerow et al. (2000)                          |
| **On CLIDEX?**              | nan                                             |
| **Data Storage Location**   | nan                                             |
| **Downloaded Variables**    | nan                                             |
| **URL 1**                   | https://pmm.nasa.gov/data-access/downloads/trmm |
| **URL 2**                   | nan                                             |
| **User / point of contact** | nan                                             |
| **Download script**         | [scripts/trmm/gpm](scripts/trmm/gpm)            |
### GPM IMERG
|                             |                                                |
|:----------------------------|:-----------------------------------------------|
| **Category**                | Precipitation                                  |
| **Product and version**     | GPM IMERG                                      |
| **Institution**             | NASA                                           |
| **Product Type**            | Satellite                                      |
| **Spatial Resolution**      | 0.1º x 0.1º                                    |
| **Period Available**        | 2000-present                                   |
| **Temporal Resolution**     | sub-daily, daily, monthly                      |
| **Variables**               | precip                                         |
| **Reference**               | Hou et al (2014), Liu and Zipser (2015)        |
| **On CLIDEX?**              | nan                                            |
| **Data Storage Location**   | nan                                            |
| **Downloaded Variables**    | nan                                            |
| **URL 1**                   | https://pmm.nasa.gov/data-access/downloads/gpm |
| **URL 2**                   | nan                                            |
| **User / point of contact** | nan                                            |
| **Download script**         | [scripts/gpm-imerg](scripts/gpm-imerg)         |
### CloudSat
|                             |                                                      |
|:----------------------------|:-----------------------------------------------------|
| **Category**                | Precipitation                                        |
| **Product and version**     | CloudSat                                             |
| **Institution**             | JPL, CSU                                             |
| **Product Type**            | Satellite                                            |
| **Spatial Resolution**      | 2º x 2º                                              |
| **Period Available**        | 2006-2010                                            |
| **Temporal Resolution**     | Monthly                                              |
| **Variables**               | <ul> <li>precip</li> <li>cloud properties</li> </ul> |
| **Reference**               | Stephens et al. (2002)                               |
| **On CLIDEX?**              | nan                                                  |
| **Data Storage Location**   | nan                                                  |
| **Downloaded Variables**    | nan                                                  |
| **URL 1**                   | https://cloudsat.atmos.colostate.edu/data            |
| **URL 2**                   | nan                                                  |
| **User / point of contact** | nan                                                  |
| **Download script**         | [scripts/cloudsat](scripts/cloudsat)                 |
### CMORPH
|                             |                                                                         |
|:----------------------------|:------------------------------------------------------------------------|
| **Category**                | Precipitation                                                           |
| **Product and version**     | CMORPH                                                                  |
| **Institution**             | NOAA CPC                                                                |
| **Product Type**            | Satellite                                                               |
| **Spatial Resolution**      | 0.25º x 0.25º                                                           |
| **Period Available**        | 2002-2017                                                               |
| **Temporal Resolution**     | Sub-daily, daily                                                        |
| **Variables**               | precip                                                                  |
| **Reference**               | Joyce et al. (2004)                                                     |
| **On CLIDEX?**              | nan                                                                     |
| **Data Storage Location**   | nan                                                                     |
| **Downloaded Variables**    | nan                                                                     |
| **URL 1**                   | https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html |
| **URL 2**                   | nan                                                                     |
| **User / point of contact** | nan                                                                     |
| **Download script**         | [scripts/cmorph](scripts/cmorph)                                        |
### Aphrodite
|                             |                                                       |
|:----------------------------|:------------------------------------------------------|
| **Category**                | Precipitation                                         |
| **Product and version**     | Aphrodite                                             |
| **Institution**             | JMA                                                   |
| **Product Type**            | Gridded from obs                                      |
| **Spatial Resolution**      | 0.25º x 0.25º, 0.5º x 0.5º                            |
| **Period Available**        | 1950-2007                                             |
| **Temporal Resolution**     | daily                                                 |
| **Variables**               | precip                                                |
| **Reference**               | Yatagai et al. (2012)                                 |
| **On CLIDEX?**              | nan                                                   |
| **Data Storage Location**   | nan                                                   |
| **Downloaded Variables**    | nan                                                   |
| **URL 1**                   | https://www.chikyu.ac.jp/precip/english/products.html |
| **URL 2**                   | nan                                                   |
| **User / point of contact** | nan                                                   |
| **Download script**         | [scripts/aphrodite](scripts/aphrodite)                |
### CMAP
|                             |                                                                           |
|:----------------------------|:--------------------------------------------------------------------------|
| **Category**                | Precipitation                                                             |
| **Product and version**     | CMAP                                                                      |
| **Institution**             | NOAA CPC                                                                  |
| **Product Type**            | Gridded from obs, satellite                                               |
| **Spatial Resolution**      | 2.5º x 2.5º                                                               |
| **Period Available**        | 1979-present                                                              |
| **Temporal Resolution**     | mothly                                                                    |
| **Variables**               | precip                                                                    |
| **Reference**               | Xie et al. (1996; 1997)                                                   |
| **On CLIDEX?**              | nan                                                                       |
| **Data Storage Location**   | nan                                                                       |
| **Downloaded Variables**    | nan                                                                       |
| **URL 1**                   | https://www.cpc.ncep.noaa.gov/products/global_precip/html/wpage.cmap.html |
| **URL 2**                   | nan                                                                       |
| **User / point of contact** | nan                                                                       |
| **Download script**         | [scripts/cmap](scripts/cmap)                                              |
### PERSIANN-CDR
|                             |                                                                |
|:----------------------------|:---------------------------------------------------------------|
| **Category**                | Precipitation                                                  |
| **Product and version**     | PERSIANN-CDR                                                   |
| **Institution**             | UCI CHRS                                                       |
| **Product Type**            | Satellite                                                      |
| **Spatial Resolution**      | 0.25º x 0.25º                                                  |
| **Period Available**        | 1983-2020                                                      |
| **Temporal Resolution**     | Sub-daily, daily                                               |
| **Variables**               | precip                                                         |
| **Reference**               | Ashouri et al. (2015)                                          |
| **On CLIDEX?**              | nan                                                            |
| **Data Storage Location**   | nan                                                            |
| **Downloaded Variables**    | nan                                                            |
| **URL 1**                   | https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc:C00854 |
| **URL 2**                   | nan                                                            |
| **User / point of contact** | nan                                                            |
| **Download script**         | [scripts/persiann-cdr](scripts/persiann-cdr)                   |
### OSCAR
|                             |                                                           |
|:----------------------------|:----------------------------------------------------------|
| **Category**                | Surface Ocean                                             |
| **Product and version**     | OSCAR                                                     |
| **Institution**             | NASA JPL                                                  |
| **Product Type**            | Gridded from obs, satellite                               |
| **Spatial Resolution**      | 0.33º x 0.33º                                             |
| **Period Available**        | 1992-present                                              |
| **Temporal Resolution**     | 5 day                                                     |
| **Variables**               | zonal and meridional surface currents                     |
| **Reference**               | ESR (2009)                                                |
| **On CLIDEX?**              | nan                                                       |
| **Data Storage Location**   | nan                                                       |
| **Downloaded Variables**    | nan                                                       |
| **URL 1**                   | https://podaac.jpl.nasa.gov/dataset/OSCAR_L4_OC_third-deg |
| **URL 2**                   | nan                                                       |
| **User / point of contact** | nan                                                       |
| **Download script**         | [scripts/oscar](scripts/oscar)                            |
### Aquarius
|                             |                                                                                                                             |
|:----------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| **Category**                | SSS                                                                                                                         |
| **Product and version**     | Aquarius                                                                                                                    |
| **Institution**             | NASA/CONAE                                                                                                                  |
| **Product Type**            | Satellite                                                                                                                   |
| **Spatial Resolution**      | 1º x 1º                                                                                                                     |
| **Period Available**        | 2011-2015                                                                                                                   |
| **Temporal Resolution**     | Sub-daily, daily, monthly                                                                                                   |
| **Variables**               | SSS                                                                                                                         |
| **Reference**               | Lagerloef et al. (2008)                                                                                                     |
| **On CLIDEX?**              | nan                                                                                                                         |
| **Data Storage Location**   | nan                                                                                                                         |
| **Downloaded Variables**    | nan                                                                                                                         |
| **URL 1**                   | https://podaac-tools.jpl.nasa.gov/drive/login?dest=L2RyaXZlL2ZpbGVzL2FsbERhdGEvYXF1YXJpdXMvTDMvbWFwcGVkL1Y1L21vbnRobHkvU0NJ |
| **URL 2**                   | nan                                                                                                                         |
| **User / point of contact** | nan                                                                                                                         |
| **Download script**         | [scripts/aquarius](scripts/aquarius)                                                                                        |
### SMOS
|                             |                                                                                        |
|:----------------------------|:---------------------------------------------------------------------------------------|
| **Category**                | SSS                                                                                    |
| **Product and version**     | SMOS                                                                                   |
| **Institution**             | CATDS                                                                                  |
| **Product Type**            | Satellite                                                                              |
| **Spatial Resolution**      | 25km x 25km?                                                                           |
| **Period Available**        | 2010-present                                                                           |
| **Temporal Resolution**     | sub-daily, daily, monthly                                                              |
| **Variables**               | SSS                                                                                    |
| **Reference**               | Boutin et al. (2016, 2018); Kolodziejczyk et al. (2016)                                |
| **On CLIDEX?**              | nan                                                                                    |
| **Data Storage Location**   | nan                                                                                    |
| **Downloaded Variables**    | nan                                                                                    |
| **URL 1**                   | https://www.catds.fr/Products/Available-products-from-CEC-OS/CEC-Locean-L3-Debiased-v3 |
| **URL 2**                   | nan                                                                                    |
| **User / point of contact** | nan                                                                                    |
| **Download script**         | [scripts/smos](scripts/smos)                                                           |
### SMAP
|                             |                                                                             |
|:----------------------------|:----------------------------------------------------------------------------|
| **Category**                | SSS                                                                         |
| **Product and version**     | SMAP                                                                        |
| **Institution**             | NASA JPL                                                                    |
| **Product Type**            | Satellite                                                                   |
| **Spatial Resolution**      | 0.25º x 0.25º                                                               |
| **Period Available**        | 2010-present                                                                |
| **Temporal Resolution**     | sub-daily                                                                   |
| **Variables**               | SSS                                                                         |
| **Reference**               | Fore et al. (2016)                                                          |
| **On CLIDEX?**              | nan                                                                         |
| **Data Storage Location**   | nan                                                                         |
| **Downloaded Variables**    | nan                                                                         |
| **URL 1**                   | https://podaac.jpl.nasa.gov/dataset/SMAP_JPL_L3_SSS_CAP_8DAY-RUNNINGMEAN_V4 |
| **URL 2**                   | nan                                                                         |
| **User / point of contact** | nan                                                                         |
| **Download script**         | [scripts/smap](scripts/smap)                                                |
### Global Ocean gridded SSH
|                             |                                                                                                                                                        |
|:----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Category**                | SSH                                                                                                                                                    |
| **Product and version**     | Global Ocean gridded SSH                                                                                                                               |
| **Institution**             | CMEMS (AVISO)                                                                                                                                          |
| **Product Type**            | Satellite                                                                                                                                              |
| **Spatial Resolution**      | 0.25º x 0.25º                                                                                                                                          |
| **Period Available**        | 1992-present                                                                                                                                           |
| **Temporal Resolution**     | sub-daily                                                                                                                                              |
| **Variables**               | <ul> <li>SLA</li> <li>ADT</li> <li>geostrophic velocities</li> </ul>                                                                                   |
| **Reference**               | nan                                                                                                                                                    |
| **On CLIDEX?**              | Y                                                                                                                                                      |
| **Data Storage Location**   | /clidex/data/obs/SSH/CMESM_SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047/                                                                               |
| **Downloaded Variables**    | SLA, ADT                                                                                                                                               |
| **URL 1**                   | http://marine.copernicus.eu/services-portfolio/access-to-products/?option=com_csw&view=details&product_id=SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047 |
| **URL 2**                   | nan                                                                                                                                                    |
| **User / point of contact** | nan                                                                                                                                                    |
| **Download script**         | [scripts/global-ocean-gridded-ssh](scripts/global-ocean-gridded-ssh)                                                                                   |
### AVISO
|                             |                                                                |
|:----------------------------|:---------------------------------------------------------------|
| **Category**                | SSH                                                            |
| **Product and version**     | AVISO                                                          |
| **Institution**             | NASA                                                           |
| **Product Type**            | Satellite                                                      |
| **Spatial Resolution**      | 1º x 1º                                                        |
| **Period Available**        | 1992-2010                                                      |
| **Temporal Resolution**     | Monthly                                                        |
| **Variables**               | <ul> <li>sea level</li> <li>SSH</li> </ul>                     |
| **Reference**               | AVISO (2011)                                                   |
| **On CLIDEX?**              | nan                                                            |
| **Data Storage Location**   | nan                                                            |
| **Downloaded Variables**    | nan                                                            |
| **URL 1**                   | https://podaac.jpl.nasa.gov/dataset/AVISO_L4_DYN_TOPO_1DEG_1MO |
| **URL 2**                   | nan                                                            |
| **User / point of contact** | nan                                                            |
| **Download script**         | [scripts/aviso](scripts/aviso)                                 |
### Reconstructed Sea Level v1
|                             |                                                                          |
|:----------------------------|:-------------------------------------------------------------------------|
| **Category**                | SSH                                                                      |
| **Product and version**     | Reconstructed Sea Level v1                                               |
| **Institution**             | CSEOF                                                                    |
| **Product Type**            | Satellite, in situ                                                       |
| **Spatial Resolution**      | 0.5º x 0.5º                                                              |
| **Period Available**        | 1950-2009                                                                |
| **Temporal Resolution**     | 7-day                                                                    |
| **Variables**               | Reconstructed SSH                                                        |
| **Reference**               | Hamlington et al. (2014)                                                 |
| **On CLIDEX?**              | nan                                                                      |
| **Data Storage Location**   | nan                                                                      |
| **Downloaded Variables**    | nan                                                                      |
| **URL 1**                   | https://podaac.jpl.nasa.gov/dataset/RECON_SEA_LEVEL_OST_L4_V1            |
| **URL 2**                   | nan                                                                      |
| **User / point of contact** | nan                                                                      |
| **Download script**         | [scripts/reconstructed-sea-level-v1](scripts/reconstructed-sea-level-v1) |
### ERSSTv4
|                             |                                                                                                                |
|:----------------------------|:---------------------------------------------------------------------------------------------------------------|
| **Category**                | SST                                                                                                            |
| **Product and version**     | ERSSTv4                                                                                                        |
| **Institution**             | NOAA                                                                                                           |
| **Product Type**            | Gridded from obs                                                                                               |
| **Spatial Resolution**      | 2º x 2º                                                                                                        |
| **Period Available**        | 1854-present                                                                                                   |
| **Temporal Resolution**     | Monthly                                                                                                        |
| **Variables**               | Reconstructed SST                                                                                              |
| **Reference**               | Huang et al. (2015); Liu et al. (2015)                                                                         |
| **On CLIDEX?**              | nan                                                                                                            |
| **Data Storage Location**   | nan                                                                                                            |
| **Downloaded Variables**    | nan                                                                                                            |
| **URL 1**                   | https://www.ncdc.noaa.gov/data-access/marineocean-data/extended-reconstructed-sea-surface-temperature-ersst-v4 |
| **URL 2**                   | nan                                                                                                            |
| **User / point of contact** | nan                                                                                                            |
| **Download script**         | [scripts/ersstv4](scripts/ersstv4)                                                                             |
### ERSSTv5
|                             |                                                           |
|:----------------------------|:----------------------------------------------------------|
| **Category**                | SST                                                       |
| **Product and version**     | ERSSTv5                                                   |
| **Institution**             | NOAA                                                      |
| **Product Type**            | Gridded from obs                                          |
| **Spatial Resolution**      | 2º x 2º                                                   |
| **Period Available**        | 1854-present                                              |
| **Temporal Resolution**     | Monthly                                                   |
| **Variables**               | Reconstructed SST                                         |
| **Reference**               | Huang et al. (2017)                                       |
| **On CLIDEX?**              | Y                                                         |
| **Data Storage Location**   | /clidex/data/obs/ERSSTv5/                                 |
| **Downloaded Variables**    | SST up to June 2019                                       |
| **URL 1**                   | https://psl.noaa.gov/data/gridded/data.noaa.ersst.v5.html |
| **URL 2**                   | nan                                                       |
| **User / point of contact** | Mariya                                                    |
| **Download script**         | [scripts/ersstv5](scripts/ersstv5)                        |
### OISST v2
|                             |                                                                            |
|:----------------------------|:---------------------------------------------------------------------------|
| **Category**                | SST                                                                        |
| **Product and version**     | OISST v2                                                                   |
| **Institution**             | NOAA                                                                       |
| **Product Type**            | Gridded from obs, satellite                                                |
| **Spatial Resolution**      | 0.25º x 0.25º                                                              |
| **Period Available**        | 1981-present                                                               |
| **Temporal Resolution**     | daily, monthly                                                             |
| **Variables**               | SST                                                                        |
| **Reference**               | Reynolds et al. (2007)                                                     |
| **On CLIDEX?**              | Y                                                                          |
| **Data Storage Location**   | /clidex/data/obs/OISSTv2/                                                  |
| **Downloaded Variables**    | nan                                                                        |
| **URL 1**                   | https://www.esrl.noaa.gov/psd/data/gridded/data.noaa.oisst.v2.highres.html |
| **URL 2**                   | nan                                                                        |
| **User / point of contact** | nan                                                                        |
| **Download script**         | [scripts/oisst-v2](scripts/oisst-v2)                                       |
### GISTEMP
|                             |                                        |
|:----------------------------|:---------------------------------------|
| **Category**                | SST                                    |
| **Product and version**     | GISTEMP                                |
| **Institution**             | NASA GISS                              |
| **Product Type**            | Gridded from obs                       |
| **Spatial Resolution**      | 2º x 2º                                |
| **Period Available**        | 1880-2018                              |
| **Temporal Resolution**     | Monthly                                |
| **Variables**               | <ul> <li>Air T</li> <li>SST</li> </ul> |
| **Reference**               | Hansen et al. (1999)                   |
| **On CLIDEX?**              | nan                                    |
| **Data Storage Location**   | nan                                    |
| **Downloaded Variables**    | nan                                    |
| **URL 1**                   | https://data.giss.nasa.gov/gistemp/    |
| **URL 2**                   | nan                                    |
| **User / point of contact** | nan                                    |
| **Download script**         | [scripts/gistemp](scripts/gistemp)     |
### MODIS/Aqua
|                             |                                                              |
|:----------------------------|:-------------------------------------------------------------|
| **Category**                | SST                                                          |
| **Product and version**     | MODIS/Aqua                                                   |
| **Institution**             | NASA GISS                                                    |
| **Product Type**            | Satellite                                                    |
| **Spatial Resolution**      | 4km                                                          |
| **Period Available**        | 2002-2016                                                    |
| **Temporal Resolution**     | daily                                                        |
| **Variables**               | <ul> <li>SST</li> <li>chlorophyll-a concentration</li> </ul> |
| **Reference**               | Ocean Biology Processing Group (2014)                        |
| **On CLIDEX?**              | nan                                                          |
| **Data Storage Location**   | nan                                                          |
| **Downloaded Variables**    | nan                                                          |
| **URL 1**                   | https://modis.gsfc.nasa.gov/data/dataprod/mod28.php          |
| **URL 2**                   | nan                                                          |
| **User / point of contact** | nan                                                          |
| **Download script**         | [scripts/modis/aqua](scripts/modis/aqua)                     |
### OSTIA SST
|                             |                                                             |
|:----------------------------|:------------------------------------------------------------|
| **Category**                | SST                                                         |
| **Product and version**     | OSTIA SST                                                   |
| **Institution**             | UKMO                                                        |
| **Product Type**            | Satellite                                                   |
| **Spatial Resolution**      | 0.05º x 0.05º                                               |
| **Period Available**        | 1992-present                                                |
| **Temporal Resolution**     | daily                                                       |
| **Variables**               | SST                                                         |
| **Reference**               | Donlon et al. (2012)                                        |
| **On CLIDEX?**              | nan                                                         |
| **Data Storage Location**   | nan                                                         |
| **Downloaded Variables**    | nan                                                         |
| **URL 1**                   | https://podaac.jpl.nasa.gov/dataset/OSTIA-UKMO-L4-GLOB-v2.0 |
| **URL 2**                   | nan                                                         |
| **User / point of contact** | nan                                                         |
| **Download script**         | [scripts/ostia-sst](scripts/ostia-sst)                      |
### HadISST v1.1
|                             |                                              |
|:----------------------------|:---------------------------------------------|
| **Category**                | SST                                          |
| **Product and version**     | HadISST v1.1                                 |
| **Institution**             | Hadley Centre, UK                            |
| **Product Type**            | Gridded from obs                             |
| **Spatial Resolution**      | 1º x 1º                                      |
| **Period Available**        | 1870-present                                 |
| **Temporal Resolution**     | Monthly                                      |
| **Variables**               | SST                                          |
| **Reference**               | Rayner et al. (2003)                         |
| **On CLIDEX?**              | nan                                          |
| **Data Storage Location**   | /clidex/data/obs/HadISST/                    |
| **Downloaded Variables**    | nan                                          |
| **URL 1**                   | https://www.metoffice.gov.uk/hadobs/hadisst/ |
| **URL 2**                   | nan                                          |
| **User / point of contact** | Mariya                                       |
| **Download script**         | [scripts/hadisst-v11](scripts/hadisst-v11)   |
### ORAS4
|                             |                                                                                                                      |
|:----------------------------|:---------------------------------------------------------------------------------------------------------------------|
| **Category**                | Subsurface Ocean                                                                                                     |
| **Product and version**     | ORAS4                                                                                                                |
| **Institution**             | ECMWF                                                                                                                |
| **Product Type**            | Reanalysis                                                                                                           |
| **Spatial Resolution**      | 1º x 1º                                                                                                              |
| **Period Available**        | 1958-2017                                                                                                            |
| **Temporal Resolution**     | Monthly                                                                                                              |
| **Variables**               | <ul> <li>T</li> <li>S</li> <li>precip</li> <li>wind stress</li> <li>zonal/meridional current</li> <li>MLD</li> </ul> |
| **Reference**               | Balmaseda et al. (2013)                                                                                              |
| **On CLIDEX?**              | nan                                                                                                                  |
| **Data Storage Location**   | nan                                                                                                                  |
| **Downloaded Variables**    | nan                                                                                                                  |
| **URL 1**                   | http://apdrc.soest.hawaii.edu/datadoc/ecmwf_oras4.php                                                                |
| **URL 2**                   | nan                                                                                                                  |
| **User / point of contact** | nan                                                                                                                  |
| **Download script**         | [scripts/oras4](scripts/oras4)                                                                                       |
### ORAS5
|                             |                                                                                                                                   |
|:----------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| **Category**                | Subsurface Ocean                                                                                                                  |
| **Product and version**     | ORAS5                                                                                                                             |
| **Institution**             | ECMWF                                                                                                                             |
| **Product Type**            | Reanalysis                                                                                                                        |
| **Spatial Resolution**      | 1º x 1º                                                                                                                           |
| **Period Available**        | 1979-2018                                                                                                                         |
| **Temporal Resolution**     | Monthly                                                                                                                           |
| **Variables**               | <ul> <li>T</li> <li>S</li> <li>precip</li> <li>wind stress</li> <li>zonal/meridional current</li> <li>MLD</li> <li>SSH</li> </ul> |
| **Reference**               | Zuo et al. (2019)                                                                                                                 |
| **On CLIDEX?**              | Y                                                                                                                                 |
| **Data Storage Location**   | /clidex/data/reanalysis/oras5/                                                                                                    |
| **Downloaded Variables**    | nan                                                                                                                               |
| **URL 1**                   | http://apdrc.soest.hawaii.edu/datadoc/ecmwf_oras5_1x1.php                                                                         |
| **URL 2**                   | nan                                                                                                                               |
| **User / point of contact** | nan                                                                                                                               |
| **Download script**         | [scripts/oras5](scripts/oras5)                                                                                                    |
### SODA 2.2.4
|                             |                                                                                           |
|:----------------------------|:------------------------------------------------------------------------------------------|
| **Category**                | Subsurface Ocean                                                                          |
| **Product and version**     | SODA 2.2.4                                                                                |
| **Institution**             | UMD                                                                                       |
| **Product Type**            | Reanalysis                                                                                |
| **Spatial Resolution**      | 0.25º x 0.4º                                                                              |
| **Period Available**        | 1871-2008                                                                                 |
| **Temporal Resolution**     | Monthly                                                                                   |
| **Variables**               | <ul> <li>T</li> <li>S</li> <li>u and v current components</li> <li>wind stress</li> </ul> |
| **Reference**               | Carton and Giese (2008)                                                                   |
| **On CLIDEX?**              | nan                                                                                       |
| **Data Storage Location**   | nan                                                                                       |
| **Downloaded Variables**    | nan                                                                                       |
| **URL 1**                   | https://coastwatch.pfeg.noaa.gov/erddap/info/hawaii_d90f_20ee_c4cb/index.html             |
| **URL 2**                   | nan                                                                                       |
| **User / point of contact** | nan                                                                                       |
| **Download script**         | [scripts/soda-224](scripts/soda-224)                                                      |
### GFDL-ECDA v3.1
|                             |                                                                                                                                                                                                                         |
|:----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Category**                | Subsurface Ocean                                                                                                                                                                                                        |
| **Product and version**     | GFDL-ECDA v3.1                                                                                                                                                                                                          |
| **Institution**             | GFDL                                                                                                                                                                                                                    |
| **Product Type**            | Reanalysis                                                                                                                                                                                                              |
| **Spatial Resolution**      | 0.33º x 1º                                                                                                                                                                                                              |
| **Period Available**        | 1961-2012                                                                                                                                                                                                               |
| **Temporal Resolution**     | Monthly                                                                                                                                                                                                                 |
| **Variables**               | <ul> <li>mixed layer depth</li> <li>S</li> <li>zonal and meridional wind stress</li> <li>sea water velocity</li> <li>P-E</li> <li>surface heat flux</li> <li>river water flux</li> <li>potential temperature</li> </ul> |
| **Reference**               | Chang et al. (2013)                                                                                                                                                                                                     |
| **On CLIDEX?**              | nan                                                                                                                                                                                                                     |
| **Data Storage Location**   | nan                                                                                                                                                                                                                     |
| **Downloaded Variables**    | nan                                                                                                                                                                                                                     |
| **URL 1**                   | http://apdrc.soest.hawaii.edu/datadoc/gfdl.php                                                                                                                                                                          |
| **URL 2**                   | nan                                                                                                                                                                                                                     |
| **User / point of contact** | nan                                                                                                                                                                                                                     |
| **Download script**         | [scripts/gfdl-ecda-v31](scripts/gfdl-ecda-v31)                                                                                                                                                                          |
### GODAS
|                             |                                                                                                                                     |
|:----------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| **Category**                | Subsurface Ocean                                                                                                                    |
| **Product and version**     | GODAS                                                                                                                               |
| **Institution**             | NCEP                                                                                                                                |
| **Product Type**            | Reanalysis                                                                                                                          |
| **Spatial Resolution**      | 1º x 1º                                                                                                                             |
| **Period Available**        | 1980-present                                                                                                                        |
| **Temporal Resolution**     | Monthly                                                                                                                             |
| **Variables**               | <ul> <li>3D velocity</li> <li>SST</li> <li>S</li> <li>heat flux</li> <li>MLD</li> <li>SSH</li> <li>potential temperature</li> </ul> |
| **Reference**               | Saha et al. (2006); Nishida (2011)                                                                                                  |
| **On CLIDEX?**              | nan                                                                                                                                 |
| **Data Storage Location**   | nan                                                                                                                                 |
| **Downloaded Variables**    | nan                                                                                                                                 |
| **URL 1**                   | https://www.cpc.ncep.noaa.gov/products/GODAS/                                                                                       |
| **URL 2**                   | nan                                                                                                                                 |
| **User / point of contact** | nan                                                                                                                                 |
| **Download script**         | [scripts/godas](scripts/godas)                                                                                                      |
### ECCO2
|                             |                                                                                                                                                                                                                                                      |
|:----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Category**                | Subsurface Ocean                                                                                                                                                                                                                                     |
| **Product and version**     | ECCO2                                                                                                                                                                                                                                                |
| **Institution**             | NASA JPL                                                                                                                                                                                                                                             |
| **Product Type**            | Reanalysis                                                                                                                                                                                                                                           |
| **Spatial Resolution**      | 0.25º x 0.25º                                                                                                                                                                                                                                        |
| **Period Available**        | 1992-2013                                                                                                                                                                                                                                            |
| **Temporal Resolution**     | Monthly                                                                                                                                                                                                                                              |
| **Variables**               | <ul> <li>SST</li> <li>SSS</li> <li>S</li> <li>potential temperature</li> <li>zonal and meridional velocity</li> <li>mixed layer depth</li> <li>net surface freshwater and heat fluxes</li> <li>zonal and meridional surface winter stress</li> </ul> |
| **Reference**               | nan                                                                                                                                                                                                                                                  |
| **On CLIDEX?**              | nan                                                                                                                                                                                                                                                  |
| **Data Storage Location**   | nan                                                                                                                                                                                                                                                  |
| **Downloaded Variables**    | nan                                                                                                                                                                                                                                                  |
| **URL 1**                   | http://ecco2.jpl.nasa.gov                                                                                                                                                                                                                            |
| **URL 2**                   | nan                                                                                                                                                                                                                                                  |
| **User / point of contact** | nan                                                                                                                                                                                                                                                  |
| **Download script**         | [scripts/ecco2](scripts/ecco2)                                                                                                                                                                                                                       |
### GLORYS2v1
|                             |                                                                                                |
|:----------------------------|:-----------------------------------------------------------------------------------------------|
| **Category**                | Subsurface Ocean                                                                               |
| **Product and version**     | GLORYS2v1                                                                                      |
| **Institution**             | CNRS                                                                                           |
| **Product Type**            | Reanalysis                                                                                     |
| **Spatial Resolution**      | 0.25º x 0.25º                                                                                  |
| **Period Available**        | 1993-2017                                                                                      |
| **Temporal Resolution**     | sub-daily                                                                                      |
| **Variables**               | <ul> <li>SLA</li> <li>SST</li> </ul>                                                           |
| **Reference**               | Garric et al.                                                                                  |
| **On CLIDEX?**              | nan                                                                                            |
| **Data Storage Location**   | nan                                                                                            |
| **Downloaded Variables**    | nan                                                                                            |
| **URL 1**                   | https://www.mercator-ocean.fr/en/science-publications/glorys/                                  |
| **URL 2**                   | https://www.mercator-ocean.fr/en/science-publications/operational-systems/operational-systems/ |
| **User / point of contact** | nan                                                                                            |
| **Download script**         | [scripts/glorys2v1](scripts/glorys2v1)                                                         |
### EN4.1.1
|                             |                                          |
|:----------------------------|:-----------------------------------------|
| **Category**                | Subsurface Ocean                         |
| **Product and version**     | EN4.1.1                                  |
| **Institution**             | UK Met Office                            |
| **Product Type**            | Gridded from obs, in situ                |
| **Spatial Resolution**      | 1º x 1º                                  |
| **Period Available**        | 1900-present                             |
| **Temporal Resolution**     | Monthly                                  |
| **Variables**               | <ul> <li>S</li> <li>T</li> </ul>         |
| **Reference**               | Good et al. (2013)                       |
| **On CLIDEX?**              | nan                                      |
| **Data Storage Location**   | nan                                      |
| **Downloaded Variables**    | nan                                      |
| **URL 1**                   | https://www.metoffice.gov.uk/hadobs/en4/ |
| **URL 2**                   | nan                                      |
| **User / point of contact** | nan                                      |
| **Download script**         | [scripts/en411](scripts/en411)           |
### IAP ocean temp & OHC
|                             |                                                                                                                                   |
|:----------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| **Category**                | Subsurface Ocean                                                                                                                  |
| **Product and version**     | IAP ocean temp & OHC                                                                                                              |
| **Institution**             | IAP                                                                                                                               |
| **Product Type**            | Gridded from obs                                                                                                                  |
| **Spatial Resolution**      | 1º x 1º                                                                                                                           |
| **Period Available**        | 1940-2016                                                                                                                         |
| **Temporal Resolution**     | Monthly                                                                                                                           |
| **Variables**               | <ul> <li>T to 2000m depth</li> <li>OHC</li> </ul>                                                                                 |
| **Reference**               | Cheng et al. (2019; 2020)                                                                                                         |
| **On CLIDEX?**              | nan                                                                                                                               |
| **Data Storage Location**   | nan                                                                                                                               |
| **Downloaded Variables**    | nan                                                                                                                               |
| **URL 1**                   | https://climatedataguide.ucar.edu/climate-data/ocean-temperature-analysis-and-heat-content-estimate-institute-atmospheric-physics |
| **URL 2**                   | http://159.226.119.60/cheng/                                                                                                      |
| **User / point of contact** | nan                                                                                                                               |
| **Download script**         | [scripts/iap-ocean-temp-&-ohc](scripts/iap-ocean-temp-&-ohc)                                                                      |
### IOTA/QuOTA
|                             |                                                                                       |
|:----------------------------|:--------------------------------------------------------------------------------------|
| **Category**                | Subsurface Ocean                                                                      |
| **Product and version**     | IOTA/QuOTA                                                                            |
| **Institution**             | CSIRO                                                                                 |
| **Product Type**            | Observational                                                                         |
| **Spatial Resolution**      | 0.5º x 0.5º                                                                           |
| **Period Available**        | 1870-present                                                                          |
| **Temporal Resolution**     | ???                                                                                   |
| **Variables**               | T                                                                                     |
| **Reference**               | Gronell and Wijffels (2008)                                                           |
| **On CLIDEX?**              | nan                                                                                   |
| **Data Storage Location**   | nan                                                                                   |
| **Downloaded Variables**    | nan                                                                                   |
| **URL 1**                   | https://data.gov.au/dataset/ds-marlin-edb476bb-54fb-429a-aec5-eb97f7d5535a/details?q= |
| **URL 2**                   | nan                                                                                   |
| **User / point of contact** | nan                                                                                   |
| **Download script**         | [scripts/iota/quota](scripts/iota/quota)                                              |
### ARGO
|                             |                                              |
|:----------------------------|:---------------------------------------------|
| **Category**                | Subsurface Ocean                             |
| **Product and version**     | ARGO                                         |
| **Institution**             | nan                                          |
| **Product Type**            | Gridded from Obs, in situ                    |
| **Spatial Resolution**      | 1º x 1º                                      |
| **Period Available**        | 2000-present                                 |
| **Temporal Resolution**     | weekly, monthly                              |
| **Variables**               | <ul> <li>T</li> <li>S</li> </ul>             |
| **Reference**               | Roemmich and Gilson (2009)                   |
| **On CLIDEX?**              | nan                                          |
| **Data Storage Location**   | nan                                          |
| **Downloaded Variables**    | nan                                          |
| **URL 1**                   | http://www.argo.ucsd.edu/Gridded_fields.html |
| **URL 2**                   | http://sio-argo.ucsd.edu/RG_Climatology.html |
| **User / point of contact** | nan                                          |
| **Download script**         | [scripts/argo](scripts/argo)                 |
### ITF from IX1
|                             |                                              |
|:----------------------------|:---------------------------------------------|
| **Category**                | Subsurface Ocean                             |
| **Product and version**     | ITF from IX1                                 |
| **Institution**             | CSIRO                                        |
| **Product Type**            | In situ                                      |
| **Spatial Resolution**      | nan                                          |
| **Period Available**        | 1983-present                                 |
| **Temporal Resolution**     | monthly                                      |
| **Variables**               | <ul> <li>T</li> <li>ITF transport</li> </ul> |
| **Reference**               | Ming Feng/ Wijffels                          |
| **On CLIDEX?**              | nan                                          |
| **Data Storage Location**   | nan                                          |
| **Downloaded Variables**    | nan                                          |
| **URL 1**                   | nan                                          |
| **URL 2**                   | nan                                          |
| **User / point of contact** | nan                                          |
| **Download script**         | [scripts/itf-from-ix1](scripts/itf-from-ix1) |
### ITF Makassar
|                             |                                                                          |
|:----------------------------|:-------------------------------------------------------------------------|
| **Category**                | Subsurface Ocean                                                         |
| **Product and version**     | ITF Makassar                                                             |
| **Institution**             | LDEO?                                                                    |
| **Product Type**            | In situ                                                                  |
| **Spatial Resolution**      | nan                                                                      |
| **Period Available**        | 2004-2011, 2013-2017                                                     |
| **Temporal Resolution**     | monthly                                                                  |
| **Variables**               | <ul> <li>u and v velocities</li> <li>ITF transport</li> <li>T</li> </ul> |
| **Reference**               | Gordon et al. (2008; 2010)                                               |
| **On CLIDEX?**              | nan                                                                      |
| **Data Storage Location**   | nan                                                                      |
| **Downloaded Variables**    | nan                                                                      |
| **URL 1**                   | nan                                                                      |
| **URL 2**                   | nan                                                                      |
| **User / point of contact** | nan                                                                      |
| **Download script**         | [scripts/itf-makassar](scripts/itf-makassar)                             |
### Levitus
|                             |                                                                                                                   |
|:----------------------------|:------------------------------------------------------------------------------------------------------------------|
| **Category**                | Subsurface Ocean                                                                                                  |
| **Product and version**     | Levitus                                                                                                           |
| **Institution**             | NOAA                                                                                                              |
| **Product Type**            | Gridded from obs                                                                                                  |
| **Spatial Resolution**      | variable                                                                                                          |
| **Period Available**        | 1955-2010                                                                                                         |
| **Temporal Resolution**     | variable                                                                                                          |
| **Variables**               | <ul> <li>S</li> <li>T</li> <li>heat content</li> </ul>                                                            |
| **Reference**               | Levitus et al. (2012)                                                                                             |
| **On CLIDEX?**              | nan                                                                                                               |
| **Data Storage Location**   | /clidex/data/obs/Levitus/                                                                                         |
| **Downloaded Variables**    | heat content anomaly (0-700m), temperature anomaly (0-700m); both seasonal and yearly fields for different basins |
| **URL 1**                   | https://www.nodc.noaa.gov/OC5/3M_HEAT_CONTENT/                                                                    |
| **URL 2**                   | nan                                                                                                               |
| **User / point of contact** | nan                                                                                                               |
| **Download script**         | [scripts/levitus](scripts/levitus)                                                                                |
### Ishii Product
|                             |                                                                           |
|:----------------------------|:--------------------------------------------------------------------------|
| **Category**                | Subsurface Ocean                                                          |
| **Product and version**     | Ishii Product                                                             |
| **Institution**             | JAMSTEC                                                                   |
| **Product Type**            | Gridded from obs, in situ                                                 |
| **Spatial Resolution**      | 1º x 1º                                                                   |
| **Period Available**        | 1945-2012                                                                 |
| **Temporal Resolution**     | Monthly                                                                   |
| **Variables**               | <ul> <li>SST</li> <li>S</li> <li>T</li> <li>ocean heat content</li> </ul> |
| **Reference**               | Ishii et al. (2005; 2006)                                                 |
| **On CLIDEX?**              | nan                                                                       |
| **Data Storage Location**   | /clidex/data/obs/Ishii/                                                   |
| **Downloaded Variables**    | T                                                                         |
| **URL 1**                   | https://rda.ucar.edu/datasets/ds285.3/                                    |
| **URL 2**                   | nan                                                                       |
| **User / point of contact** | nan                                                                       |
| **Download script**         | [scripts/ishii-product](scripts/ishii-product)                            |
### PDO
|                             |                            |
|:----------------------------|:---------------------------|
| **Category**                | Climate Indices            |
| **Product and version**     | PDO                        |
| **Institution**             | nan                        |
| **Product Type**            | nan                        |
| **Spatial Resolution**      | nan                        |
| **Period Available**        | nan                        |
| **Temporal Resolution**     | nan                        |
| **Variables**               | nan                        |
| **Reference**               | nan                        |
| **On CLIDEX?**              | nan                        |
| **Data Storage Location**   | nan                        |
| **Downloaded Variables**    | nan                        |
| **URL 1**                   | nan                        |
| **URL 2**                   | nan                        |
| **User / point of contact** | nan                        |
| **Download script**         | [scripts/pdo](scripts/pdo) |
### IPO
|                             |                            |
|:----------------------------|:---------------------------|
| **Category**                | Climate Indices            |
| **Product and version**     | IPO                        |
| **Institution**             | nan                        |
| **Product Type**            | nan                        |
| **Spatial Resolution**      | nan                        |
| **Period Available**        | nan                        |
| **Temporal Resolution**     | nan                        |
| **Variables**               | nan                        |
| **Reference**               | nan                        |
| **On CLIDEX?**              | nan                        |
| **Data Storage Location**   | nan                        |
| **Downloaded Variables**    | nan                        |
| **URL 1**                   | nan                        |
| **URL 2**                   | nan                        |
| **User / point of contact** | nan                        |
| **Download script**         | [scripts/ipo](scripts/ipo) |
### Nino3.4
|                             |                                  |
|:----------------------------|:---------------------------------|
| **Category**                | Climate Indices                  |
| **Product and version**     | Nino3.4                          |
| **Institution**             | nan                              |
| **Product Type**            | nan                              |
| **Spatial Resolution**      | nan                              |
| **Period Available**        | nan                              |
| **Temporal Resolution**     | nan                              |
| **Variables**               | nan                              |
| **Reference**               | nan                              |
| **On CLIDEX?**              | nan                              |
| **Data Storage Location**   | nan                              |
| **Downloaded Variables**    | nan                              |
| **URL 1**                   | nan                              |
| **URL 2**                   | nan                              |
| **User / point of contact** | nan                              |
| **Download script**         | [scripts/nino34](scripts/nino34) |
### ONI
|                             |                            |
|:----------------------------|:---------------------------|
| **Category**                | Climate Indices            |
| **Product and version**     | ONI                        |
| **Institution**             | nan                        |
| **Product Type**            | nan                        |
| **Spatial Resolution**      | nan                        |
| **Period Available**        | nan                        |
| **Temporal Resolution**     | nan                        |
| **Variables**               | nan                        |
| **Reference**               | nan                        |
| **On CLIDEX?**              | nan                        |
| **Data Storage Location**   | nan                        |
| **Downloaded Variables**    | nan                        |
| **URL 1**                   | nan                        |
| **URL 2**                   | nan                        |
| **User / point of contact** | nan                        |
| **Download script**         | [scripts/oni](scripts/oni) |
### SAM
|                             |                            |
|:----------------------------|:---------------------------|
| **Category**                | Climate Indices            |
| **Product and version**     | SAM                        |
| **Institution**             | nan                        |
| **Product Type**            | nan                        |
| **Spatial Resolution**      | nan                        |
| **Period Available**        | nan                        |
| **Temporal Resolution**     | nan                        |
| **Variables**               | nan                        |
| **Reference**               | nan                        |
| **On CLIDEX?**              | nan                        |
| **Data Storage Location**   | nan                        |
| **Downloaded Variables**    | nan                        |
| **URL 1**                   | nan                        |
| **URL 2**                   | nan                        |
| **User / point of contact** | nan                        |
| **Download script**         | [scripts/sam](scripts/sam) |
### SOI
|                             |                            |
|:----------------------------|:---------------------------|
| **Category**                | Climate Indices            |
| **Product and version**     | SOI                        |
| **Institution**             | nan                        |
| **Product Type**            | nan                        |
| **Spatial Resolution**      | nan                        |
| **Period Available**        | nan                        |
| **Temporal Resolution**     | nan                        |
| **Variables**               | nan                        |
| **Reference**               | nan                        |
| **On CLIDEX?**              | nan                        |
| **Data Storage Location**   | nan                        |
| **Downloaded Variables**    | nan                        |
| **URL 1**                   | nan                        |
| **URL 2**                   | nan                        |
| **User / point of contact** | nan                        |
| **Download script**         | [scripts/soi](scripts/soi) |
### DMI
|                             |                            |
|:----------------------------|:---------------------------|
| **Category**                | Climate Indices            |
| **Product and version**     | DMI                        |
| **Institution**             | nan                        |
| **Product Type**            | nan                        |
| **Spatial Resolution**      | nan                        |
| **Period Available**        | nan                        |
| **Temporal Resolution**     | nan                        |
| **Variables**               | nan                        |
| **Reference**               | nan                        |
| **On CLIDEX?**              | nan                        |
| **Data Storage Location**   | nan                        |
| **Downloaded Variables**    | nan                        |
| **URL 1**                   | nan                        |
| **URL 2**                   | nan                        |
| **User / point of contact** | nan                        |
| **Download script**         | [scripts/dmi](scripts/dmi) |
### NAO
|                             |                            |
|:----------------------------|:---------------------------|
| **Category**                | Climate Indices            |
| **Product and version**     | NAO                        |
| **Institution**             | nan                        |
| **Product Type**            | nan                        |
| **Spatial Resolution**      | nan                        |
| **Period Available**        | nan                        |
| **Temporal Resolution**     | nan                        |
| **Variables**               | nan                        |
| **Reference**               | nan                        |
| **On CLIDEX?**              | nan                        |
| **Data Storage Location**   | nan                        |
| **Downloaded Variables**    | nan                        |
| **URL 1**                   | nan                        |
| **URL 2**                   | nan                        |
| **User / point of contact** | nan                        |
| **Download script**         | [scripts/nao](scripts/nao) |
### monsoon indices
|                             |                                                    |
|:----------------------------|:---------------------------------------------------|
| **Category**                | Climate Indices                                    |
| **Product and version**     | monsoon indices                                    |
| **Institution**             | nan                                                |
| **Product Type**            | nan                                                |
| **Spatial Resolution**      | nan                                                |
| **Period Available**        | nan                                                |
| **Temporal Resolution**     | nan                                                |
| **Variables**               | nan                                                |
| **Reference**               | nan                                                |
| **On CLIDEX?**              | nan                                                |
| **Data Storage Location**   | nan                                                |
| **Downloaded Variables**    | nan                                                |
| **URL 1**                   | nan                                                |
| **URL 2**                   | nan                                                |
| **User / point of contact** | nan                                                |
| **Download script**         | [scripts/monsoon-indices](scripts/monsoon-indices) |
