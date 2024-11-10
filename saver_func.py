"""Saver function"""

from typing import Union
import pandas as pd


class SaveData:
    counter = 0

    def __init__(self):
        try:
            with open("save_log.csv", "x") as f:
                f.write("name,time,mem_address\n")
        except:
            pass

    @classmethod
    def save(cls, val: Union[pd.DataFrame, pd.Series], suffix: str = ""):
        """Save a pandas DataFrame or Series to a csv file.

        Args:
            val (Union[pd.DataFrame, pd.Series]): The DataFrame or Series to save.
            name (str, optional): Optional suffix for the file. Defaults to "".
        """
        assert isinstance(
            val, (pd.DataFrame, pd.Series)
        ), "val must be a DataFrame or Series"

        if isinstance(val, pd.Series):
            val = val.to_frame()

        file_name = f"save_{cls.counter}{'_' + suffix if suffix else ''}"
        val.to_html(file_name + ".html")
        with open("save_log.csv", "a") as f:
            f.write(f"{file_name}, {pd.Timestamp.now()}, {hex(id(val))}\n")
        cls.counter += 1
