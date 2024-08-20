from django.db.models.query import QuerySet
import polars as pl
from openpyxl import Workbook

class BaseExportClass:
    @classmethod
    def apply_config(cls, queryset: QuerySet, filename: str):
        # Your configuration logic here
        cls.manage_seetname()

    @classmethod
    def manage_seetname(cls, wb: Workbook, sheet_config:dict):
        # manager sheet related actions here form config part
        pass


class ExcelExport(BaseExportClass):
    @classmethod
    def export(cls, queryset: QuerySet, filename: str):
        data = list(queryset.values())
        df = pl.DataFrame(data)
        df.write_excel(filename, fmt='xlsx')
        cls.apply_config()


class CSVExport(BaseExportClass):
    
    @classmethod
    def export(cls, queryset: QuerySet, filename: str):
        data = list(queryset.values())
        df = pl.DataFrame(data)
        df.write_csv(filename)
        cls.apply_config()
