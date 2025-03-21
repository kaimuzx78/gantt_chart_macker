# Gantt Chart Maker

A simple tool to generate Gantt charts from a `.txt` file using Python and Tkinter.

## Developed by: Kaimu 

## Installation

<b>pip install matplotlib pandas</b><br>
Make sure you have Python installed, then install the required dependencies:


## How to Run

1. Run the script:

2. Upload a `.txt` file containing project data when prompted.

## Upload Raw Data (.txt file)
## Note : Do not Upload the Same data file Make Chages in Date and table Then uplaod

1. Open Notepad and enter data in the following format.
2. Save the file as `data.txt`.
3. Run `main.py` and upload your `.txt` file.
4. The program will generate a Gantt chart.

### Example Data Format:

Sr No Task Name Duration (D.
ys) Start Date Finish Date 1 Project topic deciding 3 28-06-2024 01-07-2024 2 Collecting data 3 03-07-2024 06-07-2024 3 Problem Definition 5 05-07-2024 16-07-2024 4 System design 11 17-08-2024 28-08-2024 5 Problem evaluation 4 01-09-2024 05-09-2024 6 Define function and behaviour 11 10-09-2024 21-09-2024 7 Requirement analysis 15 25-09-2024 10-10-2024 8 Implementation and coding 35 27-10-2024 05-12-2024 9 Unit testing 28 05-12-2024 02-01-2025 10 Integration and Validation 35 03-01-2025 07-02-2025 11 System testing 10 10-02-2025 20-02-2025


## Example Input File:

![Example Data](https://github.com/user-attachments/assets/b42ee838-8f2b-4151-a7d1-e4eaf3de146f)

## Notepad Example
![image](https://github.com/user-attachments/assets/74ca0390-2e12-4df5-9884-4022a7580638)

## Output

Once the file is uploaded, the tool will generate a Gantt chart like this:

![Gantt Chart Output](https://github.com/user-attachments/assets/7f79ddc6-acc6-4fc9-b871-d37eb59e8226)

## Features

- Simple UI with file upload functionality
- Reads tab-separated data files
- Generates a clear, visually appealing Gantt chart
- Uses Matplotlib for visualization
