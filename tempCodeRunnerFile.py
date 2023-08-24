    for row in rows:
        cols = row.find_elements(By.TAG_NAME,'td')
        temp_data = []
        try:
            
            temp_data.append({
                cols[0].text:cols[1].text

            })
        except:
            print("NO")
        
        data.append(temp_data)