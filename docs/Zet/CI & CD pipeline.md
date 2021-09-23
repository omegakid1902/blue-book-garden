# CI & CD Pipeline

- metadata
	- UID: P-210717-0937
	- tags: #created/2021/Jul/17, #permanent/concept 
	- source: 
	- related: [[Pipeline]], [[CD - Continuous Delivery]]

## Notes
CI & CD Pipeline là một chuỗi các công việc được hiện tuần tự trong [[CI & CD]]. Bao gồm các bước cơ bản:
- Source: Developer thay đổi source, commit và push lên repo.
- Build: Source code được build, nếu quá trình build xảy ra lỗi, nó sẽ dừng và developer sẽ phải fix và bắt đầu lại bước đầu.
- Test: Sau quá trình build, Output có thể nhiều đối tượng nhưng thường là một phần mềm thực thi, và trải qua công đoạn test để kiểm tra việc chạy có đúng với mong muốn
- Deploy: Gửi cho người dùng cuối chạy thử hoặc triển khai trên môi trường thực.

## Questions & thoughts:
- [ ] Code được build và triển khai qua các [[Docker]], Docker là gì? #question❓ 
- [ ] 
