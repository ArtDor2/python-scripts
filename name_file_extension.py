import os
import magic # pip install python-magic
from concurrent.futures import ThreadPoolExecutor, as_completed

mime_extension_mapping = {
        "message/rfc822": ".rfc822",
        "video/MP2T": ".mp2t",
        "application/x-ole-storage": ".doc",
        "application/x-wine-extension-ini": ".ini",
        "application/winhelp": ".hlp",
        "application/x-msi": ".msi",
        "image/vnd.djvu": ".djvu",
        "application/x-iso9660-image": ".iso",
        "application/x-ms-reader": ".lit",
        "application/x-mobipocket-ebook": ".mobi",
        "text/rtf": ".rtf",
        "text/xml": ".xml",
        "application/vnd.ms-htmlhelp": ".chm",
        "application/x-rar-compressed": ".rar",
        "application/x-rar": ".rar",
        "audio/aac": ".aac",
        "application/x-abiword": ".abw",
        "application/x-freearc": ".arc",
        "image/avif": ".avif",
        "video/x-msvideo": ".avi",
        "application/vnd.amazon.ebook": ".azw",
        "application/octet-stream": ".bin",  # this one is tricky, could be anything
        "image/bmp": ".bmp",
        "application/x-bzip": ".bz",
        "application/x-bzip2": ".bz2",
        "application/x-cdf": ".cda",
        "application/x-csh": ".csh",
        "text/css": ".css",
        "text/csv": ".csv",
        "application/msword": ".doc",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
        "application/vnd.ms-fontobject": ".eot",
        "application/epub+zip": ".epub",
        "application/gzip": ".gz",
        "image/gif": ".gif",
        "text/html": ".html",
        "image/vnd.microsoft.icon": ".ico",
        "text/calendar": ".ics",
        "application/java-archive": ".jar",
        "image/jpeg": ".jpeg",
        "text/javascript": ".js",
        "application/json": ".json",
        "application/ld+json": ".jsonld",
        "audio/midi": ".midi",
        "text/javascript": ".mjs",
        "audio/mpeg": ".mp3",
        "video/mp4": ".mp4",
        "video/mpeg": ".mpeg",
        "application/vnd.apple.installer+xml": ".mpkg",
        "application/vnd.oasis.opendocument.presentation": ".odp",
        "application/vnd.oasis.opendocument.spreadsheet": ".ods",
        "application/vnd.oasis.opendocument.text": ".odt",
        "audio/ogg": ".oga",
        "video/ogg": ".ogv",
        "application/ogg": ".ogx",
        "audio/opus": ".opus",
        "font/otf": ".otf",
        "image/png": ".png",
        "application/pdf": ".pdf",
        "application/x-httpd-php": ".php",
        "application/vnd.ms-powerpoint": ".ppt",
        "application/vnd.openxmlformats-officedocument.presentationml.presentation": ".pptx",
        "application/vnd.rar": ".rar",
        "application/rtf": ".rtf",
        "application/x-sh": ".sh",
        "image/svg+xml": ".svg",
        "application/x-tar": ".tar",
        "image/tiff": ".tiff",
        "video/mp2t": ".ts",
        "font/ttf": ".ttf",
        "text/plain": ".txt",
        "application/vnd.visio": ".vsd",
        "audio/wav": ".wav",
        "audio/webm": ".weba",
        "video/webm": ".webm",
        "image/webp": ".webp",
        "font/woff": ".woff",
        "font/woff2": ".woff2",
        "application/xhtml+xml": ".xhtml",
        "application/vnd.ms-excel": ".xls",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": ".xlsx",
        "application/xml": ".xml",  # this one is tricky, could be anything
        "application/vnd.mozilla.xul+xml": ".xul",
        "application/zip": ".zip",
        "video/3gpp": ".3gp",
        "video/3gpp2": ".3g2",
        "application/x-7z-compressed": ".7z",
        "application/vnd.microsoft.portable-executable": ".exe",
        "image/vnd.dwg": ".dwg",
        "application/postscript": ".ps",
        "application/x-dosexec": ".exe",
        "application/x-ndjson": ".ndjson",
        "application/vnd.hp-HPGL": ".hpgl"
    }

def get_file_extension(file_info):
    file_number, file_path = file_info
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)

    print(file_number, file_path, file_type)

    ext = mime_extension_mapping.get(file_type)
    if ext is None:
        return file_number, file_type, file_path, False
    return file_number, ext, file_path, True

def rename_file(file):
    file_number, guessed_ext, file_path, is_recognized = file

    if is_recognized:  
        new_file_path = file_path + guessed_ext
        os.rename(file_path, new_file_path)
        print(f"Renamed {file_path} to {new_file_path}")

def rename_files_without_extensions(folder_path):
    files_without_ext = []
    unrecognized_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_name, file_ext = os.path.splitext(file_path)

            if not file_ext:  # Check if the file doesn't have an extension
                files_without_ext.append(file_path)

    file_number = 1  # Initialize the file_number variable
    with ThreadPoolExecutor(max_workers=16) as executor:
        future_to_file = {executor.submit(get_file_extension, (file_number + i, file_path)): (file_number + i, file_path) for i, file_path in enumerate(files_without_ext)}

        for future in as_completed(future_to_file):
            mime_type = future.result()
            if mime_type[3]:  # check if extension is recognized
                executor.submit(rename_file, mime_type)
            else:
                unrecognized_files.append(mime_type)

        # Wait until all renaming jobs are finished before printing errors
        executor.shutdown(wait=True)

    # Print out the file paths and types for the unrecognized files
    if unrecognized_files:
        print("\nThese files had unrecognized types:")
        for file in unrecognized_files:
            print(f"File Path: {file[2]}, MIME Type: {file[1]}")

folder_path = input("/path")
rename_files_without_extensions(folder_path)
