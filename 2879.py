# URL: https://leetcode.com/problems/display-the-first-three-rows/                        
# TITLE: Display the First Three Rows                            
# DIFFICULTY: Easy                                
# ------------------------------------------------------
import pandas as pd
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)


# ------------------------------------------------------
import pandas as pd
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[:3]