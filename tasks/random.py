import webbrowser
import time

x = True
while x:
    time.sleep(1800)
    chrome_path = r"c:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None,  
                        webbrowser.BackgroundBrowser(chrome_path)) 
    webbrowser.get('chrome').open('https://www.google.com/search?q=exercise&tbm=isch&ved=2ahUKEwi355b477yDAxVsAfsDHWPeDvgQ2-cCegQIABAA&oq=exercise&gs_lcp=CgNpbWcQAzIKCAAQgAQQigUQQzIKCAAQgAQQigUQQzIKCAAQgAQQigUQQzIKCAAQgAQQigUQQzIKCAAQgAQQigUQQzIKCAAQgAQQigUQQzIKCAAQgAQQigUQQzIFCAAQgAQyBQgAEIAEMgUIABCABDoGCAAQBxAeULsDWN0ZYKoeaAFwAHgAgAHRAYgB_QaSAQUwLjUuMZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=0AuTZbe_HOyC7M8P47y7wA8&bih=738&biw=1536#imgrc=6pfWI1gdAihngM')