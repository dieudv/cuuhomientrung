import json
import pandas
from app.utils import temporary_files

REQUIRED_COLUMN_HEADERS = ['Tên hộ dân', 'Tình trạng', 'Vị trí', 'Tỉnh',
                           'Xã', 'Huyện', 'Sdt', 'Cứu hộ', 'Thời gian cuối cùng cập nhật', 'Ghi chú']


def validate_import_table(name):
    df = pandas.read_excel(temporary_files.name_to_path(name))
    headers = list(df)
    return set(REQUIRED_COLUMN_HEADERS).issubset(set(headers))


def get_json_from_table(name):
    df = pandas.read_excel(temporary_files.name_to_path(name))
    records = df.to_dict('records')
    return json.dumps(records)
