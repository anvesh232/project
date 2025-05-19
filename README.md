# project
Dashboard link: https://project-92e2vs9cfj5qub8zy2skmb.streamlit.app/
Overview
This project has been an enlightening journey, spanning a mere three weeks, yet packed with invaluable learning experiences. Initially daunting, I found myself staring at the CPS (Current Population Survey) data variables for days, overwhelmed and unsure where to begin. However, as I gradually delved into understanding each variable's description, the fog began to lift, and I started to experiment with the API.

Data Collection
The journey of data collection was both illuminating and challenging. Initially, I wrote code to explore API responses, identifying gaps in data coverage across different states and months. It became apparent that several states lacked substantial data, potentially leaving out critical insights, with more than four or five metropolitan areas void of substantial data.

Moreover, I encountered occasional API response issues, where the service would temporarily cease to function correctly. To mitigate this, I opted to collect data year by year, ultimately amassing a sizable 600 MB dataset.

Data Compression and Hosting
Hosting such a large dataset posed a significant challenge, with platforms like Google, Kaggle, and GitHub unable to support direct access to raw files of such magnitude. Inspired by an ingenious suggestion, I embarked on compressing the dataset based on CBSA (Core Based Statistical Area) and year, effectively reducing its size to a mere 2 MB. Additionally, I integrated latitude and longitude values using the Google API for potential future use.

Visualization
Visualization marked a pivotal stage in the project, where I transitioned from individual plot exploration in Google Colab to the development of a comprehensive dashboard using Streamlit. While initially encountering hurdles, such as numpy build errors, meticulous version management and local environment replication resolved these issues.

The resulting dashboard offers users the flexibility to specify the year and CBSA, generating corresponding graphs alongside a US map pinpointing all metropolitan areas. Though attempts to implement a map-based selection feature were unsuccessful, they represent valuable learning experiences for future endeavors.

GitHub Integration and Automation
The project culminated in the establishment of an automated pipeline, ensuring seamless updates to both the dataset and Streamlit dashboard. Leveraging a combination of Python scripts and GitHub workflows, I orchestrated the periodic execution of data retrieval, compression, and dashboard updates, fostering a dynamic and evolving platform.

Future Improvements
Reflecting on this project, there are several areas I would approach differently in the future. Firstly, I acknowledge the importance of thorough code review and validation before embarking on resource-intensive processes, minimizing potential setbacks and optimizing efficiency. Additionally, I recognize the need for proactive monitoring of platform traffic, ensuring optimal performance during critical stages of development.
