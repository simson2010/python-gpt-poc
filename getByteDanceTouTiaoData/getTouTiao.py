import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://www.toutiao.com/?channel=follow&source=tuwen_detail&wid=1695498028576"  # 替换为你要访问的URL


def run():
    global driver
    # 配置浏览器驱动，这里以Chrome为例
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')  # 禁用GPU加速

    # 配置浏览器驱动，这里以Chrome为例
    driver = webdriver.Chrome()  # 需要提前下载和配置Chrome驱动，并指定其路径


    # 加载页面
    driver.get(url)

    # 等待页面加载完成（可根据需要调整等待时间）
    #driver.implicitly_wait(10)  # 最多等待10秒钟

    # 执行其他操作，如填写表单、点击按钮等
    # ...

    # 获取页面源代码
    page_source = driver.page_source

    print(page_source)
    # 关闭浏览器
    # driver.quit()

    # 处理页面源代码
    # ...
    time.sleep(5)

    search_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div[1]/div/div/div/div[1]/div/ul/li[6]/div/div') 
    print(search_button)
    search_button.click()

    time.sleep(10)

    all_links = driver.find_elements(By.XPATH, '//div[@class="feed-card-article-l"]/a')
    for link in all_links:
        print(link.get_attribute('href'))
        print(link.text)

if __name__ == '__main__':
    run()
    input('Press ENTER to exit...')