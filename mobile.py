from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
import time
import random

# 关键词列表（100个）
keywords = [
    "Python programming", "AI technology", "Machine learning", "Data science", "Web development",
    "Cloud computing", "Cybersecurity", "Blockchain", "Quantum computing", "Big data",
    "Artificial intelligence", "Deep learning", "Software engineering", "DevOps", "Mobile apps",
    "Game development", "Network security", "Database management", "API integration", "Microservices",
    "Computer vision", "Natural language processing", "Robotics", "IoT devices", "5G technology",
    "Augmented reality", "Virtual reality", "Edge computing", "Serverless architecture", "Fintech",
    "Cryptocurrency", "Digital transformation", "Agile methodology", "Selenium automation", "Bing rewards",
    "Cloud security", "Web3", "Data analytics", "Neural networks", "Kubernetes", "Docker containers",
    "Cybersecurity trends", "Generative AI", "Low-code platforms", "Quantum cryptography",
    "Latest movies 2025", "Music streaming services", "Top Netflix shows", "Hollywood news",
    "Video game releases", "Pop culture trends", "Celebrity interviews", "Anime recommendations",
    "Streaming platforms comparison", "Oscar predictions 2025", "K-pop trends", "Virtual concerts",
    "Football highlights", "Basketball NBA news", "Olympics 2024 updates", "Tennis rankings",
    "Soccer World Cup", "Sports betting trends", "Fitness training tips", "Marathon training",
    "Healthy recipes", "Sustainable living", "Minimalist lifestyle", "Travel destinations 2025",
    "Home decor ideas", "Personal finance tips", "Mental health awareness", "Yoga benefits",
    "Vegan diet plans", "DIY home projects", "Eco-friendly products", "Budget travel tips",
    "Global news today", "Climate change updates", "Economic trends 2025", "International politics",
    "Tech industry news", "Stock market analysis", "World health organization updates",
    "Renewable energy trends", "Geopolitical events", "Space exploration news",
    "Online learning platforms", "Free coding tutorials", "Language learning apps",
    "STEM education trends", "Virtual classrooms", "Best universities 2025",
    "Weather forecast", "Local events near me", "Photography tips", "Pet care advice",
    "Gardening tips", "Electric vehicles 2025", "Smart home devices", "Fashion trends 2025",
    "Food delivery apps", "Virtual reality gaming", "Productivity tools", "Remote work tips",
    "Cryptocurrency prices", "Artificial intelligence ethics", "Space tourism", "Fitness trackers"
]

# 设置 Edge 浏览器选项，模拟移动设备
options = webdriver.EdgeOptions()
mobile_user_agent = (
    "Mozilla/5.0 (Linux; Android 14; Pixel 6 Build/AP2A.240605.024) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 Edge/121.0.2277.138"
)
options.add_argument(f"user-agent={mobile_user_agent}")
# 如果需要无界面运行，取消注释以下行
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("mobileEmulation", {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": mobile_user_agent
})

# 自动下载并使用 Edge WebDriver
driver_path = "msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=options)


def simulate_human_scroll():
    """模拟人类的滚动行为"""
    try:
        # 获取页面高度
        page_height = driver.execute_script("return document.body.scrollHeight")
        # 随机滚动次数（1-3次）
        scroll_times = random.randint(1, 3)
        current_position = 0

        for _ in range(scroll_times):
            # 随机滚动距离（50-300像素，适合移动端页面）
            scroll_distance = random.randint(50, 300)
            # 确保不超出页面高度
            if current_position + scroll_distance < page_height:
                driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
                current_position += scroll_distance
            else:
                # 如果接近页面底部，滚动到末尾
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                break
            # 模拟人类阅读的随机停顿（0.5-2秒）
            time.sleep(random.uniform(0.5, 2))
    except Exception as e:
        print(f"滚动时发生错误: {e}")


def bing_search(query):
    try:
        driver.get("https://www.bing.com")
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sb_form_q"))
        )
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        # 等待搜索结果加载
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2 a"))
        )
        # 模拟滚动行为
        simulate_human_scroll()
        # 额外延迟，模拟浏览时间
        time.sleep(random.uniform(2, 6))
    except Exception as e:
        print(f"搜索 {query} 时发生错误: {e}")


def main():
    try:
        # 打开 Bing 登录页面（如果需要手动登录，取消注释以下代码）
        # driver.get("https://login.live.com")
        # print("请手动登录 Microsoft 账户，然后按 Enter 继续...")
        # input()

        # 执行23次移动端搜索
        for i in range(30):
            keyword = random.choice(keywords)
            print(f"执行第 {i + 1} 次移动端搜索: {keyword}")
            bing_search(keyword)

        print("已完成23次移动端搜索！")

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()