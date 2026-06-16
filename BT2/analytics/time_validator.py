from datetime import datetime


def parse_and_inspect_date(date_str):
    try:
        upload_date = datetime.strptime(
            date_str,
            "%Y-%m-%d"
        )

        return upload_date

    except ValueError:
        print(
            f"[ERROR] Định dạng ngày upload "
            f"'{date_str}' không tồn tại"
        )

        return None