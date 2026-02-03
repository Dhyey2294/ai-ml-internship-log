import os
from icrawler.builtin import BingImageCrawler

BASE_PATH = "Dataset/food_final_selected"

SEARCHES = {
    "dal": ["dal curry indian food", "dal fry dish", "dal tadka bowl"],
    "roti": ["roti chapati indian bread", "fresh roti tawa", "chapati plate"],
    "plain_rice": ["plain rice bowl", "steamed white rice plate"],
    "dosa": ["masala dosa south indian", "crispy dosa restaurant"],
    "idli": ["idli sambar chutney plate"],
    "rajma": ["rajma curry bowl", "rajma chawal plate"],
    "pav_bhaji": ["pav bhaji street food", "butter pav bhaji plate"],

    "guava": ["guava fruit fresh"],
    "papaya": ["papaya fruit slices"],
    "orange": ["orange fruit citrus"],
    "pear": ["pear fruit fresh"],

    "carrot": ["carrot vegetable fresh"],
    "spinach": ["spinach leaves fresh"],
    "cabbage": ["cabbage vegetable whole"],
}

def crawl():
    for cls, queries in SEARCHES.items():
        save_dir = os.path.join(BASE_PATH, cls)
        os.makedirs(save_dir, exist_ok=True)

        crawler = BingImageCrawler(storage={'root_dir': save_dir})

        for q in queries:
            print(f"{cls} → {q}")
            crawler.crawl(keyword=q, max_num=120)

if __name__ == "__main__":
    crawl()
