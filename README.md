# Review of Low-Voltage Load Forecasting

This is the repository for the Github pages site produced with [Jekyll](https://jekyllrb.com/) to [our page](https://low-voltage-loadforecasting.github.io/) hosting an overview of load forecasting data sets as presented in our paper available as [preprint on arXiv](https://arxiv.org/pdf/2106.00006.pdf) and published in [Applied Energy](https://www.sciencedirect.com/science/article/pii/S0306261921011326).

## How To Contribute a dataset

### Submit by opening an issue
The easiest way to contribute is to use the issue functionality of Github. For that switch into the tab "Issues" above. Then click "New Issue". Optionally add the label "dataset". Then provide as much as possible from the following information:
- **Name**: A short name that can be referenced
- **Url**: Link to where the dataset is hosted or can be requested
- **Type**: Should be one or several of "Residential", "Commercial", "Industrial", "Other", "Substation"
- **Customers**: Number of entitites in the dataset (e.g., number of households, number of substations)
- **Resolution**: Resolution in minutes, seconds or kHz
- **Duration**: What is the typical duration of data available in days, weeks or months
- **Intervention**: If an intervention like Time-of-Use or dynamic prices was part of the measurement campaign
- **Submetering**: Yes/No If there is any hierarchy in the dataset (e.g. households belonging to same substation, or measurements within the household)
- **Weather**: Yes/No If there is weather data available
- **Location**: Country and possibly city or Region
- **Other**: If there is other measurements belonging to the dataset besides load.
- **Licence**: The licence (if any)

Many datasets ask for (or require) attribution of a certain paper. If so, provide it's bibliographic information. Ideally, provide a bibtex entry or simply list the information required (see [here](https://de.overleaf.com/learn/latex/Bibliography_management_with_bibtex#The_bibliography_file) for example bibtex entries). 

See [this issue](https://github.com/low-voltage-loadforecasting/low-voltage-loadforecasting.github.io/issues/2) as an example.

### Submit via pull request

You can also add a paper yourself and add it to the repository as a pull request. This repository has two branches. The code hosted in branch 'source' and the static page hosted in 'gh-pages' which will automatically be deployed by Github to the page. So to add a dataset, follow the following steps:
- Checkout the 'source' branch
- Make your changes locally and test them (requires [Jekyll](https://jekyllrb.com/)), for testing run: `bundle exec jekyll serve`
- Build the page locally, run `bundle exec jekyll build`, which creates the sources in folder '_site'
- Commit (and push) the changes to the source branch
- Now to publish the web site by only pushing the '_site' subfolder to the branch 'gh-pages': `git subtree push --prefix _site origin gh-pages`

## Any Ideas or Feedback?
We know, this is yet another list of datasets out there. We believe it is a useful resource and providing a way to keep it up-to-date beyond the paper adds value. If you have any idea on how this could be improved or have other ideas, either open an issue for discussion or contact [us](mailto:mail@marcusvoss.com). It serves currently the purpose of manual exploration and there was no focus on properly standardizing and harmonizing that data source in the YAML.

## Other lists of datasets
- ACM Special Interest Group on Energy Systems and Informatics: https://bwdatadiss.kit.edu/dataset/184#headingFileList
- Climate Change AI Wiki page on Electricity Systems: https://wiki.climatechange.ai/wiki/Electricity_Systems
- List of NILM datasets by Oliver Parson: https://blog.oliverparson.co.uk/2012/06/public-data-sets-for-nialm.html
- List compiled by Miha Grabner: https://www.mihagrabner.com/resources
- List in Paper "A Comprehensive Review of Residential Electricity Load Profile Models", https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9316723
- List of HTW Berlin: https://pvspeicher.htw-berlin.de/veroeffentlichungen/daten/
