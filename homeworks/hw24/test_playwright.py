from playwright.sync_api import sync_playwright, expect


def test_saucedemo():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("input[name='user-name']").fill("standard_user")
    page.locator("input[name='password']").fill("secret_sauce")
    (expect(page.locator('input[id="user-name"]')).
     to_have_value('standard_user'))
    expect(page.locator('input[id="password"]')).to_have_value('secret_sauce')
    page.locator("input[name='login-button']").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".inventory_list")).to_be_visible()
    page.locator("button[name='add-to-cart-sauce-labs-backpack']").click()
    expect(page.locator('[class=shopping_cart_badge]')).to_have_text('1')
    page.locator("a[data-test='shopping-cart-link']").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    page.locator("button[name='checkout']").click()
    (expect(page).
     to_have_url("https://www.saucedemo.com/checkout-step-one.html"))
    expect(page.locator('input[id="first-name"]')).to_be_empty()
    expect(page.locator('input[id="last-name"]')).to_be_empty()
    expect(page.locator('input[id="postal-code"]')).to_be_empty()
    page.locator("input[id='first-name']").fill("Nikita")
    page.locator("input[id='last-name']").fill("Kotovich")
    page.locator("input[id='postal-code']").fill("00112233")
    expect(page.locator('input[id="first-name"]')).to_have_value('Nikita')
    expect(page.locator('input[id="last-name"]')).to_have_value('Kotovich')
    expect(page.locator('input[id="postal-code"]')).to_have_value('00112233')
    page.locator("input[id='continue']").click()
    (expect(page).
     to_have_url("https://www.saucedemo.com/checkout-step-two.html"))
    expect(page.locator('[class=title]')).to_have_text('Checkout: Overview')
    expect(page.locator('[class=app_logo]')).to_have_text('Swag Labs')
    page.locator("button[name='finish']").click()
    (expect(page).
     to_have_url("https://www.saucedemo.com/checkout-complete.html"))
    expect(page.locator('[class=title]')).to_have_text('Checkout: Complete!')
    (expect(page.locator('[class=complete-header]')).
     to_have_text('Thank you for your order!'))
    expect(page.locator("img.pony_express")).to_be_visible()
    page.locator("button[id='back-to-products']").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.locator("button[id='react-burger-menu-btn']").click()
    (expect(page.locator("[data-test='inventory-sidebar-link']")).
     to_have_text("All Items"))
    (expect(page.locator("[data-test='about-sidebar-link']")).
     to_have_text("About"))
    (expect(page.locator("[data-test='logout-sidebar-link']")).
     to_have_text("Logout"))
    (expect(page.locator("[data-test='reset-sidebar-link']")).
     to_have_text("Reset App State"))
    page.locator("[id='logout_sidebar_link']").click()
    expect(page).to_have_url("https://www.saucedemo.com/")
    browser.close()
    playwright.stop()
