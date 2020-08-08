# Mã nguồn : Python + Scrapy
def parse(self, response) có 2 phần:
+) Phần đầu thực hiện kiểm tra xem link có phải là bài báo không. Nếu đúng thực hiện việc ghi : link, time, title, sapo, content, author ra file .text
+) Nếu không phải thì thực hiện việc gọi callback lại hàm parse. Và trong hàm yield chỉ chọn những link có dạng : "https://24h.com.vn/"
# Các công việc đã thực hiện được: lấy được link, time, title, sapo, content, author của một bài viết.
# Kết quả : Thu thập 20000 bài báo trên trang https://24h.com.vn/, tốc độ 1000+/phút và lưu trong file bao24h_output.txt