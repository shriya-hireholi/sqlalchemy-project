# IPL Data Analysis  

## Data

We are going to use the data of [IPL]( https://www.kaggle.com/manasgarg/ipl/version/5) provided by kaggle.
<hr>

## Language and Libraries

This project is built on Python 3.8.2 and uses standard Python libraries. Apart from that, we have also used [Highcharts](https://www.highcharts.com/) to plot charts. 
<hr>

## How to run this file

Clone this repo

Move to the folder  sqlalchemy-IPL-shriyahireholi

Create a virtual environment and activate it.

Install all dependencies

```bash
pip3 install -r requirements.txt
```

In *scripts_for_schema* under **user.py**, put down the credentials of your postgres.

Move into *scripts_for_schema* folder and run the following commands :

To create Database:
```bash  
python3 create_db.py 
```

To create Tables:
```bash  
python3 create_tables.py 
```

To insert data into Tables:
```bash  
python3 data_insertion.py 
```

For data analysis:
```bash  
python3 data_analysis.py 
```
<hr>

### Now that the Database is set,

Run python3 server:
```bash
python3 -m http.server
```
Click on the url to view the charts which will be displayed on your browser.
<hr>

### To delete the Database

```bash  
python3 delete_db.py 
```
