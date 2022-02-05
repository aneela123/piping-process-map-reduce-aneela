# piping-process-map-reduce-aneela
To learn piping process with map and reduce.

The data set contains the different countries and their gdp values in various years.
## Analysis

By using mapping, reducing and piping techniques I have first mapped and the sorted my data based on the different country names once the reducer output has generated and I have used that data in the excel sheet(in which I have got 245 rows of data where initially I had 11,500 rows) by taking those two columns i.e country name and its count and filtered the graph by selecting country name to generate a bar graph.

## Commands used:

```cat gdp.csv | python 01mapper.py > mapOutput.txt```

```cat gdp.csv | python 01mapper.py | sort | python 01reducer.py > redOutput.txt```

## Chart


![myChart](https://github.com/aneela123/piping-process-map-reduce-aneela/blob/main/Capture.PNG)
