from playwright.sync_api import sync_playwright
import time
import csv
with sync_playwright() as p :
    
    browser = p.chromium.launch(headless=False, slow_mo=50)
    
    page = browser.new_page()
    print("Browser opened Successfully")
    
    job_links = []
    
    for i in range(9):
        url = f"https://wuzzuf.net/search/jobs?q=data%20analyst&start={i}&a=navbg"
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
    
        try:      
            page.locator("h2.css-193uk2c a").first.wait_for()
            elements = page.locator("h2.css-193uk2c a").all()
    
    
    
            for el in elements :
                href = el.get_attribute("href")
                
                if "wuzzuf.net" not in href:
                    href = "http://wuzzuf.net" + href 
                
                job_links.append(href)
        except Exception as e:
            # لو ملقاش وظايف في الصفحة دي (النتيجة خلصت)، هيوقف اللوب دي ويكمل
            print(f"No job posted on this page{i+1}")
            break
    print(f"Done Scraping {len(job_links)} Links")
    with open('wuzzuf_data_analyst_jobs_.csv', mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        
        # 3. نكتب أول سطر اللي هو العناوين (Headers)
        writer.writerow(['Job Title', 'Company','Date', 'Type', 'Location', 'Skills', 'Job Link'])
        
        for link in job_links:
            try:
                page.goto(link)
                
                job_title = page.locator("h1.css-gkdl1m").inner_text()
                
                company_loc = page.locator("a.css-p7pghv span").first
                company = company_loc.inner_text(timeout=1000).replace("...", "").strip()
                
                Date = page.locator("span.css-154erwh").first.inner_text()
                
                raw_location = page.locator("strong.css-1vlp604").first.inner_text()
                Location = raw_location.replace("...", "").split("-")[-1].strip() if "-" in raw_location else raw_location
                
                try:
                    block_list = page.locator("span.css-dmid6b").all_inner_texts()

                    Type = ", ".join(block_list).replace("\n", " ").strip() if block_list else "N/A"
                except:
                    Type = "N/A"            
                
                possible_skills_selectors = ["span.css-1vi25m1", "a.css-g65o95", "a.css-5x9pm1"]
                skills_list = []
                
                for selector in possible_skills_selectors:
                    try:
                        # بنجبره يستنى لحد ثانية ونص عشان ندي فرصة للمهارات تظهر
                        page.locator(selector).first.wait_for(timeout=1500)
                        skills_list = page.locator(selector).all_inner_texts()
                        break # لو لقاها بيقفل اللوب
                    except:
                        continue # لو ملقاش الكلاس ده، يروح يجرب الكلاس اللي بعده
                        
                Skills = ", ".join(skills_list) if skills_list else "N/A"
            
                print(f"✔️ {job_title} | {company}  ")
                writer.writerow([job_title, company,Date, Type, Location, Skills, link])
            except Exception as e:
                print(f"Error in link {link}: {e}")
    browser.close()
    print("\n🎉Data Saved in 'wuzzuf_data_analyst_jobs.csv' ")