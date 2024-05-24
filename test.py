import asyncio
from pyppeteer import launch

async def main():
    # Khởi tạo trình duyệt
    browser = await launch(headless=False)
    page = await browser.newPage()

    # Điều hướng đến trang web
    await page.goto('https://www.google.com')

    # Chờ trang web được tải hoàn toàn
    await page.waitForSelector('input[name="q"]')

    # Nhập "Python" vào ô tìm kiếm
    await page.type('input[name="q"]', 'Python')

    # Nhấn Enter để tìm kiếm
    await page.keyboard.press('Enter')

    # Chờ trang kết quả được tải
    await page.waitForNavigation()

    # Click vào liên kết đầu tiên trong kết quả
    await page.click('h3')

    # Chờ một lúc để xem kết quả
    await asyncio.sleep(5)

    # Đóng trình duyệt
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
