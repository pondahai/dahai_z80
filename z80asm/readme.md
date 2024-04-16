這是z80的組譯器  
來自：http://www.trs-80emulators.com/z80asm/  
主要使用方法
```
z80asm.exe 原始碼 -cim
```
結果會產生 .lst 以及二進制檔 .cim  

另外 conv.py 這隻程式是用來把.cim檔轉換成c語言陣列變數格式  
以便用來把程式碼放在arduino程式裡面  
使用方法：
```
python3 conv.py 二進位碼檔.cim
```
他會直接輸出結果到標準輸出  
可以直接在命令列視窗中複製  
或者用轉向指令把結果存成檔案再進行後續處理  
