---
title: UTF-8
UID: 210831205040
tags:
  - '#created/2021/Aug/31'
  - '#seed🥜'
  - '#permanent/concept'
aliases:
  - UTF-8
---
# UTF-8

## Notes:
UTF-8 là một loại mã hóa [[UTF]] để chuyển đổi Unicode.
UTF-8 dùng 1byte để biểu diễn ký tự tiếng Anh chuẩn. Dùng 2 bytes để biểu diễn các ký tự Latinh và Trung Đông. 3 bytes cho các ký tự châu Á
Ví dụ: [wiki](https://vi.wikipedia.org/wiki/Unicode)
- 1 byte: dùng để biểu diễn 128 ký tự [[ASCII]], tức những mã có giá trị < 0x80. 
- Với ký tự nhỏ hơn 0x800, sử dụng 2 bytes để biểu diễn, byte thứ nhất có giá trị 0xC0 cộng với 5 bit từ thứ 7 tới 11; byte thứ hai có giá trị 0x80 cộng với các bit từ thứ 1 tới thứ 6. 
- ...	

## Ideas & thoughts:

## Questions:


## Tham khảo:
```dataview
list
from [[UTF-8]]
sort file.name asc
```