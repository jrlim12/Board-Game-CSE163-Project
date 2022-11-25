# Board-Game-Analyzer-CSE163-Project

# How to Run Our Board Game Project

## Libraries to install before running code
1: pandas: To install pandas, type "pip install pandas"
into the terminal.

2: plotly: To install plotly, type "$ pip install plotly==5.8.0" into the terminal.

3: Scikit(or sklearn): To install sklearn, type
"pip install -U scikit-learn" into the terminal.

## Downloading datasets used for code
1: Larxel Dataset: download "The Larxel BGG Dataset" included with the submitted files.

2: Pantherson Dataset: download "Pantherson Dataset include with the submitted files.

**Note: Make sure to change the paths of the two files to the appropriate path of your own computer!**

*For example, change these two variable paths specifically:*

        DATASET_1 = pd.read_csv(
        r'C:/Users/jrlim/Documents/UW/2021-2022/CSE 163/VS Projects'
        r'/final project board game/The_Larxel_BBG_Dataset.csv',
        encoding='unicode_escape')
        
        DATASET_2 = pd.read_csv(
        r'C:/Users/jrlim/Documents/UW/2021-2022/CSE 163/VS Projects'
        r'/final project board game/Pantherson_Data_Set.csv',
        encoding='unicode_escape')

**If any other issues may arise, make sure that you are correctly importing all libraries and no spelling errors are found anywhere within your code!**
