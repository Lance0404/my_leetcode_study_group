from typing import List


def transform_date_format(dates: List[str]):
    """
    only those format:
    YYYY/MM/DD
    DD/MM/YYYY
    MM-DD-YYYY

    to 
    YYYYMMDD
    """
    def etl(date: str) -> str:
        if '/' in date:
            if len(date.split('/',1)[0]) == 4:
                return date.replace('/', '')
            else:
                tmp = date.split('/',2)
                return f'{tmp[2]}{tmp[1]}{tmp[0]}'
        elif '-' in date:
            tmp = date.split('-',2)
            return f'{tmp[2]}{tmp[0]}{tmp[1]}'
        return None
    return [etl(i) for i in dates if etl(i)]

if __name__ == "__main__":
    dates = transform_date_format(["2010/02/20", "19/12/2016", "11-18-2012", "20130720"])
    print(*dates, sep='\n')