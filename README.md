# Review of Low-Voltage Load Forecasting

This is the repository for the Github pages site produced with [Jekyll](https://jekyllrb.com/) to [our page](https://low-voltage-loadforecasting.github.io/) hosting an overview of load forecasting data sets as presented in our [preprint on arXiv](). 

## How To Contribute a dataset

### Submit by opening an issue
The easiest way to contribute is to use the issue functionality of Github. For that switch into the tab "Issues" above. Then click "New Issue". Optionally add the label "dataset". Then provide as much as possible from the following information:
- **Name**: A short name that can be referenced
- **Url**: Link to where the dataset is hosted or can be requested
- **Type**: Should be one or several of "Residential", "Commercial", "Industrial", "Other", "Substation"
- **No.Customers**: Number of entitites in the dataset (e.g., number of households, number of substations)
- **Resolution**: Resolution in minutes, seconds or kHz
- **Duration**: What is the typical duration of data available in days, weeks or months
- **Intervention**: If an intervention like Time-of-Use or dynamic prices was part of the measurement campaign
- **Sub-metering**: If there is any hierarchy in the dataset (e.g. households belonging to same substation, or measurements within the household)
- **Weather avail.**: If there is weather data available
- **Location**: Country and possibly city or Region
- **Other data provided**: If there is other measurements belonging to the dataset besides load.
- **Access/Licence**: The licence (if any)

Many datasets ask for (or require) attribution of a certain paper. If so, provide it's bibliographic information. Ideally, provide a bibtex entry or simply list the information required (see [here](https://de.overleaf.com/learn/latex/Bibliography_management_with_bibtex#The_bibliography_file) for example bibtex entries). 

See issue #2 as an example.

### Submit via pull request

## Any Ideas or Feedback?
We know, this is yet another list of datasets out there. We believe it is a useful resource and providing a way to keep it up-to-date beyond the paper adds value. If you have any idea on how this could be improved, for instance by adding more structure to the data for a better meta-review. If you have any ideas, either open an issue for discussion or contact [us](mailto:mail@marcusvoss.com).
