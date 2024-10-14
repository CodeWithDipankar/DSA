from typing import List
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ["student_id","age"])

if __name__ == "__main__":
    student = [
                [1, 15],
                [2, 11],
                [3, 11],
                [4, 20]
                ]
    createDataframe(student)