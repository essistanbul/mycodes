import sqlite3 import os from bing_image_downloader.downloader import download from PIL import Image
klasor_adi = "resim_klasoru" db_adi = "resimler.sqlite3"
if not os.path.exists(klasor_adi): os.makedirs(klasor_adi)
db_yolu = os.path.join(klasor_adi, db_adi) conn = sqlite3.connect(db_yolu) cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS resimler (dosya_adi TEXT, dosya_yolu TEXT, genislik INTEGER, yukseklik INTEGER)")
def download_images_with_size_criteria(search_term, limit, timeout, min_width, min_height, max_width, max_height):
Plain Text
print(f"{search_term} terimiyle ilgili resimler indiriliyor... Lütfen bekleyin.")
downloader_args = {
    "limit": limit,
    "output_dir": "indirilen_resimler",
    "adult_filter_off": True,
    "force_replace": False,
    "timeout": timeout,
    "verbose": True,
}
download(search_term, **downloader_args)
read_image_info_and_insert_into_db(os.path.join("indirilen_resimler", search_term), min_width, min_height, max_width, max_height)