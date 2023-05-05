# climate-metadata
Metadata and download scripts for ocean/atmosphere reanalyses and observations. Note: markdown tables converted from [DataList.xlsx](https://docs.google.com/spreadsheets/d/1wIDB3dqRYOLwdLhRBvtFWuBlwpajNRG2/edit#gid=2108251210) using a [table-to-markdown converter](https://tabletomarkdown.com/convert-spreadsheet-to-markdown/). Updated markdown tables can be formatted [here](https://tabletomarkdown.com/format-markdown-table/). 


# Summary tables

## Atmosphere
| Product and version | Spatial Resolution | Temporal Resolution       | Period Available |
| ------------------- | ------------------ | ------------------------- | ---------------- |
| [20CR v2](#20cr-v2)             | 2º x 2º            | Sub-daily, daily, monthly | 1850-2014        |
| [20CR v3](#20cr-v3)             | 1º x 1º            | Sub-daily, daily, monthly | 1836-2015        |
| [ERA-20C](#era-20c)             | 1º x 1º            | Sub-daily, daily, monthly | 1900-2010        |
| [ERA-Interim](#era-interim)         | 0.75º x 0.75º      | Sub-daily, daily, monthly | 1979-2019        |
| [ERA5](#era5)       | 1º x 1º            | Sub-daily                 | 1979-present     |
| JRA-55              | 1.25º x 1.25º      | Sub-daily, monthly        | 1958-present     |
| MERRA               | 0.5º x 0.667º      | sub-daily, monthly        | 1979-2016        |
| NNR 1               | 2.5º x 2.5º        | 4-times daily, monthly    | 1948-present     |
| NNR 2               | 2.5º x 2.5º        | Sub-daily, daily, monthly | 1979-present     |
| OAFlux              | 1º x 1º            | Daily, monthly            | 1958-2012        |
| TropFlux            | ???                | Daily, monthly            | 1979-2013        |

## Wind
| Product and version       | Spatial Resolution | Temporal Resolution    | Period Available |
| ------------------------- | ------------------ | ---------------------- | ---------------- |
| CCMP Wind Vector Analysis | 0.25º x 0.25º      | sub-daily              | 1987-present     |
| IFREMER                   | 0.25º x 0.25º      | Sub-daily              | 1992-present     |
| Quikscat                  | 1º x 1º            | Daily, weekly, monthly | 1999-2009        |
| WASWind                   | 4º x 4º            | Monthly                | 1950-2011        |



## Precip
| Product and version | Spatial Resolution         | Temporal Resolution       | Period Available |
| ------------------- | -------------------------- | ------------------------- | ---------------- |
| Aphrodite           | 0.25º x 0.25º, 0.5º x 0.5º | daily                     | 1950-2007        |
| CMAP                | 2.5º x 2.5º                | mothly                    | 1979-present     |
| CMORPH              | 0.25º x 0.25º              | Sub-daily, daily          | 2002-2017        |
| CloudSat            | 2º x 2º                    | Monthly                   | 2006-2010        |
| GPCP v2.3           | 2.5º x 2.5º                | Monthly                   | 1979-present     |
| GPM IMERG           | 0.1º x 0.1º                | sub-daily, daily, monthly | 2000-present     |
| PERSIANN-CDR        | 0.25º x 0.25º              | Sub-daily, daily          | 1983-2020        |
| TRMM/GPM            | 0.25º x 0.25º              | Sub-daily, daily, monthly | 1998-2019        |



## Surface ocean
| Product and version | Spatial Resolution | Temporal Resolution | Period Available |
| ------------------- | ------------------ | ------------------- | ---------------- |
| OSCAR               | 0.33º x 0.33º      | 5 day               | 1992-present     |


## Sea surface salinity (SSS)
| Product and version | Spatial Resolution | Temporal Resolution       | Period Available |
| ------------------- | ------------------ | ------------------------- | ---------------- |
| Aquarius            | 1º x 1º            | Sub-daily, daily, monthly | 2011-2015        |
| SMAP                | 0.25º x 0.25º      | sub-daily                 | 2010-present     |
| SMOS                | 25km x 25km?       | sub-daily, daily, monthly | 2010-present     |

## Sea surface height (SSH)
| Product and version        | Spatial Resolution | Temporal Resolution | Period Available |
| -------------------------- | ------------------ | ------------------- | ---------------- |
| AVISO                      | 1º x 1º            | Monthly             | 1992-2010        |
| Global Ocean gridded SSH   | 0.25º x 0.25º      | sub-daily           | 1992-present     |
| Reconstructed Sea Level v1 | 0.5º x 0.5º        | 7-day               | 1950-2009        |

## Sea surface temperature (SST)
| Product and version | Spatial Resolution | Temporal Resolution | Period Available |
| ------------------- | ------------------ | ------------------- | ---------------- |
| ERSSTv4             | 2º x 2º            | Monthly             | 1854-present     |
| ERSSTv5             | 2º x 2º            | Monthly             | 1854-present     |
| GISTEMP             | 2º x 2º            | Monthly             | 1880-2018        |
| HadISST v1.1        | 1º x 1º            | Monthly             | 1870-present     |
| MODIS/Aqua          | 4km                | daily               | 2002-2016        |
| OISST v2            | 0.25º x 0.25º      | daily, monthly      | 1981-present     |
| OSTIA SST           | 0.05º x 0.05º      | daily               | 1992-present     |

## Subsurface ocean
| Product and version  | Spatial Resolution | Temporal Resolution | Period Available     |
| -------------------- | ------------------ | ------------------- | -------------------- |
| ARGO                 | 1º x 1º            | weekly, monthly     | 2000-present         |
| ECCO2                | 0.25º x 0.25º      | Monthly             | 1992-2013            |
| EN4.1.1              | 1º x 1º            | Monthly             | 1900-present         |
| GFDL-ECDA v3.1       | 0.33º x 1º         | Monthly             | 1961-2012            |
| GLORYS2v1            | 0.25º x 0.25º      | sub-daily           | 1993-2017            |
| GODAS                | 1º x 1º            | Monthly             | 1980-present         |
| IAP ocean temp & OHC | 1º x 1º            | Monthly             | 1940-2016            |
| IOTA/QuOTA           | 0.5º x 0.5º        | ???                 | 1870-present         |
| ITF Makassar         |                    | monthly             | 2004-2011, 2013-2017 |
| ITF from IX1         |                    | monthly             | 1983-present         |
| Ishii Product        | 1º x 1º            | Monthly             | 1945-2012            |
| Levitus              | variable           | variable            | 1955-2010            |
| ORAS4                | 1º x 1º            | Monthly             | 1958-2017            |
| ORAS5                | 1º x 1º            | Monthly             | 1979-2018            |
| SODA 2.2.4           | 0.25º x 0.4º       | Monthly             | 1871-2008            |


# Detailed metadata

### 20CR v2
|                             |                                                                      |
|-----------------------------|----------------------------------------------------------------------|
| **Product and version**     | 20CR v2                                                              |
| **Category**                | Atmospheric                                                          |
| **Institution**             | NOAA                                                                 |
| **Product Type**            | Reanalysis                                                           |
| **Spatial Resolution**      | 2º x 2º                                                              |
| **Period Available**        | 1850-2014                                                            |
| **Temporal Resolution**     | Sub-daily, daily, monthly                                            |
| **Variables**               | AirT, geopotential height, zonal/meridional wind, precipitable water |
| **Reference**               | Compo et al. (2011)                                                  |
| **On CLIDEX?**              |                                                                      |
| **Data Storage Location**   |                                                                      |
| **Downloaded Variables**    |                                                                      |
| **URL 1**                   | https://www.esrl.noaa.gov/psd/data/gridded/data.20thC_ReanV2.html    |
| **URL 2**                   |                                                                      |
| **User / point of contact** |

### 20CR v3
|                             |                                                                      |
|-----------------------------|----------------------------------------------------------------------|
| **Product and version**     | 20CR v3                                                              |
| **Category**                | Atmospheric                                                          |
| **Institution**             | NOAA                                                                 |
| **Product Type**            | Reanalysis                                                           |
| **Spatial Resolution**      | 1º x 1º                                                              |
| **Period Available**        | 1836-2015                                                            |
| **Temporal Resolution**     | Sub-daily, daily, monthly                                            |
| **Variables**               | AirT, geopotential height, zonal/meridional wind, precipitable water |
| **Reference**               | Giese et al. (2016); Slivinski et al. (2019)                         |
| **On CLIDEX?**              |                                                                      |
| **Data Storage Location**   |                                                                      |
| **Downloaded Variables**    |                                                                      |
| **URL 1**                  | https://www.esrl.noaa.gov/psd/data/gridded/data.20thC_ReanV3.html    |
| **URL 2**                   |                                                                      |
| **User / point of contact** |                                                                      |
| **Download script**         |

### ERA-20C
|                             |                                                                                                                                                                          |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Product and version**     | ERA-20C                                                                                                                                                                  |
| **Category**                | Atmospheric                                                                                                                                                              |
| **Institution**             | ECMWF                                                                                                                                                                    |
| **Product Type**            | Reanalysis                                                                                                                                                               |
| **Spatial Resolution**      | 1º x 1º                                                                                                                                                                  |
| **Period Available**        | 1900-2010                                                                                                                                                                |
| **Temporal Resolution**     | Sub-daily, daily, monthly                                                                                                                                                |
| **Variables**               | <ul> <li>Air temperature</li> <li>geopotential height</li> <li>heat flux</li> <li>humidity</li> <li>surface pressure</li> <li>surface winds</li> <li>surface roughness</li> <li>convergence</li> <li>sea level pressure</li> </ul> |
| **Reference**               | Poli et al. (2013)                                                                                                                                                       |
| **On CLIDEX?**              |                                                                                                                                                                          |
| **Data Storage Location**   |                                                                                                                                                                          |
| **Downloaded Variables**    |                                                                                                                                                                          |
| **URL 1**                   | https://rda.ucar.edu/datasets/ds626.0/                                                                                                                                   |
| **URL 2**                   |                                                                                                                                                                          |
| **User / point of contact** |                                                                                                                                                                          |
| **Download script**         |


### ERA-Interim
|                             |                                                                                                                                                |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Product and version**     | ERA-Interim                                                                                                                                    |
| **Category**                | Atmospheric                                                                                                                                    |
| **Institution**             | ECMWF                                                                                                                                          |
| **Product Type**            | Reanalysis                                                                                                                                     |
| **Spatial Resolution**      | 0.75º x 0.75º                                                                                                                                  |
| **Period Available**        | 1979-2019                                                                                                                                      |
| **Temporal Resolution**     | Sub-daily, daily, monthly                                                                                                                      |
| **Variables**               | <ul> <li>AirT</li> <li>geopotential height</li> <li>precipitable water</li> <li>precip</li> <li>wind</li> <li>E-P</li> <li>humidity</li> <li>surface pressure</li> <li>water vapor flux</li> <li>cloud liquid/frozen water flux</li> </ul> |
| **Reference**               | Dee et al. (2008; 2011; 2014)                                                                                                                  |
| **On CLIDEX?**              | Y                                                                                                                                              |
| **Data Storage Location**   | /climodes/data7/datasets/ERA-int/WAM_moisture_tracking_data                                                                                    |
| **Downloaded Variables**    |                                                                                                                                                |
| **URL 1**                   | https://www.ecmwf.int/en/research/climate-reanalysis/era-interim                                                                               |
| **URL 2**                   |                                                                                                                                                |
| **User / point of contact** |                                                                                                                                                |
| **Download script**         |




### ERA5
|                             |                                                                                                                                                      |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Product and version**     | ERA5                                                                                                                                                 |
| **Category**                | Atmospheric                                                                                                                                          |
| **Institution**             | ECMWF                                                                                                                                                |
| **Product Type**            | Reanalysis                                                                                                                                           |
| **Spatial Resolution**      | 1º x 1º                                                                                                                                              |
| **Period Available**        | 1979-present                                                                                                                                         |
| **Temporal Resolution**     | Sub-daily                                                                                                                                            |
| **Variables**               | <ul> <li>wind & specific humidity (pressure-level)</li> <li>evaporation, precipitation</li> <li>surface pressure</li> <li>precipitable water</li> <li>liquid/frozen water fluxes</li> </ul> |
| **Reference**               |                                                                                                                                                      |
| **On CLIDEX?**              | Y                                                                                                                                                    |
| **Data Storage Location**   | /clidex/data/reanalysis/era5/                                                                                                                        |
| **Downloaded Variables**    |                                                                                                                                                      |
| **URL 1**                   |                                                                                                                                                      |
| **URL 2**                   |                                                                                                                                                      |
| **User / point of contact** | Mariya                                                                                                                                               |
| **Download script**         | [scripts/era5](scripts/era5)



