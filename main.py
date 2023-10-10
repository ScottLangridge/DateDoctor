import datetime
import os.path

import piexif


def main(root_timestamp, reverse=False):
    foldername = 'photos'

    file_list = sorted(os.listdir(foldername))
    if reverse:
        file_list.reverse()

    for filename in file_list:
        new_timestamp_str = root_timestamp.strftime('%Y:%m:%d %H:%M:%S')
        update_metadata_timestamps(os.path.join(foldername, filename), new_timestamp_str)
        root_timestamp += datetime.timedelta(minutes=1)


def get_first_timestamp(filename):
    try:
        exif_dict = piexif.load(filename)
        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_timestamp_str
        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_timestamp_str
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, filename)

    except Exception as e:
        print(f"Error updating timestamps: {e}")


def update_metadata_timestamps(filename, new_timestamp_str):
    try:
        exif_dict = piexif.load(filename)
        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_timestamp_str
        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_timestamp_str
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, filename)

    except Exception as e:
        print(f"Error updating timestamps: {e}")


main(datetime.datetime(2023, 9, 21, 3, 0, 0), False)
