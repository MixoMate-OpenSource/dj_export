from django.db.models.query import QuerySet
import polars as pl

class ExcelExport:
    @classmethod
    def export_config(cls, queryset: QuerySet, filename: str):
        # Your configuration logic here
        pass

    @classmethod
    def export(cls, queryset: QuerySet, filename: str):
        data = list(queryset.values())
        df = pl.DataFrame(data)
        df.write_excel(filename, fmt='xlsx')

class CSVExport:
    @classmethod
    def export_config(cls, queryset: QuerySet, filename: str):
        # Your configuration logic here
        pass

    @classmethod
    def export(cls, queryset: QuerySet, filename: str):
        data = list(queryset.values())
        df = pl.DataFrame(data)
        df.write_csv(filename)