from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
import time
import random
pc_num = 40

# 关键词列表（100个，风格偏日常搜索场景）
keywords = [
    # 购物相关
    "Best laptops 2025", "Smartphone deals", "Fashion trends women", "Online shopping discounts",
    "Gaming console prices", "Home appliance reviews", "Sneaker brands", "Luxury watches",
    "Budget headphones", "Furniture sales", "Electronics deals", "Black Friday 2025",
    "Amazon best sellers", "Tech gadgets 2025", "Winter clothing trends", "Jewelry gift ideas",

    # 旅游与生活
    "Top travel destinations", "Cheap flights 2025", "Hotel booking tips", "Beach vacation ideas",
    "City break Europe", "Adventure travel packages", "Cruise deals 2025", "Travel insurance comparison",
    "Camping gear reviews", "Best hiking trails", "Family vacation spots", "Solo travel tips",
    "Backpacking destinations", "Luxury resorts Asia", "Travel safety tips", "Road trip ideas",

    # 新闻与时事
    "Breaking news today", "World news updates", "US election 2025", "Global economy trends",
    "Climate change solutions", "Political debates 2025", "International conflicts", "Tech industry updates",
    "Stock market predictions", "Health policy news", "Space mission updates", "Energy crisis 2025",

    # 学术与教育
    "Online courses free", "Best coding bootcamps", "Study abroad programs", "Scholarship opportunities",
    "Academic research tools", "Math learning apps", "History documentaries", "Science podcasts",
    "University rankings 2025", "Career training programs", "Language learning tips", "STEM resources",

    # 健康与健身
    "Weight loss diets", "Home workout routines", "Mental health tips", "Meditation apps",
    "Healthy meal plans", "Fitness equipment reviews", "Yoga for beginners", "Nutrition supplements",
    "Running shoes reviews", "Stress management techniques", "Sleep improvement tips", "Vegan recipes easy",

    # 娱乐与文化
    "New movie releases", "TV show reviews 2025", "Music festivals 2025", "Book recommendations",
    "Streaming service deals", "Celebrity news today", "Top video games 2025", "Art exhibitions",
    "Theater shows 2025", "Pop music charts", "Comedy specials Netflix", "Cultural events near me",

    # 科技与创新
    "Smart home devices 2025", "Wearable tech reviews", "Electric car prices", "AI innovations",
    "5G network updates", "Virtual reality headsets", "Drone technology", "Cybersecurity tips",
    "Tech startups 2025", "Cloud storage comparison", "Programming tutorials", "Data privacy laws",

    # 其他日常搜索
    "Local weather forecast", "Event planning ideas", "DIY craft projects", "Pet adoption near me",
    "Gardening for beginners", "Car maintenance tips", "Home renovation ideas", "Wedding planning guide",
    "Photography gear reviews", "Best coffee machines", "Restaurant reviews near me", "Online grocery delivery",
    "Real estate trends 2025", "Job search websites", "Personal finance apps", "Charity organizations"
]

# 设置 Edge 浏览器选项（电脑端，无移动端模拟）
options = webdriver.EdgeOptions()
# 如果需要无界面运行，取消注释以下行
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 自动下载并使用 Edge WebDriver
driver_path = "msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=options)


def simulate_human_scroll():
    """模拟人类的滚动行为"""
    try:
        # 获取页面高度
        page_height = driver.execute_script("return document.body.scrollHeight")
        # 随机滚动次数（1-4次，电脑端页面较长）
        scroll_times = random.randint(1, 4)
        current_position = 0

        for _ in range(scroll_times):
            # 随机滚动距离（100-500像素，适合电脑端页面）
            scroll_distance = random.randint(100, 500)
            # 30% 概率向上滚动
            if random.random() < 0.3:
                scroll_distance = -scroll_distance
            # 确保不超出页面范围
            if 0 <= current_position + scroll_distance < page_height:
                driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
                current_position += scroll_distance
            else:
                # 滚动到顶部或底部
                driver.execute_script("window.scrollTo(0, arguments[0]);",
                                      0 if current_position + scroll_distance < 0 else page_height)
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

        # 执行33次电脑端搜索
        for i in range(pc_num):
            keyword = random.choice(keywords)
            print(f"执行第 {i + 1} 次电脑端搜索: {keyword}")
            bing_search(keyword)

        print("已完成 %d 次电脑端搜索！"%pc_num)

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()