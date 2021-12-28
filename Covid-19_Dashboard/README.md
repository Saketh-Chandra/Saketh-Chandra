![Covid-19 png](https://www.leaders-in-law.com/wp-content/uploads/2020/03/COVID-19.png)

## :bulb: This is a subproject of [Covid-19_website](https://github.com/Saketh-Chandra/Covid-19_website)

### Covid-19 Dashboard
[![COVID-19_Dashboard](https://github.com/Saketh-Chandra/Saketh-Chandra/actions/workflows/Main_Covid-19_Dashboard.yml/badge.svg)](https://github.com/Saketh-Chandra/Saketh-Chandra/actions/workflows/Main_Covid-19_Dashboard.yml)

<!--img src="https://raw.githubusercontent.com/Saketh-Chandra/Saketh-Chandra/master/Covid-19_Dashboard/Covid-19.svg" /-->
[![Covid-19 India](https://raw.githubusercontent.com/Saketh-Chandra/Saketh-Chandra/master/Covid-19_Dashboard/Covid-19.svg)](https://raw.githubusercontent.com/Saketh-Chandra/Saketh-Chandra/master/Covid-19_Dashboard/Covid-19.svg)
#### *This will automatically update every 12 hours using GitHub's actions.


### Wear a mask 😷. Help slow the spread of COVID-19

## Data Source for the project:
The data source for our project is provided by the Center for Systems Science and Engineering
(CSSE) at Johns Hopkins University. The main reason for obtaining the data from them is they
provide the data for free of cost and they also provide authenticated data source as they pool the
information regarding the number of COVID-19 cases registered, number of recoveries, number
of deaths from authenticated and reliable sources like World Health Organization (WHO),
European Centre for Disease Prevention and Control (ECDC) etc. 
## [Thanks for CSSEGISandData for providing COVID-19 Data Repository](https://github.com/CSSEGISandData/COVID-19)

#### GitHub Actions: [Main_Covid-19_Dashboard.yml](https://github.com/Saketh-Chandra/Saketh-Chandra/blob/master/.github/workflows/Main_Covid-19_Dashboard.yml) file

```yml
name: COVID-19_Dashboard

on:
  schedule:
    - cron: '0 */12 * * *' # Runs at 00:00 and 12:00 UTC every day.
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:

      - name: checkout repo content
        uses: actions/checkout@v2 # checkout the repository content to github runner

      - name: setup python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8.11' # install the python version needed
          
      - name: install python packages
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          
      - name: execute main.py # run main.py <Country> <State>
        run: python Covid-19_Dashboard/main.py India
          
      - name: commit files
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add -A
          git commit -m "update Covid-19_Dashboard" -a
          
      - name: push changes
        uses: ad-m/github-push-action@v0.6.0
        with:
          github_token: ${{ secrets._TOKEN }}
          branch: master 
```
