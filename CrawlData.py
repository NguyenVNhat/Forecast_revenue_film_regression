import requests
from bs4 import BeautifulSoup
import pandas as pd
import Budget

def scrape_box_office_mojo(year):
    url = "https://www.boxofficemojo.com/year/{year}/?area=VN&grossesOption=totalGrosses&sort=gross".format(year=year)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        if table:
            movie_data = []
            for row in table.find_all('tr')[1:]:
                cells = row.find_all('td')
                if len(cells) >= 3:
                    year = year
                    releasegroup = cells[1].text.strip()
                    gross = cells[5].text.strip()
                    maxtheater = cells[6].text.strip()
                    openning = cells[7].text.strip()
                    percentoftotal = cells[8].text.strip()
                    openningtheater = cells[9].text.strip()
                    dateopen = cells[10].text.strip()
                    movie_data.append([releasegroup, gross, maxtheater, openning, percentoftotal, openningtheater,dateopen,year])
            return movie_data
        else:
            print("Không tìm thấy bảng dữ liệu.")
            return None
    else:
        print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)
        return None

# Tạo DataFrame từ dữ liệu của mỗi năm
years = [2016,2017,2018,2019,2020,2021,2022,2023,2024]
all_years_data = []
for y in years:
    year_data = scrape_box_office_mojo(y)
    if year_data:
        all_years_data.extend(year_data)

df = pd.DataFrame(all_years_data, columns=[ "Release Group", "Gross", "Maxtheater", "Openning", "Percent of total", "Openning theater","Date","Year"])
df = df.replace('-','')
output_file = "data_old.csv"
df.to_csv(output_file, index=False)
print("Dữ liệu đã được xuất thành công ra file:", output_file)
