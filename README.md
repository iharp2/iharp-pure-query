# iharp-pure-query

HTML preview: https://html-preview.github.io/?url=https://github.com/iharp2/iharp-pure-query/blob/main/src/example.html

Run `init_venv.sh` to initialize virtual environment and install packages. 
```bash
bash init_venv.sh
```

To run the query examples, open jupyter notebook `src/example.ipynb` and run all cells. 

To run tests, run `pytest` in terminal. 
```bash
pytest
```

## Roadmap

| Query                              |    Single File     |    Multi Files     | Files + API | pre-aggregation | pre-aggregation + API |
| ---------------------------------- | :----------------: | :----------------: | :---------: | :-------------: | :-------------------: |
| single value aggregation           | :white_check_mark: | :white_check_mark: |             |                 |                       |
| time series aggregation            | :white_check_mark: | :white_check_mark: |             |                 |                       |
| heatmap aggregation (single layer) | :white_check_mark: | :white_check_mark: |             |                 |                       |
| heatmap aggregation (multi layer)  | :white_check_mark: | :white_check_mark: |             |                 |                       |
| value-criteria query               | :white_check_mark: | :white_check_mark: |             |                 |                       |
| arbitrary shape query              | :white_check_mark: | :white_check_mark: |             |                 |                       |
| time period finding                | :white_check_mark: | :white_check_mark: |             |                 |                       |
| area finding                       | :white_check_mark: | :white_check_mark: |             |                 |                       |

## Example

| Query                                                                                                                                         |                 Example                  |
| --------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------: |
| single value aggregation (average temperature in the area during the period of time)                                                          |  ![](screenshots/single_value_agg.png)   |
| time series aggregation (daily average temperature in the area during the period of time)                                                     |     ![](screenshots/time_series.png)     |
| heatmap aggregation (single layer) (max temperature for the box area during the period of time)                                               |   ![](screenshots/heatmap(single).png)   |
| heatmap aggregation (multi layer) (temperature in the area (at 2degree * 2degree resolution) during the period of time (at daily resolution)) |   ![](screenshots/heatmap(multi).png)    |
| value-criteria query (max temperature in the area during the period of time , where daily max temperature < 255)                              |   ![](screenshots/value_criteria.png)    |
| arbitrary shape query (temperature on Greenland)                                                                                              |   ![](screenshots/arbitrary_shape.png)   |
| time period finding (find the days where where all pixels' temperature < 282)                                                                 | ![](screenshots/time_period_finding.png) |
| area finding ( find the area where every day's temperature < 255)                                                                             |    ![](screenshots/area_finding.png)     |
